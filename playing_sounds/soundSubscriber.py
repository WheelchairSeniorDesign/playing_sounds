import rclpy
from rclpy.node import Node
import playing_sounds.playingsoundcode
from wheelchair_sensor_msgs.msg import Sounds


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('sound_subscriber')
        self.subscription = self.create_subscription(
            Sounds,
            'sounds',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        playing_sounds.playingsoundcode.soundPlay(msg.sound_file, msg.volume/100.0)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()