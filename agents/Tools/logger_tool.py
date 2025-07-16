"""
Tool: ToolLogger
Purpose: Logs tool usage events for debugging and traceability.
"""

import json
import os
from datetime import datetime
from smolagents.tools import Tool

class ToolLogger(Tool):
    """
    Logs which tools were used, with inputs, timestamps, and optionally outputs.
    For now, logs are saved to a local 'tool_usage_log.txt' file in the same folder as the script.
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

    def forward(self, tool_name: str, inputs: dict, output: str = None, summary: str = None) -> str:
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "tool_name": tool_name,
            "inputs": inputs,
            "output": output,
            "summary": summary
        }

        # Ensure the log file is saved in the same directory as this script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(current_dir, "tool_usage_log.txt")

        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, indent=2) + "\n")

        return "Log entry created."
