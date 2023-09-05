class Python:
    def __init__(self) -> None:
        self.is_cool = True


class FastAPI(Python):
    pass


fast_api = FastAPI()

print(fast_api.is_cool)
print(FastAPI.__mro__)