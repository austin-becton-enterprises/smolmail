"""
Tool: ToolLogger
Purpose: Logs tool usage events for debugging and traceability using both JSON format and rotating log file.
"""

import os
import json
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from smolagents.tools import Tool
from app.core.gmail_api import API
class ToolLogger(Tool):
    """
    Logs tool usage in both human-readable format and structured JSON.
    """

    name = "tool_logger"
    description = (
        "Logs tool usage with tool name, inputs, timestamp, and optional outputs or summaries. "
        "Useful for debugging and tracing agent behavior."
    )

    inputs = {
        "tool_name": {
            "type": "string",
            "description": "The name of the tool being logged."
        },
        "inputs": {
            "type": "object",
            "description": "The dictionary of input arguments passed to the tool."
        },
        "output": {
            "type": "string",
            "description": "The output or response from the tool.",
            "default": None,
            "nullable": True
        },
        "summary": {
            "type": "string",
            "description": "A short summary or note about the action.",
            "default": None,
            "nullable": True
        }
    }

    output_type = "string"
    
    def __init__(self):
        super().__init__()
        self.api = API()
        
    def __init__(self):
        super().__init__()
        self.logger = self.setup_logger()

    def setup_logger(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(current_dir, "tool_usage_log.txt")

        logger = logging.getLogger("ToolLogger")
        logger.setLevel(logging.INFO)

        if not logger.handlers:  # Avoid adding multiple handlers
            handler = RotatingFileHandler(log_path, maxBytes=5 * 1024 * 1024, backupCount=3)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger

    def forward(self, tool_name: str, inputs: dict, output: str = None, summary: str = None) -> str:
        timestamp = datetime.utcnow().isoformat()

        log_entry = {
            "timestamp": timestamp,
            "tool_name": tool_name,
            "inputs": inputs,
            "output": output,
            "summary": summary
        }

        # JSON-style log (pretty printed)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(current_dir, "tool_usage_log.txt")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, indent=2) + "\n")

        # Rotating file log
        message = f"Tool: {tool_name} | Inputs: {inputs} | Output: {output} | Summary: {summary}"
        self.logger.info(message)

        return "Log entry created."
