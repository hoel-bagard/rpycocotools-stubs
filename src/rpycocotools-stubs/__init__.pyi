__version__ = "0.0.1"

from typing_extensions import Self

class Category:
    id: int
    name: str
    supercategory: str

    def __init__(self: Self, id: int, name: str, supercategory: str) -> None: ...

class COCO:
    # anns: dict[int, Annotation]
    # dataset: Dataset
    cats: dict[int, Category]
    # imgs: dict[int, Image]
    # imgToAnns: dict[int, list[Annotation]]

    def __init__(self: Self, annotation_path: str, image_folder_path: str) -> None: ...
    def visualize_img(self: Self, img_id: int) -> None: ...
