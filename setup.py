from setuptools import setup

package_name = 'devel'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='uchida',
    maintainer_email='uchida@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'pub = devel.20231016_pub_test:main',
        'sub = devel.20231016_sub_test:main',
        'speech = devel.sub_speech:main',
        'chat = devel.voice_chat_bot:main',
        ],
    },
)
