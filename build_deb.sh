#!/bin/bash

# Oraset Debian Package Builder
# This script packages Oraset into a .deb file for Debian/Ubuntu

set -e

PACKAGE_NAME="oraset"
VERSION="1.0.0"
ARCH="all"
MAINTAINER="Oraset Developer"
DESCRIPTION="A simple cross-platform programming language"
LICENSE="GPL-3.0"

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

# Build directory
BUILD_DIR="orasetdeb"
PACKAGE_DIR="${BUILD_DIR}/${PACKAGE_NAME}_${VERSION}_${ARCH}"

echo "=== Oraset Debian Package Builder ==="
echo ""

# Clean previous build
echo "[1/6] Cleaning previous build..."
rm -rf ${BUILD_DIR}
mkdir -p ${PACKAGE_DIR}

# Install PyInstaller if not present
echo "[2/6] Checking PyInstaller..."
if ! command -v pyinstaller &> /dev/null; then
    echo "Installing PyInstaller..."
    pip install --break-system-packages pyinstaller
fi

# Create binary with PyInstaller
echo "[3/6] Building binary with PyInstaller..."
pyinstaller --onefile --name oraset oraset.py

# Copy binary to package directory
echo "[4/6] Copying files..."
mkdir -p ${PACKAGE_DIR}/usr/bin
cp dist/oraset ${PACKAGE_DIR}/usr/bin/

# Create DEBIAN directory and control file
echo "[5/6] Creating package metadata..."
mkdir -p ${PACKAGE_DIR}/DEBIAN

cat > ${PACKAGE_DIR}/DEBIAN/control << EOF
Package: ${PACKAGE_NAME}
Version: ${VERSION}
Section: interpreters
Priority: optional
Architecture: ${ARCH}
Depends: python3
Maintainer: ${MAINTAINER}
Description: ${DESCRIPTION}
 A simple cross-platform programming language written in Python.
 Supports Windows and Linux, with features like variables,
 functions, classes, conditional statements, loops, and more.
EOF

# Create copyright file
mkdir -p ${PACKAGE_DIR}/usr/share/doc/${PACKAGE_NAME}
cat > ${PACKAGE_DIR}/usr/share/doc/${PACKAGE_NAME}/copyright << EOF
Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: ${PACKAGE_NAME}
Upstream-Contact: ${MAINTAINER}
Source: https://github.com/oraset/oraset

Files: *
Copyright: ${LICENSE}
License: GPL-3.0
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License.
 .
 On a Debian system, you can find the complete text of the GPL-3.0
 license in /usr/share/common-licenses/GPL-3.
EOF

# Build the .deb package
echo "[6/6] Building .deb package..."
dpkg-deb --build ${PACKAGE_DIR}

# Move package to current directory
mv ${PACKAGE_DIR}.deb ${BUILD_DIR}/

# Clean up PyInstaller build files
rm -rf build dist

echo ""
echo "=== Build Complete ==="
echo "Package created: ${BUILD_DIR}/${PACKAGE_NAME}_${VERSION}_${ARCH}.deb"
echo ""
echo "To install the package, run:"
echo "  sudo dpkg -i ${BUILD_DIR}/${PACKAGE_NAME}_${VERSION}_${ARCH}.deb"
echo ""
echo "To uninstall the package, run:"
echo "  sudo dpkg -r ${PACKAGE_NAME}"
