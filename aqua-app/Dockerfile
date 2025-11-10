FROM python:3

EXPOSE 8080
WORKDIR /app

COPY . ./
COPY .streamlit/secrets.toml /home/app/.streamlit/secrets.toml

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "aqua_app.py", "--server.port=8080", "--server.address=0.0.0.0"]