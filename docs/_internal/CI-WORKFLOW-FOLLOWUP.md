# CI follow-up — needs `workflow` scope

Local PAT cannot push `.github/workflows/*`. Apply this to `validate.yml` when auth has **workflow** scope:

1. After `Run validator`, add:

```yaml
      - name: Lab pytest (synthetic scenarios A–C)
        run: |
          python3 -m pip install -q pytest
          cd lab && PYTHONPATH=. python3 -m pytest -q
```

2. In Data freshness, add:

```yaml
          test -d lab && test -d docs/50-evidence
```

Then: `gh auth refresh -h github.com -s repo,workflow` → commit → push.
