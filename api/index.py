import os
import sys

from mangum import Mangum

# Make the project root importable when running as a Vercel function.
ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(ROOT)
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from backend.app import app as fastapi_app  # noqa: E402

handler = Mangum(fastapi_app)
