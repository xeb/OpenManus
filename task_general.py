import argparse
import asyncio

from app.agent.manus import Manus
from app.logger import logger

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run the General Agent")
    parser.add_argument(
        "--prompt",
        default="Tell me I'm pretty and terminate",
        required=True,
        help="What is the prompt given to the agent?",
    )   
    return parser.parse_args()

async def main():
    agent = Manus()
    args = parse_args()

    try:
        logger.warning("Processing your request...")
        logger.warning(f"{args.prompt}")
        await agent.run(args.prompt)
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")


if __name__ == "__main__":
    asyncio.run(main())
