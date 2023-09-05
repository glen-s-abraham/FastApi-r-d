from typing import List, Tuple, Dict, Union, Optional

price: List[int] = [12, 23, 4, 5]
price: Tuple[int, int, int] = (1, 2, 5)
price: Dict[str, int] = {"item1": 23, "item2": 45}
# combining multiple datatypes
x: List[Union[int, float]] = [1.2, 4, 5, 6.7]


def inr_to_usd(value: float) -> Union[float, None]:
    try:
        conversion_factor = 80
        value = value / conversion_factor
        return value
    except TypeError:
        return None


inr_to_usd(23)

Image = List[List[int]]


def flatten_image(img: Image) -> List:
    flat_list = []
    for sublist in img:
        for item in sublist:
            flat_list.append(item)
    return flat_list


image = [[1, 2, 3], [4, 5, 6]]
flatten_image(image)


class Job:
    def __init__(self, title: str, description: Optional[str]) -> None:
        self.title = title
        self.description = description

    def __repr__(self) -> str:
        return self.title


job1 = Job(title="Team lead", description="sdks")
job2 = Job(title="Project manager", description="fdfdf")

jobs: List[Job] = [job1, job2]
