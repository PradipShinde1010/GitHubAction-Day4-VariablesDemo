import os
env_name = os.getenv("ENV_NAME", "not-set")
print(f"ENV_NAME from Python app = {env_name}")