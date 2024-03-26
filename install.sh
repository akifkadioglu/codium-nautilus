#!/bin/bash


# Remove previous version and setup folder
echo "Removing previous version (if found)..."
mkdir -p ~/.local/share/nautilus-python/extensions
rm -f ~/.local/share/nautilus-python/extensions/VSCodiumExtension.py
rm -f ~/.local/share/nautilus-python/extensions/codium-nautilus.py

# Download and install the extension
echo "Downloading newest version..."
wget --show-progress -q -O ~/.local/share/nautilus-python/extensions/codium-nautilus.py https://raw.githubusercontent.com/akifkadioglu/codium-nautilus/master/codium-nautilus.py

# Restart nautilus
echo "Restarting nautilus..."
nautilus -q

echo "Installation Complete"
