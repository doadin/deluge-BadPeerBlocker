from setuptools import setup

setup(
    name="BadPeerBlocker",
    version="1.0",
    description="Automatically blocks peers with Unknown client names.",
    author="Doadin",
    packages=["BadPeerBlocker"],
    package_data={
        "BadPeerBlocker": ["*.egg-info"],
    },
    entry_points={
        "deluge.plugin.core": [
            "BadPeerBlocker = BadPeerBlocker:CorePlugin"
        ]
    },
)