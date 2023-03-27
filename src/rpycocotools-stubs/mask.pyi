import numpy as np
import numpy.typing as npt

from .anns import EncodedRle, Polygons, PolygonsRS, Rle

def decode_rle(encoded_mask: Rle) -> npt.NDArray[np.uint8]: ...
def decode_encoded_rle(encoded_mask: EncodedRle) -> npt.NDArray[np.uint8]: ...
def decode_poly_rs(encoded_mask: PolygonsRS) -> npt.NDArray[np.uint8]: ...
def decode_poly(poly: Polygons, width: int, height: int) -> npt.NDArray[np.uint8]: ...
