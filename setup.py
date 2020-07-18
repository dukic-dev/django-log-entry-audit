from setuptools import find_packages, setup


def read(f):
    return open(f, "r", encoding="utf-8").read()


setup(
    name="django-log-entry-audit",
    version=0.1,
    description="A Django app which adds Log Entry model.",
    long_description=read("README.md"),
    author="Daniel Đukić",
    author_email="daniel@dukic.dev",
    license="MIT",
    install_requires=["django>=3.0", "psycopg2>=2.8.5", "django-enumfields>=2.0.0"],
    python_requires=">=3.8",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=True,
)
