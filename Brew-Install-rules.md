# Brew: Prefer Head/Source Builds Over Binaries

User prefers to install the latest head version/source version (if head not found) of formula/cask using brew, ensuring it is not the binary version. Use https://formulae.brew.sh/formula/X, https://github.com/Homebrew/homebrew-core/blob/*/Formula/*/X.rb (will get actual url from first URL) & https://formulae.brew.sh/api/formula/X.json URLs for more details. Similarly https://formulae.brew.sh/cask/X, https://github.com/Homebrew/homebrew-cask/blob/*/Casks/*/X.rb & https://formulae.brew.sh/api/cask/X.json in the case of Casks. Since the build from source is multi step process, ensure maximum logging from brew.

**Reference URLs for Research:**
- Formulas: https://formulae.brew.sh/formula/{package-name}
- Formula Source: https://github.com/Homebrew/homebrew-core/blob/*/Formula/*/{package-name}.rb
- Formula API: https://formulae.brew.sh/api/formula/{package-name}.json
- Casks: https://formulae.brew.sh/cask/{package-name}
- Cask Source: https://github.com/Homebrew/homebrew-cask/blob/*/Casks/*/{package-name}.rb
- Cask API: https://formulae.brew.sh/api/cask/{package-name}.json

**Installation Priority:**
1. Head version (if available): brew install --HEAD {package-name}
2. Source build (if head not available): brew install --build-from-source {package-name}
3. Always use verbose logging: --verbose flag
