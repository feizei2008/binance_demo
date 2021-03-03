import logging
import sys
from pathlib import Path


logger = logging.getLogger("stock-data-processor")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    fmt="%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s",
    datefmt="%Y-%m-%d  %H:%M:%S"
)
log_path = Path(__file__).parent.parent.joinpath("stock-data-processor.log").resolve()

file_handler = logging.FileHandler(log_path, encoding='utf-8')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
