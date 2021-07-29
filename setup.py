from setuptools import setup, find_packages

setup(
    name="home-assistant-frontend",
    version="20210729.0",
    description="The Home Assistant frontend",
    url="https://github.com/home-assistant/frontend",
    author="The Home Assistant Authors",
    author_email="hello@home-assistant.io",
    license="Apache-2.0",
    packages=find_packages(include=["hass_frontend", "hass_frontend.*"]),
    include_package_data=True,
    zip_safe=False,
)
