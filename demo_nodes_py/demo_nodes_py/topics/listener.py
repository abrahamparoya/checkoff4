# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from words2number import w2n
from num2words import num2words
from std_msgs.msg import String


class Listener(Node):

    def __init__(self):
        super().__init__('abe')
        self.sub = self.create_subscription(String, 'chatter', self.chatter_callback, 10)

    def chatter_callback(self, msg):
        text = msg.data
        text.replace("Hello World: ", "")
        number = w2n.word_to_num(text)
        newMsg = msg.data
        newMsg = newMsg.replace(text, str(number))
        msg.data.replace(text, str(number))
        self.get_logger().info('Abe heard: [ECE 4532 -> %s]' % newMsg)


def main(args=None):
    rclpy.init(args=args)

    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
