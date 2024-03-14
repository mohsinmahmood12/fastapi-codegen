#!/bin/bash

# Ensure script is executed with bash
if [ -z "$BASH_VERSION" ]; then
    exec /bin/bash "$0" "$@"
fi

# Stop on the first sign of trouble
set -e

echo "Checking for required environment variables..."
if [ -z "${OPENAI_API_KEY}" ]; then
    echo "The OPENAI_API_KEY environment variable is not set. Please set it and rerun this script."
    exit 1
fi

if [ -z "${REDIS_URL}" ]; then
    echo "The REDIS_URL environment variable is not set. Defaulting to redis://redis:6379"
    export REDIS_URL="redis://redis:6379"
fi

echo "Environment variables look good."

echo "Starting Docker containers..."
docker-compose up -d

echo "The server should now be running on http://localhost:8000"
