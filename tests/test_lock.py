import httpx
import pytest
import asyncio

@pytest.mark.asyncio
@pytest.mark.parametrize("threading_mode", ["runtime", "workers"])
@pytest.mark.parametrize("server_mode", ["wsgi", "asgi", "rsgi"])
async def test_lock(wsgi_server, asgi_server, rsgi_server, threading_mode, server_mode):
    server = {"wsgi": wsgi_server,
              "asgi": asgi_server,
              "rsgi": rsgi_server,
              }[server_mode]
    async with server(threading_mode, workers=2) as port:

        async def make_req(x):
            async with httpx.AsyncClient() as client:
                return await client.post(f"http://127.0.0.1:{port}/echo", content=f"{x}")

        for iteration in range(100):
            ok = 0
            timeout = 0
            out = tuple()
            for res in await asyncio.gather(*[make_req(x) for x in range(3)], return_exceptions=True):
                if isinstance(res, Exception):
                    out += ("timeout",)
                else:
                    assert res.status_code == 200
                    out += (res.text,)
            out += (iteration,)
            assert out == ("0", "1", "2", iteration)
