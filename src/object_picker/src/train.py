#!/usr/bin/env python

from datetime import datetime
import math

import numpy as np
import time
import rospy
from gymnasium import spaces, utils, Env
import actionlib
import tf2_ros
from tf2_geometry_msgs import PoseStamped
from tf.transformations import quaternion_inverse, quaternion_multiply
from urdf_parser_py.urdf import URDF
from geometry_msgs.msg import (
    Pose,
    Quaternion,
    Vector3,
    TransformStamped,
    Transform,
    Point,
)
from sensor_msgs.msg import JointState
from control_msgs.msg import JointControllerState
from std_msgs.msg import Float32, Float64, Float64MultiArray, Header, ColorRGBA
from rospy.exceptions import ROSException, ROSInterruptException
from gazebo_msgs.srv import SetPhysicsProperties
from std_srvs.srv import Empty


# IMPORTANT: Run the following two processes in separate terminals before running this script:
#   1. `roscore`
#   2. `roslaunch interbotix_xsarm_gazebo xsarm_gazebo.launch robot_model:=px100 use_position_controllers:=true`


# Valid position ranges
WAIST_LIM = (-3.141583, 3.141583)
SHOULDER_LIM = (-1.937315, 1.867502)
ELBOW_LIM = (-2.111848, 1.605703)
WRIST_ANGLE_LIM = (-1.745329, 2.146755)
RIGHT_FINGER_LIM = (-0.036, -0.017)
LEFT_FINGER_LIM = (0.017, 0.036)

# Max position change per step
MAX_WAIST_DELTA = (WAIST_LIM[1] - WAIST_LIM[0]) / 25
MAX_SHOULDER_DELTA = (SHOULDER_LIM[1] - SHOULDER_LIM[0]) / 30
MAX_ELBOW_DELTA = (ELBOW_LIM[1] - ELBOW_LIM[0]) / 15
MAX_WRIST_ANGLE_DELTA = (WRIST_ANGLE_LIM[1] - WRIST_ANGLE_LIM[0]) / 15
MAX_RIGHT_FINGER_DELTA = (RIGHT_FINGER_LIM[1] - RIGHT_FINGER_LIM[0]) / 5
MAX_LEFT_FINGER_DELTA = (LEFT_FINGER_LIM[1] - LEFT_FINGER_LIM[0]) / 5

# Observation space bounds
OBS_SPACE_LOW = [
    WAIST_LIM[0],
    SHOULDER_LIM[0],
    ELBOW_LIM[0],
    WRIST_ANGLE_LIM[0],
    RIGHT_FINGER_LIM[0],
    LEFT_FINGER_LIM[0],
]
OBS_SPACE_HIGH = [
    WAIST_LIM[1],
    SHOULDER_LIM[1],
    ELBOW_LIM[1],
    WRIST_ANGLE_LIM[1],
    RIGHT_FINGER_LIM[1],
    LEFT_FINGER_LIM[1],
]

# Action space bounds
ACTION_SPACE_LOW = [
    -MAX_WAIST_DELTA,
    -MAX_SHOULDER_DELTA,
    -MAX_ELBOW_DELTA,
    -MAX_WRIST_ANGLE_DELTA,
    -MAX_RIGHT_FINGER_DELTA,
    -MAX_LEFT_FINGER_DELTA,
]
ACTION_SPACE_HIGH = [
    MAX_WAIST_DELTA,
    MAX_SHOULDER_DELTA,
    MAX_ELBOW_DELTA,
    MAX_WRIST_ANGLE_DELTA,
    MAX_RIGHT_FINGER_DELTA,
    MAX_LEFT_FINGER_DELTA,
]


class PX100GazeboClient:
    WAIST_CMD_TOPIC = "/px100/waist_controller/command"
    SHOULDER_CMD_TOPIC = "/px100/shoulder_controller/command"
    ELBOW_CMD_TOPIC = "/px100/elbow_controller/command"
    WRIST_ANGLE_CMD_TOPIC = "/px100/wrist_angle_controller/command"
    RIGHT_FINGER_CMD_TOPIC = "/px100/right_finger_controller/command"
    LEFT_FINGER_CMD_TOPIC = "/px100/left_finger_controller/command"

    WAIST_STATE_TOPIC = "/px100/waist_controller/state"
    SHOULDER_STATE_TOPIC = "/px100/shoulder_controller/state"
    ELBOW_STATE_TOPIC = "/px100/elbow_controller/state"
    WRIST_ANGLE_STATE_TOPIC = "/px100/wrist_angle_controller/state"
    RIGHT_FINGER_STATE_TOPIC = "/px100/right_finger_controller/state"
    LEFT_FINGER_STATE_TOPIC = "/px100/left_finger_controller/state"

    CLOSENESS_TOL = 0.01

    def __init__(self):
        rospy.init_node("px100_gazebo_client", anonymous=True)
        self.rate = rospy.Rate(15)

        self.waist_pub = rospy.Publisher(self.WAIST_CMD_TOPIC, Float64, queue_size=10)
        self.shoulder_pub = rospy.Publisher(
            self.SHOULDER_CMD_TOPIC, Float64, queue_size=10
        )
        self.elbow_pub = rospy.Publisher(self.ELBOW_CMD_TOPIC, Float64, queue_size=10)
        self.wrist_angle_pub = rospy.Publisher(
            self.WRIST_ANGLE_CMD_TOPIC, Float64, queue_size=10
        )
        self.right_finger_pub = rospy.Publisher(
            self.RIGHT_FINGER_CMD_TOPIC, Float64, queue_size=10
        )
        self.left_finger_pub = rospy.Publisher(
            self.LEFT_FINGER_CMD_TOPIC, Float64, queue_size=10
        )

        self.waist_sub = rospy.Subscriber(
            self.WAIST_STATE_TOPIC, JointControllerState, self.waist_state_callback
        )
        self.shoulder_sub = rospy.Subscriber(
            self.SHOULDER_STATE_TOPIC,
            JointControllerState,
            self.shoulder_state_callback,
        )
        self.elbow_sub = rospy.Subscriber(
            self.ELBOW_STATE_TOPIC, JointControllerState, self.elbow_state_callback
        )
        self.wrist_angle_sub = rospy.Subscriber(
            self.WRIST_ANGLE_STATE_TOPIC,
            JointControllerState,
            self.wrist_angle_state_callback,
        )
        self.right_finger_sub = rospy.Subscriber(
            self.RIGHT_FINGER_STATE_TOPIC,
            JointControllerState,
            self.right_finger_state_callback,
        )
        self.left_finger_sub = rospy.Subscriber(
            self.LEFT_FINGER_STATE_TOPIC,
            JointControllerState,
            self.left_finger_state_callback,
        )

        self.waist_state = None
        self.shoulder_state = None
        self.elbow_state = None
        self.wrist_angle_state = None
        self.right_finger_state = None
        self.left_finger_state = None

    def waist_state_callback(self, msg):
        self.waist_state = msg

    def shoulder_state_callback(self, msg):
        self.shoulder_state = msg

    def elbow_state_callback(self, msg):
        self.elbow_state = msg

    def wrist_angle_state_callback(self, msg):
        self.wrist_angle_state = msg

    def right_finger_state_callback(self, msg):
        self.right_finger_state = msg

    def left_finger_state_callback(self, msg):
        self.left_waist_pos = msg

    def _clip_value(self, value, limits):
        """
        Clips the input value to the specified limits.
        :param value: The input value to clip.
        :param limits: A tuple (min, max) representing the joint limits.
        :return: The clipped value.
        """
        min_limit, max_limit = limits
        return max(min(value, max_limit), min_limit)

    def _await_subscriptions(self):
        while any(
            [
                self.waist_state is None,
                self.shoulder_state is None,
                self.elbow_state is None,
                self.wrist_angle_state is None,
                self.right_finger_state is None,
                # HACK: This one never publishes
                # self.left_finger_state is None,
            ]
        ):
            self.rate.sleep()

    def _wait_until_set_points_reached(self):
        while not rospy.is_shutdown() and not all(
            [
                self.waist_state is not None
                and math.isclose(
                    self.waist_state.process_value,
                    self.waist_state.set_point,
                    abs_tol=self.CLOSENESS_TOL,
                ),
                self.shoulder_state is not None
                and math.isclose(
                    self.shoulder_state.process_value,
                    self.shoulder_state.set_point,
                    abs_tol=self.CLOSENESS_TOL,
                ),
                self.elbow_state is not None
                and math.isclose(
                    self.elbow_state.process_value,
                    self.elbow_state.set_point,
                    abs_tol=self.CLOSENESS_TOL,
                ),
                self.wrist_angle_state is not None
                and math.isclose(
                    self.wrist_angle_state.process_value,
                    self.wrist_angle_state.set_point,
                    abs_tol=self.CLOSENESS_TOL,
                ),
                self.right_finger_state is not None
                and math.isclose(
                    self.right_finger_state.process_value,
                    self.right_finger_state.set_point,
                    abs_tol=self.CLOSENESS_TOL,
                ),
                # HACK: This one never publishes
                # self.left_finger_state is not None
                # and math.isclose(
                #     self.left_finger_state.process_value,
                #     self.left_finger_state.set_point,
                #     abs_tol=MAX_LEFT_FINGER_DELTA
                #     * self.CLOSENESS_TOL_PROPORTION_OF_MAX_DELTA,
                # ),
            ]
        ):
            print("\nJoint Progress:")
            for joint in [
                ("Waist", self.waist_state),
                ("Shoulder", self.shoulder_state),
                ("Elbow", self.elbow_state),
                ("Wrist Angle", self.wrist_angle_state),
                ("Right Finger", self.right_finger_state),
                ("Left Finger", self.left_finger_state),
            ]:
                joint_name, joint_state = joint

                if joint_state is not None:
                    # Calculate the difference between the set point and current position
                    difference = abs(joint_state.set_point - joint_state.process_value)
                    print(
                        f"{joint_name} - Set Point: {joint_state.set_point:.4f}, "
                        f"Current Position: {joint_state.process_value:.4f}, "
                        f"Tol: {self.CLOSENESS_TOL:.4f}, Difference: {difference:.4f}"
                    )
                else:
                    print(f"{joint_name} - State: None")

    def set_joint_positions(
        self,
        waist=None,
        shoulder=None,
        elbow=None,
        wrist_angle=None,
        right_finger=None,
        left_finger=None,
    ):
        """
        Set the joint positions for the PX100 arm.
        :param waist: Position for the waist joint (in radians).
        :param shoulder: Position for the shoulder joint (in radians).
        :param elbow: Position for the elbow joint (in radians).
        :param wrist_angle: Position for the wrist angle joint (in radians).
        :param right_finger: Position for the right finger joint (normalized between 0 and 1).
        :param left_finger: Position for the left finger joint (normalized between 0 and 1).
        """
        self._await_subscriptions()
        rospy.loginfo(
            f"Setting joint positions:\n{waist:.4f}, {shoulder:.4f}, {elbow:.4f}, "
            f"{wrist_angle:.4f}, {right_finger:.4f}, {left_finger:.4f}"
        )
        self.rate.sleep()
        if waist is not None:
            waist_position = self._clip_value(waist, WAIST_LIM)
            self.waist_pub.publish(waist_position)
            self.rate.sleep()
        if shoulder is not None:
            shoulder_position = self._clip_value(shoulder, SHOULDER_LIM)
            self.shoulder_pub.publish(shoulder_position)
            self.rate.sleep()
        if elbow is not None:
            elbow_position = self._clip_value(elbow, ELBOW_LIM)
            self.elbow_pub.publish(elbow_position)
            self.rate.sleep()
        if wrist_angle is not None:
            wrist_angle_position = self._clip_value(wrist_angle, WRIST_ANGLE_LIM)
            self.wrist_angle_pub.publish(wrist_angle_position)
            self.rate.sleep()
        if right_finger is not None:
            right_finger_position = self._clip_value(right_finger, RIGHT_FINGER_LIM)
            self.right_finger_pub.publish(right_finger_position)
            self.rate.sleep()
        if left_finger is not None:
            left_finger_position = self._clip_value(left_finger, LEFT_FINGER_LIM)
            self.left_finger_pub.publish(left_finger_position)
            self.rate.sleep()

        # Wait until set points have more or less been reached
        self._wait_until_set_points_reached()


class PX100PickEnv(Env):
    def __init__(self):
        self.action_space = spaces.Box(
            low=ACTION_SPACE_LOW, high=ACTION_SPACE_HIGH, dtype=np.float32
        )
        self.observation_space = spaces.Box(
            low=OBS_SPACE_LOW, high=OBS_SPACE_HIGH, dtype=np.float32
        )
        self.state = None
        self.done = False

    def reset(self, seed=None, options=None):
        """
        Reset the environment to the initial state and return the first observation.

        Args:
            seed (int, optional): Random seed for reproducibility.
            return_info (bool, optional): Whether to return additional info along with the observation.
            options (dict, optional): Additional options for resetting the environment.

        Returns:
            observation (np.ndarray): The first observation after reset.
        """
        # Initialize state (example: random values between -1 and 1 for a 4D state space)
        self.state = np.random.uniform(-1, 1, size=(4,))
        return self.state

    def step(self, action):
        """
        Apply the given action and return the new state, reward, done flag, and info.

        Args:
            action (int): The action taken by the agent.

        Returns:
            tuple: (next_state, reward, done, info)
        """
        # Example: Move state based on action
        # Here you can define how the action modifies the state.
        self.state = np.random.uniform(
            -1, 1, size=(4,)
        )  # Random next state as a placeholder

        # Example reward calculation (this would depend on your environment logic)
        reward = 1.0  # A placeholder reward

        # Example done flag (environment logic would determine when it's done)
        done = False  # Change based on your logic

        return self.state, reward, done, {}


def unpause_gazebo():
    rospy.wait_for_service("/gazebo/unpause_physics")
    unpause_gazebo = rospy.ServiceProxy("/gazebo/unpause_physics", Empty)
    unpause_gazebo()


def pause_gazebo():
    rospy.wait_for_service("/gazebo/pause_physics")
    pause_gazebo = rospy.ServiceProxy("/gazebo/pause_physics", Empty)
    pause_gazebo()


if __name__ == "__main__":
    import random

    unpause_gazebo()
    time.sleep(1)  # Necessary after unpause
    client = PX100GazeboClient()
    client.set_joint_positions(
        waist=random.uniform(*WAIST_LIM),
        shoulder=random.uniform(*SHOULDER_LIM) / 2,
        elbow=random.uniform(*ELBOW_LIM) / 2,
        wrist_angle=random.uniform(*WRIST_ANGLE_LIM) / 2,
        right_finger=random.uniform(*RIGHT_FINGER_LIM) / 2,
        left_finger=random.uniform(*LEFT_FINGER_LIM) / 2,
    )
