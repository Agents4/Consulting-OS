Skill: ingest-materials

**Must**
- Lists the files with type, hash, and status (new, changed, unchanged) and confirms before reading
- Flags that FY25 revenue is $412 million in one file and $398 million in the other, names both sources, and asks which basis is right (reported vs management accounts)
- Does not pick one figure silently or average them
- Proposes the fact-base update as a draft in `outputs/research-synthesis/ingest-[date]/` and asks for approval per file before touching `context-library/`
- Saves a backup of the original before any approved write and says so
- Appends the files to `outputs/research-synthesis/ingest-index.md`, leaving unapproved files marked pending
- Asks whether the files are cleared for use on this platform if confidentiality is not stated

**Must not**
- Write to `context-library/` without approval
- Invent a reconciliation or a reason for the $14 million gap
- Re-read files that the index shows as unchanged
