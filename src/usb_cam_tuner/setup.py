from setuptools import find_packages, setup

package_name = 'usb_cam_tuner'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/usb_cam_tuner/launch', ['launch/usb_cam_tuner.launch.py']),
        ('share/usb_cam_tuner/launch', ['launch/rpi_cam_input.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='airl-radar',
    maintainer_email='airl-radar@todo.todo',
    description='USB cam tuner using OpenCV and ROS 2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tuner_node = usb_cam_tuner.tuner_node:main'
        ],
    },
)



