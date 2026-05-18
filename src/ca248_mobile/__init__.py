"""
CA-248 Mobile: 248维范畴注意力模型的移动端优化版本

版本: v0.1.0
作者: 沐小卯
许可证: Apache 2.0
"""

__version__ = "0.1.0"
__author__ = "沐小卯"
__email__ = "ca248@openclaw.ai"
__license__ = "Apache 2.0"
__copyright__ = "Copyright 2026 沐小卯"

from .model import CA248Mobile
from .config import CA248Config
from .utils import load_model, save_model
from .inference import chat, analyze_text, reason

__all__ = [
    "CA248Mobile",
    "CA248Config", 
    "load_model",
    "save_model",
    "chat",
    "analyze_text",
    "reason",
]