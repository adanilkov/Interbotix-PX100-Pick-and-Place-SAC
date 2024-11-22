// Auto-generated. Do not edit!

// (in-package panda_gazebo.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class GetMoveItControlledJointsRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetMoveItControlledJointsRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetMoveItControlledJointsRequest
    let len;
    let data = new GetMoveItControlledJointsRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_gazebo/GetMoveItControlledJointsRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Service that can be used to retrieve the joints that are currently controlled by MoveIt.
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GetMoveItControlledJointsRequest(null);
    return resolved;
    }
};

class GetMoveItControlledJointsResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.controlled_joints = null;
      this.controlled_joints_arm = null;
      this.controlled_joints_hand = null;
      this.success = null;
      this.message = null;
    }
    else {
      if (initObj.hasOwnProperty('controlled_joints')) {
        this.controlled_joints = initObj.controlled_joints
      }
      else {
        this.controlled_joints = [];
      }
      if (initObj.hasOwnProperty('controlled_joints_arm')) {
        this.controlled_joints_arm = initObj.controlled_joints_arm
      }
      else {
        this.controlled_joints_arm = [];
      }
      if (initObj.hasOwnProperty('controlled_joints_hand')) {
        this.controlled_joints_hand = initObj.controlled_joints_hand
      }
      else {
        this.controlled_joints_hand = [];
      }
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
      if (initObj.hasOwnProperty('message')) {
        this.message = initObj.message
      }
      else {
        this.message = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetMoveItControlledJointsResponse
    // Serialize message field [controlled_joints]
    bufferOffset = _arraySerializer.string(obj.controlled_joints, buffer, bufferOffset, null);
    // Serialize message field [controlled_joints_arm]
    bufferOffset = _arraySerializer.string(obj.controlled_joints_arm, buffer, bufferOffset, null);
    // Serialize message field [controlled_joints_hand]
    bufferOffset = _arraySerializer.string(obj.controlled_joints_hand, buffer, bufferOffset, null);
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    // Serialize message field [message]
    bufferOffset = _serializer.string(obj.message, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetMoveItControlledJointsResponse
    let len;
    let data = new GetMoveItControlledJointsResponse(null);
    // Deserialize message field [controlled_joints]
    data.controlled_joints = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [controlled_joints_arm]
    data.controlled_joints_arm = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [controlled_joints_hand]
    data.controlled_joints_hand = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [message]
    data.message = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.controlled_joints.forEach((val) => {
      length += 4 + _getByteLength(val);
    });
    object.controlled_joints_arm.forEach((val) => {
      length += 4 + _getByteLength(val);
    });
    object.controlled_joints_hand.forEach((val) => {
      length += 4 + _getByteLength(val);
    });
    length += _getByteLength(object.message);
    return length + 17;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_gazebo/GetMoveItControlledJointsResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'de338cfffbebe92f5e336e5f98b28598';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] controlled_joints
    string[] controlled_joints_arm
    string[] controlled_joints_hand
    bool success
    string message
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GetMoveItControlledJointsResponse(null);
    if (msg.controlled_joints !== undefined) {
      resolved.controlled_joints = msg.controlled_joints;
    }
    else {
      resolved.controlled_joints = []
    }

    if (msg.controlled_joints_arm !== undefined) {
      resolved.controlled_joints_arm = msg.controlled_joints_arm;
    }
    else {
      resolved.controlled_joints_arm = []
    }

    if (msg.controlled_joints_hand !== undefined) {
      resolved.controlled_joints_hand = msg.controlled_joints_hand;
    }
    else {
      resolved.controlled_joints_hand = []
    }

    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    if (msg.message !== undefined) {
      resolved.message = msg.message;
    }
    else {
      resolved.message = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: GetMoveItControlledJointsRequest,
  Response: GetMoveItControlledJointsResponse,
  md5sum() { return 'de338cfffbebe92f5e336e5f98b28598'; },
  datatype() { return 'panda_gazebo/GetMoveItControlledJoints'; }
};