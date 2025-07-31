import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Set up log directory
        log_dir = os.path.join(os.getcwd(), "Logs")
        os.makedirs(log_dir, exist_ok=True)

        # Create full log path
        log_path = os.path.join(log_dir, "automation.log")

        # Clear any existing logging handlers to ensure basicConfig works
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        # Configure logging
        logging.basicConfig(
            filename=log_path,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.INFO
        )

        # Create named logger
        logger = logging.getLogger("automationLogger")

        # Log test message to verify setup
        logger.info("Logger initialized and writing to automation.log.")

        return logger
