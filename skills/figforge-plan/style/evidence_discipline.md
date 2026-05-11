# Evidence Discipline — figforge-plan

Single source of truth for evidence, assumption, and unknown handling across every
sub-skill and renderer. All sub-skills inherit these rules; do not redefine them locally.

---

## CORE RULES

1. **Source > inference.** Every concrete claim must be traceable to a file path,
   paper section, image region, or user-provided text.
2. **Mark uncertainty explicitly.** Use `unknown`, omit the panel, or use a qualitative
   label (`compact repo`, `small benchmark`) rather than a fabricated number.
3. **Separate evidence from assumption** in every content block. Assumptions are
   visualization choices, not facts.
4. **Conflicts stay visible.** When sources disagree, surface the disagreement; do not
   smooth it into a single confident claim.
5. **Spirit, not just letter.** "Approximately", "likely", and "typical" are
   fabrication wearing a hedge. Either source it or omit it.

---

## EVIDENCE LEDGER

Every sub-skill produces a ledger before compiling output. Use this shape:

```
EVIDENCE:
  Sources inspected: [file paths / paper sections / image regions]
  Concrete facts directly observed: [list]
  Numbers measured by command/tool: [number → source command or file]

ASSUMPTIONS:
  [visualization choices not stated by the source]

UNKNOWNS:
  [important details not visible in the source]
```

For HYBRID inputs, tag every content item with origin:
`[FROM CODE]`, `[FROM PAPER]`, `[FROM DIAGRAM]`, `[FROM TEXT]`,
`[SYNTHESIZED]`, `[UNKNOWN]`.

---

## METRIC DISCIPLINE

A number is allowed in the final output only if it appears in the evidence ledger
with a source pointer. This applies to:

- File counts, line counts, dependency counts
- Latency, throughput, accuracy, precision, recall, F1
- Improvement deltas, baseline scores, ablation values
- Author counts, citation counts, dataset sizes, parameter counts

If a metric was not measured, **omit the stat panel**. Do not back-fill from common
knowledge or "typical values".

---

## RED FLAGS — STOP if you catch yourself thinking:

| Rationalization | Reality |
|-----------------|---------|
| "This number probably exists in the source." | If you cannot quote the source, it does not exist for this figure. |
| "Marking unknown looks ugly." | An ugly honest figure beats a beautiful false one. Omit the panel. |
| "User wants polish; rough estimates are fine." | Estimates labeled as facts are fabrication. Use qualitative labels. |
| "This dependency is so common it must be present." | Common ≠ verified. Omit unless evidenced. |
| "The paper probably reports ~X% improvement." | "Probably" = unknown. Do not insert. |
| "I'll round it and label it approximate." | Approximate of what? Rounding hides invention. |
| "It's just a placeholder; the user can fix it later." | Placeholders inside polished figures get shipped. Use `[TODO: source]` as a literal label, never as a fake number. |
| "The diagram needs symmetry, so I'll add one more module." | Visual balance is not evidence. Group or whitespace; don't invent. |
| "Inferring this from imports is reasonable." | Reasonable inference is still inference. Tag it `[INFERRED]`, not as fact. |

Each is a Truthfulness Contract violation. Mark `unknown`, omit, or label as
assumption/inference.

---

## STAT PANEL CHECK

Before compiling any stat panel:

- [ ] Each number maps to a ledger entry with a source pointer.
- [ ] Each number's unit and context is unambiguous.
- [ ] Qualitative labels are used wherever no exact value was measured.
- [ ] No number is back-filled from "common knowledge" or "typical values".
- [ ] The panel can be removed without breaking the figure's argument.

If any check fails, drop or qualify the panel rather than ship false certainty.

---

## SOURCE DISCIPLINE FOOTER

Every renderer footer must state at least:

- Sources used (file paths / citations / image references)
- Confidence level (high / medium / low) or coverage note
- Listed unknowns or assumptions that materially affect the figure

If no source artifact exists (e.g., DESIGN_REQUEST), the footer must state
"design assumptions" explicitly so readers do not mistake them for analyzed facts.
