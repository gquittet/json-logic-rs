from setuptools import setup
from setuptools_rust import Binding, RustExtension


setup(
    name="jsonlogic-rs",
    version="1.0",
    rust_extensions=[
        RustExtension(
            # Python package name before the dot, name of C extension to
            # stick inside of it after the dot.
            "jsonlogic_rs.jsonlogic_rs",
            "../Cargo.toml",
            features=["python"],
            binding=Binding.RustCPython,
        )
    ],
    packages=["jsonlogic_rs"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
