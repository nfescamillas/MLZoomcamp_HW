FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install -U pip
RUN pip install pipenv 

WORKDIR  /app

COPY ["Pipfile", "Pipfile.lock","./"]

RUN pipenv install --system --deploy --ignore-pipfile

COPY ["predict.py","model1.bin","dv.bin", "./"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696","predict:app"]