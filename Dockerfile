FROM python:3.11

WORKDIR /code

# Copy requirements.txt
COPY requirements.txt /code/requirements.txt

# Install the specified packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy function code. This copies EVERYTHING inside the app folder to the lambda root.
COPY ./ /code/lpay

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
# Since we copied 
CMD ["uvicorn", "lpay.main:app", "--host", "0.0.0.0", "--port", "8000"]