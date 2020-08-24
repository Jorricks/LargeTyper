from setuptools import setup

test_dependencies = [
    "pytest==5.4.2",
    "pytest-asyncio==0.12.0",
    "pytest-cov==2.9.0",
    "requests==2.23.0",
]

lint_dependencies = ["flake8==3.8.2"]

setup(
    name="large-typer",
    description="Allow you and your family to type on your smart phone with one computer showing what you typed.",
    version='1.0.0',
    url="https://github.com/Jorricks/LargeTyper",
    maintainer="Jorrick Sleijster",
    packages=[
        "large_typer",
        "large_typer.static"
    ],
    include_package_data=True,
    package_data={
        "large_typer.static": ["*.html", "*.css", "*.jpg"],
    },
    entry_points={"console_scripts": ["LargeTyper = LargeTyper.__main__:main"]},
    install_requires=[
        "aiofiles==0.5.0",
        "starlette==0.13.4",
        "uvicorn==0.11.5",
        "ujson==2.0.3",
    ],
    extras_require={
        "test": test_dependencies,
        "lint": lint_dependencies,
        "dev": test_dependencies + lint_dependencies
    },
)
