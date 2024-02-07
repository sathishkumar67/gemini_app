import io
from PIL import Image


def image_to_binary(image):
    with io.BytesIO() as buffer:
        image.save(buffer, format="PNG")
        return buffer.getvalue()
