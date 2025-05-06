FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy only the files necessary for installing dependencies
# This leverages Docker's layer caching. If these files don't change,
# Docker won't re-run poetry install in subsequent builds.
COPY pyproject.toml poetry.lock* ./

# Install project dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 