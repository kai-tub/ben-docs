# Dependencies

## Python (Poetry) Dependencies

### Documentation dependencies

```{literalinclude} ../../pyproject.toml
---
language: toml
start-after: docs-deps-start
end-before: docs-deps-end
---
```

### Linting dependencies

```{literalinclude} ../../pyproject.toml
---
language: toml
start-after: lint-deps-start
end-before: lint-deps-end
---
```

## Nix Dependencies

```{literalinclude} ../../devshell.toml
---
language: toml
start-after: nix-deps-start
end-before: nix-deps-end
---
```
