// Generated by gencpp from file panda_gazebo/SetEePoseRequest.msg
// DO NOT EDIT!


#ifndef PANDA_GAZEBO_MESSAGE_SETEEPOSEREQUEST_H
#define PANDA_GAZEBO_MESSAGE_SETEEPOSEREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Pose.h>

namespace panda_gazebo
{
template <class ContainerAllocator>
struct SetEePoseRequest_
{
  typedef SetEePoseRequest_<ContainerAllocator> Type;

  SetEePoseRequest_()
    : pose()  {
    }
  SetEePoseRequest_(const ContainerAllocator& _alloc)
    : pose(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _pose_type;
  _pose_type pose;





  typedef boost::shared_ptr< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SetEePoseRequest_

typedef ::panda_gazebo::SetEePoseRequest_<std::allocator<void> > SetEePoseRequest;

typedef boost::shared_ptr< ::panda_gazebo::SetEePoseRequest > SetEePoseRequestPtr;
typedef boost::shared_ptr< ::panda_gazebo::SetEePoseRequest const> SetEePoseRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::panda_gazebo::SetEePoseRequest_<ContainerAllocator1> & lhs, const ::panda_gazebo::SetEePoseRequest_<ContainerAllocator2> & rhs)
{
  return lhs.pose == rhs.pose;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::panda_gazebo::SetEePoseRequest_<ContainerAllocator1> & lhs, const ::panda_gazebo::SetEePoseRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace panda_gazebo

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f192399f711a48924df9a394d37edd67";
  }

  static const char* value(const ::panda_gazebo::SetEePoseRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf192399f711a4892ULL;
  static const uint64_t static_value2 = 0x4df9a394d37edd67ULL;
};

template<class ContainerAllocator>
struct DataType< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "panda_gazebo/SetEePoseRequest";
  }

  static const char* value(const ::panda_gazebo::SetEePoseRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Service that can be used to set the current EE pose and control the robot using\n"
"# MoveIt.\n"
"geometry_msgs/Pose pose\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::panda_gazebo::SetEePoseRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pose);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetEePoseRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::panda_gazebo::SetEePoseRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::panda_gazebo::SetEePoseRequest_<ContainerAllocator>& v)
  {
    s << indent << "pose: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PANDA_GAZEBO_MESSAGE_SETEEPOSEREQUEST_H