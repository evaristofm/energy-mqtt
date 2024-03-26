FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR .

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements
RUN pip install --no-cache-dir --upgrade -r /requirements/development.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000", "--reload"]