#!/bin/bash


# Install required Python packages
echo "Installing required Python packages..."
pip install transformers scipy
pip install python-dotenv
pip install llama_parse
pip install llama_index.core
pip install llama-index-readers-file
pip install torch

# Confirm completion
echo "Setup complete. All required packages have been installed."
