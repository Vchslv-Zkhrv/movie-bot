import asyncio as _asyncio
import sys as _sys
import typing as _t

import api as _api
import config as _cfg
import database as _db


def main():
    api = _t.cast(
        _api.abstract.Api, _cfg.api_container.resolve(_api.abstract.Api)
    )
    print(api)


if __name__ == "__main__":
    if "--init-models" in _sys.argv or "-M" in _sys.argv:
        if "y" in input("Are you shure? (y/n) ").lower():
            _asyncio.run(_db.services.init_models())
    else:
        main()
