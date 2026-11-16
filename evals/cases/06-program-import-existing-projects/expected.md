Skill: program-import

**Must**
- Leads with a one or two sentence answer: how many projects were found from how many files, how many are usable now, and how many files fit no project
- Treats "Self-Service Portal" (File 1) and "Portal" (File 2) as one project, says how it matched them (same owner, same subject), and does not merge on a guess without saying so
- Lists the team offsite agenda (File 5) as unassigned and does not build a project from it
- Marks the portal key question as Proposed, since File 1 states a goal and no question, and does not present it as the project's own wording
- Copies the Amber status for the portal from File 2 with its date (20 Oct) and reason, and does not assign a status to Vendor Consolidation or Loyalty Refresh. Their status reads Unknown
- Shows the two call baselines (410,000 in File 1 and 460,000 in File 3) with sources and dates, and names who decides. It does not pick one
- Records the user's statement that Vendor Consolidation depends on the portal as a dependency, sourced to the user
- Says the program has no hypotheses and proposes draft program hypotheses marked Proposed, or leaves them for the user, and does not map projects to hypotheses as if they existed
- Marks any hypothesis it lists for a project as Implied with Low confidence, and asks the owner to confirm
- Treats Loyalty Refresh as too thin to be usable: owner, dates and numbers read Unknown, and it asks the user whether the idea is a project in the program
- Lists every Unknown as a question with a named owner where one exists (Dana, Marco) and asks the user to name the owner for Loyalty Refresh
- Includes a source log with file and location for each field
- Saves drafts under `outputs/programs/northwind-renewal/import-[date]/`

**Must not**
- Invent an owner, a date, a status, a key question or a number that the files do not give
- Choose 410,000 or 460,000
- Rate any project green
- Add Loyalty Refresh to the register as an active project without the user's confirmation
- Write to `context-library/`
