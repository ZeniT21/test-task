from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import PIL
from PIL import Image, ExifTags, UnidentifiedImageError
import numpy as np
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import io
import json


app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)
templates = Jinja2Templates(directory="templates/")


@app.get("/")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/uploadfile/")
async def image_info(request: Request):

    """Method downloads image and return exif and average rgb

    Raises
    ------
    Exception
    If not file: method return - Can't read file
    ------
    Exception
    If file is not image: method return - Not supported file
    """
    form = await request.form()
    try:
        contents = await form["file"].read()
    except Exception:
        return json.dumps({"Error!": "Can't read file"})

    try:
        image = Image.open(io.BytesIO(contents))
    except PIL.UnidentifiedImageError:
        return json.dumps({"Error!": "Not supported file"})


    dic = GetSizeImg(image)
    GetAvgRgb(image, dic)
    try:
        exif_data = image._getexif()
    except Exception:
        return json.dumps({"Error!": "Not info for this file"})
    if exif_data is not None:
        for key, val in exif_data.items():
            if key in ExifTags.TAGS:
                dic[str(ExifTags.TAGS[key])] = str(val)
    return json.dumps(dic)



def GetAvgRgb(image, dic):
    average_color_row = np.average(image, axis=0)
    average_color = np.average(average_color_row, axis=0).tolist()
    if type(average_color) == list:
        dic['AvarageColor[RGB]'] = ', '.join(map(str, average_color))
    elif type(average_color) == float:
        dic['AvarageColor[RGB]'] = average_color
        return dic
    else:
        return False


def GetSizeImg(image):
    width, height = image.size
    dic = {'Width': width, 'Height': height}
    return dic
