import sys as _sys
import asyncio as _asyncio

import database as _db


if __name__ == "__main__":

    if "--init-models" in _sys.argv:
        if "y" in input("Are you shure? (y/n) ").lower():
            _asyncio.run(_db.services.init_models())

