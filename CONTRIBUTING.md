# Contributing

Contributions should support the research and educational purpose of the project.

## Good contributions

- Documentation improvements.
- New synthetic task scenarios.
- Transparent adaptation-policy variants.
- Evaluation metrics for usability, trust, workload, and autonomy.
- Tests that improve reproducibility.

## Boundary

Do not add code for hidden tracking, biometric inference, real user surveillance, productivity scoring, or clinical mental-state assessment.

## Development

```bash
python -m pip install -e .
python -m pip install -r requirements.txt
pytest
```
