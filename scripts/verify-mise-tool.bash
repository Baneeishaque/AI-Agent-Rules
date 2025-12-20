#!/bin/bash
# Verify mise tool installation
# Usage: verify-mise-tool.bash <mise_outcome> <mise_toml_path> <tool_name> [version_command]
# Example: verify-mise-tool.bash "success" "scripts/mise.toml" "python" "python --version"

set -euo pipefail

MISE_OUTCOME="${1:?Error: mise outcome parameter required}"
MISE_TOML="${2:?Error: mise.toml path parameter required}"
TOOL_NAME="${3:?Error: tool name parameter required (e.g., python, java, node)}"
VERSION_COMMAND="${4:?Error: version command parameter required (e.g., python -V)}"

# Check mise installation outcome
if [ "$MISE_OUTCOME" == "failure" ]; then
  echo "::error::mise installation failed."
  exit 1
fi

# Check mise.toml exists
if [ ! -f "$MISE_TOML" ]; then
  echo "::error::Configuration file not found: $MISE_TOML"
  exit 1
fi

# Check tool is defined in mise.toml
if ! grep -q "$TOOL_NAME" "$MISE_TOML"; then
  echo "::error::$TOOL_NAME not defined in $MISE_TOML. Add $TOOL_NAME to [tools] section."
  exit 1
fi

# Get expected version from mise.toml
EXPECTED_VERSION=$(grep "$TOOL_NAME" "$MISE_TOML" | head -1 | sed 's/.*"\([^"]*\)".*/\1/' | tr -d ' ')
if [ -z "$EXPECTED_VERSION" ]; then
  echo "::error::Could not parse $TOOL_NAME version from $MISE_TOML"
  exit 1
fi

# Verify tool is available via mise
TOOL_PATH=$(MISE_CONFIG_FILE="$MISE_TOML" mise which "$TOOL_NAME" 2>/dev/null) || {
  echo "::error::mise cannot find $TOOL_NAME. Run 'mise install' first."
  exit 1
}

# Verify tool is from mise data directory (not system)
MISE_DATA_DIR="${MISE_DATA_DIR:-$HOME/.local/share/mise}"
if [[ ! "$TOOL_PATH" == "$MISE_DATA_DIR"* ]]; then
  echo "::error::$TOOL_NAME path ($TOOL_PATH) is not from mise directory ($MISE_DATA_DIR)."
  exit 1
fi

echo "✓ mise $TOOL_NAME verified: $TOOL_PATH (expected version $EXPECTED_VERSION)"

# Verify version matches expected
ACTUAL_VERSION=$(MISE_CONFIG_FILE="$MISE_TOML" mise exec -- $VERSION_COMMAND 2>&1 | grep -oE '[0-9]+\.[0-9]+(\.[0-9]+)?' | head -1 || echo "unknown")

if [[ ! "$ACTUAL_VERSION" == "$EXPECTED_VERSION"* ]]; then
  echo "::error::$TOOL_NAME version mismatch. Expected $EXPECTED_VERSION.x, got $ACTUAL_VERSION"
  exit 1
fi

echo "✓ $TOOL_NAME version verified: $ACTUAL_VERSION"
