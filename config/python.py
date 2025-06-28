""" python deps for this project """

install_requires: list[str] = [
    "yq",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
]
requires = install_requires + build_requires
