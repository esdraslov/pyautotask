from setuptools import setup, find_packages


setup(
    name="pyautotask",
    version="0.0.1",
    packages=find_packages('./epack/'),
    install_requires=["pywin32", "pyautogui", "pynput"]
)