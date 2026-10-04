# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `rsconstruct.toml` - `tera.templates/.github/dependabot.yml.tera` exists but there is no `[processor.tera]` section, so it is never rendered; `.github/dependabot.yml` has already drifted from it (no blank line between the `github-actions` and `pip` entries that the template emits). Add `[analyzer.tera]` + `[processor.tera]` (with `config/personal.lua` and `config/version.lua`) as in the other fleet repos and let it regenerate the file.
- `README.md:1` - hand-written two-line README instead of the fleet's generated one from the shared `tera.templates/README.md.tera`; adopt the shared template and put the repo-specific text (what each `yaml/*.yaml` demonstrates, that the build converts them to `out/*.json`) in `tera.snippets/main.md.tera`.

## Low

- `pyproject.toml:12` - `pytest` is declared in the dev group but the repo has no tests and no pytest processor; drop it, or add a test for `scripts/yaml_to_json.py`.
- `rsconstruct.toml:33` - orphaned comment "The Python yq (a jq wrapper) so CI can run the conversion." left behind with no setting under it; delete it or move it next to the `yq` dependency in `pyproject.toml`.
- `yaml/array.yaml:12` - typo in URL `http://ww.ted.com` (should be `www.ted.com`).
- `yaml/paragraphs.yaml:2-3` - typos in the demo comment: "exapmle" -> "example", "striped" -> "stripped".
- `README.md:2` vs `config/project.lua:3` - the two descriptions differ ("Demos that show how to work with YAML files" vs "Demos for the yaml language"); generating the README from the template fixes this.
