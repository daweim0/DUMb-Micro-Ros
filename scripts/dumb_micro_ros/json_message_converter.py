#TODO: this file was copy and pasted from https://github.com/uos/rospy_message_converter/blob/master/src/rospy_message_converter/json_message_converter.py
# we should reference this file in a more official way (maybe a git submodule or ask the rospy_message_converter maintainer for their blessing to copy and paste their code?)

import json

import message_converter


def convert_json_to_ros_message(message_type, json_message, strict_mode=True, log_level='error'):
    """
    Takes in the message type and a JSON-formatted string and returns a ROS
    message.
    :param message_type: The desired ROS message type of the result
    :type  message_type: str
    :param json_message: A JSON-formatted string
    :type  json_message: str
    :param strict_mode: If strict_mode is set, an exception will be thrown if the json message contains extra fields.
    :type  strict_mode: bool, optional
    :param log_level: The log level to be used. Available levels: debug, info, warning, error, critical
    :type  log_level: str, optional
    :return: A ROS message
    :rtype: class:`genpy.Message`
    Example:
        >>> msg_type = "std_msgs/String"
        >>> json_msg = '{"data": "Hello, Robot"}'
        >>> convert_json_to_ros_message(msg_type, json_msg)
        data: "Hello, Robot"
    """
    dictionary = json.loads(json_message)
    return message_converter.convert_dictionary_to_ros_message(message_type, dictionary, strict_mode=strict_mode, log_level=log_level)


def convert_ros_message_to_json(message, binary_array_as_bytes=True):
    """
    Takes in a ROS message and returns a JSON-formatted string.
    :param message: A ROS message to convert
    :type  message: class:`genpy.Message`
    :param binary_array_as_bytes: rospy treats `uint8[]` data as a `bytes`, which is the Python representation for byte
           data. In Python 2, this is the same as `str`. If this parameter is `False`, all `uint8[]` fields will be
           converted to `list(int)` instead.
    :type  binary_array_as_bytes: bool, optional
    :return: A JSON-formatted string
    :rtype:  str
    Example:
        >>> import std_msgs.msg
        >>> ros_message = std_msgs.msg.String(data="Hello, Robot")
        >>> convert_ros_message_to_json(ros_message)
        '{"data": "Hello, Robot"}'
    """
    dictionary = message_converter.convert_ros_message_to_dictionary(message, binary_array_as_bytes)
    json_message = json.dumps(dictionary)
    return json_message


if __name__ == "__main__":
    import doctest

    doctest.testmod()