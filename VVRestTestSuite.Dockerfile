FROM python:3.13.2
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y python3-distutils python3-pip && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements-dev.txt
RUN sed -i 's/\r$//' /app/vvrest_test_suite.sh && chmod +x /app/vvrest_test_suite.sh
CMD ["bash", "vvrest_test_suite.sh"]