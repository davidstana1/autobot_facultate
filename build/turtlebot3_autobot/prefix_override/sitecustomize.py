import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/david/Desktop/autobot_facultate/install/turtlebot3_autobot'
