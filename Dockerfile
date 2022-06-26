FROM python:3.9

#
RUN mkdir /test1

WORKDIR /test1

#
COPY ./requirements.txt /test1/requirements.txt

#
RUN pip install  -r requirements.txt

#
COPY static/script.js /test1/static/script.js
COPY static/style.css /test1/static/style.css
COPY templates/form.html /test1/templates/form.html
COPY main.py /test1/main.py
#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]