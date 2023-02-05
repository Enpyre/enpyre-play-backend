#!/bin/bash
if [[ $ENVIRONMENT == "development" ]]; then
    echo "Installing development dependencies..."
    poetry install --no-interaction --no-ansi -vvv --without only-prod
    echo "Installing development dependencies... Done!"
else
    echo "Installing production dependencies..."
    poetry install --no-interaction --no-ansi -vvv --without dev
    echo "Installing production dependencies... Done!"
fi
