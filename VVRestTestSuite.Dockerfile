FROM python:3.13.2
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements-dev.txt
CMD ["bash", "vvrest_test_suite.sh"]