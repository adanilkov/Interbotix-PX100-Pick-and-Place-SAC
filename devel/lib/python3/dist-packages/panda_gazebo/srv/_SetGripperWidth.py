# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from panda_gazebo/SetGripperWidthRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class SetGripperWidthRequest(genpy.Message):
  _md5sum = "9f982499773828152675649f173b5489"
  _type = "panda_gazebo/SetGripperWidthRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Service that can be used to control the robot hand gripper width using the panda_control_server.
# NOTE: It serves as a small wrapper around the 'franka_gripper/move' action but automatically
# sets the speed to the maximum speed. It further clips gripper width such that it is within
# the set max/min boundaries.
float64 width       # Gripper width - ignored when the gripper is grasping.
bool grasping       # The gripper simply moves if this is `false` ignoring the 'max_effort'.
float64 max_effort  # The max effort used by the gripper.
bool wait
duration timeout # Action server timeout. If set to 0, no timeout is used and action waits indefinitely.
"""
  __slots__ = ['width','grasping','max_effort','wait','timeout']
  _slot_types = ['float64','bool','float64','bool','duration']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       width,grasping,max_effort,wait,timeout

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetGripperWidthRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.width is None:
        self.width = 0.
      if self.grasping is None:
        self.grasping = False
      if self.max_effort is None:
        self.max_effort = 0.
      if self.wait is None:
        self.wait = False
      if self.timeout is None:
        self.timeout = genpy.Duration()
    else:
      self.width = 0.
      self.grasping = False
      self.max_effort = 0.
      self.wait = False
      self.timeout = genpy.Duration()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_dBdB2i().pack(_x.width, _x.grasping, _x.max_effort, _x.wait, _x.timeout.secs, _x.timeout.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.timeout is None:
        self.timeout = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 26
      (_x.width, _x.grasping, _x.max_effort, _x.wait, _x.timeout.secs, _x.timeout.nsecs,) = _get_struct_dBdB2i().unpack(str[start:end])
      self.grasping = bool(self.grasping)
      self.wait = bool(self.wait)
      self.timeout.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_dBdB2i().pack(_x.width, _x.grasping, _x.max_effort, _x.wait, _x.timeout.secs, _x.timeout.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.timeout is None:
        self.timeout = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 26
      (_x.width, _x.grasping, _x.max_effort, _x.wait, _x.timeout.secs, _x.timeout.nsecs,) = _get_struct_dBdB2i().unpack(str[start:end])
      self.grasping = bool(self.grasping)
      self.wait = bool(self.wait)
      self.timeout.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_dBdB2i = None
def _get_struct_dBdB2i():
    global _struct_dBdB2i
    if _struct_dBdB2i is None:
        _struct_dBdB2i = struct.Struct("<dBdB2i")
    return _struct_dBdB2i
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from panda_gazebo/SetGripperWidthResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetGripperWidthResponse(genpy.Message):
  _md5sum = "937c9679a518e3a18d831e57125ea522"
  _type = "panda_gazebo/SetGripperWidthResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool success
string message

"""
  __slots__ = ['success','message']
  _slot_types = ['bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success,message

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetGripperWidthResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
      if self.message is None:
        self.message = ''
    else:
      self.success = False
      self.message = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.success
      buff.write(_get_struct_B().pack(_x))
      _x = self.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.message = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.success
      buff.write(_get_struct_B().pack(_x))
      _x = self.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.message = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class SetGripperWidth(object):
  _type          = 'panda_gazebo/SetGripperWidth'
  _md5sum = 'f1391f700eac44a55b7a2011ef94058b'
  _request_class  = SetGripperWidthRequest
  _response_class = SetGripperWidthResponse