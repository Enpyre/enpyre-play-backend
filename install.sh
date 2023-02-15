#!/bin/bash
if [[ $ENVIRONMENT == "development" ]]; then
    echo "Installing development dependencies..."
    poetry install --no-interaction --no-ansi -vvv --without only-prod
    echo "Installing development dependencies... Done!"
else
    if [[ $CELERY == "true" ]]; then
        echo "Installing production dependencies..."
        poetry install --no-interaction --no-ansi -vvv --with only-prod --with celery
        echo "Installing production dependencies... Done!"
    else
        echo "Installing production dependencies..."
        poetry install --no-interaction --no-ansi -vvv --with only-prod
        echo "Installing production dependencies... Done!"
    fi
fi
