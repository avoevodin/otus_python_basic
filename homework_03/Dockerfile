# start container as a daemon:
#docker run -d --name homework03-otus \
#        --hostname homework03-otus \
#        -p 8000:8000 \
#        homework03-otus-python-basic
#-----------------------------------------
# start container in an interactive mode:
#docker run -it --name homework03-otus \
#        --hostname homework03-otus \
#        -p 8000:8000 \
#        homework03-otus-python-basic


FROM python:3.9-buster

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY fastapi_proj .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
