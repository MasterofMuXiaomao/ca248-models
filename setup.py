from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ca248-mobile",
    version="0.1.0",
    author="沐小卯",
    author_email="ca248@openclaw.ai",
    description="CA-248: 248维范畴注意力模型的移动端优化版本",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openclaw/ca248-models",
    project_urls={
        "Bug Tracker": "https://github.com/openclaw/ca248-models/issues",
        "Documentation": "https://github.com/openclaw/ca248-models/docs",
        "Source Code": "https://github.com/openclaw/ca248-models",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "numpy>=1.21.0",
        "transformers>=4.30.0",
        "sentencepiece>=0.1.99",
        "accelerate>=0.20.0",
        "huggingface-hub>=0.16.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
        ],
        "mobile": [
            "onnxruntime>=1.15.0",
            "coremltools>=7.0.0",
        ],
        "quantization": [
            "torchao>=0.1.0",
            "bitsandbytes>=0.41.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ca248-chat=ca248_mobile.cli:chat_cli",
            "ca248-benchmark=ca248_mobile.cli:benchmark_cli",
            "ca248-convert=ca248_mobile.cli:convert_cli",
        ],
    },
    include_package_data=True,
    package_data={
        "ca248_mobile": [
            "models/*.bin",
            "models/*.json",
            "models/*.txt",
            "configs/*.json",
            "vocabs/*.bin",
        ],
    },
)