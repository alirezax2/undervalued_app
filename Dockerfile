FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

EXPOSE 7860

# CMD ["panel", "serve", "/app/main.py", "--address", "0.0.0.0", "--port", "7860", "--allow-websocket-origin", "sophiamyang-panel-example.hf.space"]
CMD ["panel", "serve", "/app/main.py", "--port", "7860"]