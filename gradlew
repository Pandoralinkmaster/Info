#!/bin/sh
# Pandora Gradle Wrapper – fixed
# Funktioniert ohne gradle-wrapper.jar und nutzt curl, wget, busybox wget oder python.

set -e

GRADLE_VERSION="8.4"
GRADLE_DIST_URL="https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"
INSTALL_DIR="${HOME}/.gradle/wrapper/dists/gradle-${GRADLE_VERSION}-bin"
ZIP="${INSTALL_DIR}/gradle-${GRADLE_VERSION}-bin.zip"
GRADLE_BIN="${INSTALL_DIR}/gradle-${GRADLE_VERSION}/bin/gradle"

if [ ! -x "$GRADLE_BIN" ]; then
    echo ">>> Lade Gradle ${GRADLE_VERSION} herunter..."
    mkdir -p "$INSTALL_DIR"
    rm -f "$ZIP"

    if command -v curl >/dev/null 2>&1; then
        curl -L --progress-bar "$GRADLE_DIST_URL" -o "$ZIP"
    elif command -v wget >/dev/null 2>&1; then
        wget -q --show-progress "$GRADLE_DIST_URL" -O "$ZIP"
    elif command -v busybox >/dev/null 2>&1; then
        busybox wget "$GRADLE_DIST_URL" -O "$ZIP"
    elif command -v python3 >/dev/null 2>&1; then
        python3 -c "import urllib.request; urllib.request.urlretrieve('$GRADLE_DIST_URL', '$ZIP')"
    elif command -v python >/dev/null 2>&1; then
        python -c "import urllib.request; urllib.request.urlretrieve('$GRADLE_DIST_URL', '$ZIP')"
    else
        echo "FEHLER: curl, wget, busybox oder python fehlt." >&2
        exit 1
    fi

    echo ">>> Entpacke Gradle..."
    unzip -oq "$ZIP" -d "$INSTALL_DIR"
    rm -f "$ZIP"
    echo ">>> Gradle ${GRADLE_VERSION} bereit."
fi

exec "$GRADLE_BIN" "$@"
