#!/bin/bash
if [[ $ENVIRONMENT == "development" ]]; then
    echo "Installing development dependencies..."
    poetry install -vvv --without mac
    echo "Installing development dependencies... Done!"
else
    echo "Installing production dependencies..."
    poetry install -vvv --without mac --without dev
    echo "Installing production dependencies... Done!"
fi
