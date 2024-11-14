# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from brl_pxh_api/JointRadGoal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class JointRadGoal(genpy.Message):
  _md5sum = "4e2eff58f579aff3380de47294f5becc"
  _type = "brl_pxh_api/JointRadGoal"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Goal
string joint_name
float32 position
float32 moving_time
float32 accel_time
bool blocking 
"""
  __slots__ = ['joint_name','position','moving_time','accel_time','blocking']
  _slot_types = ['string','float32','float32','float32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       joint_name,position,moving_time,accel_time,blocking

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(JointRadGoal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.joint_name is None:
        self.joint_name = ''
      if self.position is None:
        self.position = 0.
      if self.moving_time is None:
        self.moving_time = 0.
      if self.accel_time is None:
        self.accel_time = 0.
      if self.blocking is None:
        self.blocking = False
    else:
      self.joint_name = ''
      self.position = 0.
      self.moving_time = 0.
      self.accel_time = 0.
      self.blocking = False

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
      _x = self.joint_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3fB().pack(_x.position, _x.moving_time, _x.accel_time, _x.blocking))
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
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.joint_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.joint_name = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.position, _x.moving_time, _x.accel_time, _x.blocking,) = _get_struct_3fB().unpack(str[start:end])
      self.blocking = bool(self.blocking)
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
      _x = self.joint_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3fB().pack(_x.position, _x.moving_time, _x.accel_time, _x.blocking))
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
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.joint_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.joint_name = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.position, _x.moving_time, _x.accel_time, _x.blocking,) = _get_struct_3fB().unpack(str[start:end])
      self.blocking = bool(self.blocking)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3fB = None
def _get_struct_3fB():
    global _struct_3fB
    if _struct_3fB is None:
        _struct_3fB = struct.Struct("<3fB")
    return _struct_3fB