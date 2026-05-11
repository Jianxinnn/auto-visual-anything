# Evidence Discipline

Single source for evidence, assumptions, unknowns, conflicts, and metrics across
`visual-plan`.

## Rules

1. Concrete claims must trace to a file, paper section, image region, command, or user text.
2. Unsupported facts become `unknown`, assumptions, qualitative labels, or omitted panels.
3. Keep evidence and visualization assumptions separate.
4. Surface conflicts; do not smooth them into one confident claim.
5. Hedges such as "likely", "typical", "approximately", or "probably" do not make an
   unsupported fact acceptable.

## Ledger

Every sub-skill writes a compact ledger before rendering:

```text
EVIDENCE:
  Sources inspected: [...]
  Concrete facts observed: [...]
  Numbers measured: [number -> source command/file]

ASSUMPTIONS:
  [visual/design choices not stated by the source]

UNKNOWNS:
  [important missing details]
```

For hybrid inputs, tag content with `[FROM CODE]`, `[FROM PAPER]`, `[FROM DIAGRAM]`,
`[FROM TEXT]`, `[SYNTHESIZED]`, or `[UNKNOWN]`.

## Metrics

A number may appear in the final output only if it is in the ledger with a source pointer.
This includes file counts, dependency counts, model scores, deltas, latency, citations,
dataset sizes, and parameter counts.

If not measured or visible, omit the stat panel or use a qualitative label. Do not
back-fill from common knowledge.

## Stop Signals

Stop and correct the plan when you are about to:

- invent a number because it "probably exists"
- add a module for symmetry
- convert an import or visual hint into an untagged fact
- hide missing evidence behind placeholders
- draw charts with unsourced axes or values

Use literal `[TODO: source]` only when the user explicitly wants a draft that marks missing
evidence; never use fake final values.

## Footer

Every renderer includes sources, confidence/coverage, and material unknowns or assumptions.
For design requests with no source artifact, state `design assumptions` explicitly.
