from typing import Sequence, Optional

from large_typer.restapi import app


def main(*argv: Sequence[str]) -> Optional[int]:
    import uvicorn
    return uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    import sys
    sys.exit(main(*sys.argv))
