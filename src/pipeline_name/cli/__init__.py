from pathlib import Path

from snk_cli import CLI

workflow_path = Path(__file__).parent.parent

pipeline_name = CLI(workflow_path)
