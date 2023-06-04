FROM python:3.11.3
ARG YOUR_ENV
COPY . /app
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]