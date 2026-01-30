# Piano di implementazione – Issue #3 (Pipeline schedulata per migliorare le skill)

## Contesto
L’issue #3 richiede una pipeline schedulata che analizzi le skill nel repository e utilizzi Copilot/LLM per proporre miglioramenti o nuove skill, generando output (PR e/o issue) per i maintainer.

## Obiettivo
Definire un’implementazione ripetibile (weekly) via GitHub Actions che:
- Scansiona le skill in `skills/*/SKILL.md`
- Usa un LLM per generare suggerimenti (migliorie + gap analysis)
- Pubblica risultati come PR/issue, secondo regole definite

## Soluzioni possibili (opzioni)

### Soluzione A – PR automatiche con report consolidato (Recommended)
- Workflow schedulato genera un report markdown con suggerimenti per tutte le skill.
- Il report viene committato su branch dedicato e creato un PR unico via `peter-evans/create-pull-request`.
- Pro: review centralizzata, meno rumore; Contro: meno granularità per skill.

### Soluzione B – Issue per skill (granularità massima)
- Workflow schedulato crea/aggiorna issue per ogni skill tramite `actions/github-script`.
- Pro: tracciamento dettagliato; Contro: volume alto di issue.

### Soluzione C – PR per skill (granularità media)
- Per ogni skill, workflow crea branch e PR separato con suggerimenti specifici.
- Pro: PR più piccoli e mirati; Contro: rischio di spam di PR.

## Decisioni richieste
- Frequenza schedulazione: weekly (confermata).
- Output preferito: PR unico con report consolidato (Soluzione A).
- Modello LLM: GitHub Models/Copilot, API key/permessi richiesti.
- Regole di deduplicazione: branch fisso `skill-review-report` + titolo PR fisso; se PR aperto esiste, aggiornarlo invece di crearne uno nuovo.
- Limiti: max 50 skill per run (troncamento; override possibile via workflow_dispatch).

## Workplan

- [x] Definire requisiti operativi dettagliati (frequenza, output, limiti volume)
- [x] Disegnare il workflow GitHub Actions (schedule + workflow_dispatch)
- [x] Implementare step di discovery delle skill (`skills/*/SKILL.md`)
- [x] Implementare step LLM (prompting per review + gap analysis)
- [x] Implementare output:
  - [x] PR unico con report (Soluzione A)
  - [ ] Issue per skill (Soluzione B)
  - [ ] PR per skill (Soluzione C)
- [x] Aggiungere controlli per deduplicazione e rate limiting
- [x] Aggiungere documentazione in README/CONTRIBUTING (processo e limiti)
- [ ] Test manuale tramite `workflow_dispatch`

## Note tecniche
- Workflow aggiunto in `.github/workflows/skill-review-report.yml`.
- Script di generazione report in `scripts/generate_skill_review_report.py`.
- Le skill sono in `skills/<name>/SKILL.md` con frontmatter YAML.
- Per creare PR: usare `peter-evans/create-pull-request`.
- Per creare issue: usare `actions/github-script`.
- Permessi workflow: `contents: write`, `pull-requests: write`.

## Rischi & mitigazioni
- **Spam di PR/issue** → deduplicazione basata su label/branch/issue title.
- **Credenziali LLM** → usare secrets e limitare scope del token.
- **Costi LLM** → limitare numero di skill per run o usare batch.
