# Assignment 5 Emerging Technology Diffusion Agent
Shenghao Ma | MASY1-GC 1800 | 2026-10-26

The working specialist assesses GenAI diffusion for human-reviewed industrial procurement document assistance. The organization is a hypothetical Siemens Energy-like department, not an assertion about the real company.

## Submission contents
- Working agent: agents/diffusion_agent/specialist_instructions.md and agent_metadata.json
- Agent Record: agents/diffusion_agent/records/agent_record.md
- Five-factor assessment: application_finding in each final response
- Cases and structured outputs: agents/diffusion_agent/cases/ and responses/
- Evidence, failure/revision and handoff: agents/diffusion_agent/records/
- Requirement mapping: REQUIREMENTS_CHECKLIST.md
- Version: submission_version.json and GitHub commit history
- Validation log: work/validation.txt

The required primary artifact is the agent plus Agent Record; the memo does not explicitly require an additional standalone report. The original template is preserved in docs/. Brightspace governs any separate upload format or due date.

## Run without an API key
From the repository root, with Python 3:
```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/diffusion_agent --case agents/diffusion_agent/cases/primary.json
python tools/validate_response.py agents/diffusion_agent/responses/primary_response.json
python agents/diffusion_agent/check_tests.py
```
The saved work/diffusion_agent_*_prompt.txt packets append the dated evidence register. Paste a packet into ChatGPT, review sources, save returned JSON and validate it. Repeat for contrast_1 and contrast_2. Build_prompt creates the base packet; append records/evidence_register.md when rebuilding (the frozen tool intentionally remains unchanged). Structural checks do not verify factual or professional quality.

The original Brightspace ZIP was left unchanged; frozen files in this working copy retain their supplied hashes. Source review and local checks are documented; student review of the proposed independent judgment remains necessary.
