from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='Emotion Detection using Watson NLP',
    author='Frederick Sundeep',
)
