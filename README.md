# exo-cloud-json
## the How
1. The filename is first parsed by Regex for a valid extension.
2. It is then parsed trough Pythons JSON decoder (`json.load`).
3. All string data within the `text` markers are forwarded to the Azure Translator API.
4. The now translated markers will now be used to overwrite the previous values of any `text` markers, before the json is re-encoded (`json.dump`) and written under `[json-name].[ISO 639-2-T language code of document].json` .