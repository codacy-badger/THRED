from setuptools import find_packages, setup

setup(
    name="thred",
    version="0.1.0",
    author="Nouha Dziri, Ehsan Kamalloo, Kory Mathewson",
    author_email="dziri@cs.ualberta.ca",
    description="Neural Response Generation Framework",
    long_description=open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    keywords='dialogue-generation sequence-to-sequence tensorflow',
    url="https://github.com/nouhadziri/THRED",
    packages=find_packages(exclude=["*.tests", "*.tests.*",
                                    "tests.*", "tests"]),
    install_requires=['tensorflow_gpu==1.12.0',
                      'tensorflow-hub==0.2.0',
                      'spacy>=2.1.0,<=2.2.0',
                      'h5py>=2.9.0',
                      'scipy>=1.0.0,<2.0.0',
                      'pymagnitude',
                      'redis',
                      'PyYAML',
                      'gensim>=3.4.0',
                      'mistune>=0.8.0',
                      'emot==1.0',
                      'tqdm'],
    python_requires='>=3.5.0',
    tests_require=['pytest'],
)
