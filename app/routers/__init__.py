from fastapi import FastAPI


def setup_routers(app: FastAPI):
    import app.routers.root as RootRouter
    import app.routers.some as SomeRouter

    RootRouter.generate_routes(app)
    SomeRouter.generate_routes(app)
