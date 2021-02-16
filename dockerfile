FROM python:3.8-slim-buster AS base

RUN mkdir /app

WORKDIR /app

RUN pip3 install poetry 

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

FROM base as development
EXPOSE 5000
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]


FROM base as production
EXPOSE 8000
CMD ["gunicorn", "app:app"]