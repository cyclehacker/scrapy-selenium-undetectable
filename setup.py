"""This module contains the packaging routine for the pybook package"""

from setuptools import setup, find_packages

setup(
    name='scrapy-selenium-undetectable',
    version='0.1.0',
    packages=['scrapy_selenium_ud'],
    install_requires=["selenium", "undetected_chromedriver"],
    url="https://github.com/cyclehacker/scrapy-selenium-undetectable.git",
    license="GPL-3.0",
    author="cyclehacker",
    description="""
                This merges scrapy_selenium (https://github.com/clemfromspace/scrapy-selenium) middleware with 
                undetected_chromedriver (https://github.com/ultrafunkamsterdam/undetected-chromedriver) to provide
                an undetectable chromedriver within the scrapy_selenium middleware.
                
                For more information check out the README.""",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)

# from setuptools import setup, find_packages
# try:
#     from pip.download import PipSession
#     from pip.req import parse_requirements
# except ImportError:
#     # It is quick hack to support pip 10 that has changed its internal
#     # structure of the modules.
#     from pip._internal.download import PipSession
#     from pip._internal.req.req_file import parse_requirements
#
#
# def get_requirements(source):
#     """Get the requirements from the given ``source``
#
#     Parameters
#     ----------
#     source: str
#         The filename containing the requirements
#
#     """
#
#     install_reqs = parse_requirements(filename=source, session=PipSession())
#
#     return [str(ir.req) for ir in install_reqs]
#
#
# setup(
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
# )


