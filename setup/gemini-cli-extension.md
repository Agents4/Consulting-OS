# Consulting OS as a Gemini CLI Extension

Install the whole OS into Gemini CLI with one command. You get 55 skills, 56 slash commands, the engagement rules, review personas, frameworks, and model and deck templates. Your engagement files stay in your own folder, one folder per client.

**Tested:** the extension passes `gemini extensions validate` and installs from a local copy on Gemini CLI 0.65.0, and the CLI lists all 53 skills (the first build, before `/ingest-materials`) and the context file. I did not run a live model session (it needs your sign-in), and I did not test the install from GitHub. Try one skill after you install it and tell me what breaks.

## Check your access first

Google replaced Gemini CLI with Antigravity CLI for consumer Google AI Pro, Ultra and free individual users on June 18, 2026. Gemini CLI remains available through paid Gemini API keys and Gemini Code Assist Standard or Enterprise licenses. This extension is built for Gemini CLI. Antigravity CLI says it supports Agent Skills and extensions (called plugins), but Google notes feature parity is not 1:1, so test before you rely on it. If you do not have either, use the Gemini app path in `setup/gemini-setup-guide.md`.

## Install

```
npm install -g @google/gemini-cli          # Node.js 20 or later
gemini extensions install https://github.com/Agents4/Consulting-OS
```

Until the extension branch is merged to main, add `--ref=gemini-cli-extension`. To pin a release later, use a tag such as `--ref=v1.2.0`.

Check it: `gemini extensions list` shows `consulting-os`. Inside `gemini`, `/skills list` shows 55 skills and `/memory show` shows the context file.

Update with `gemini extensions update consulting-os`.

## Set up one client (about 2 minutes)

1. Make a folder for the client. For Google Drive, put it in your synced Drive folder, for example `Consulting Engagements/Clients/[Client]`.
2. Open a terminal in that folder and run `gemini`.
3. Run `/engagement-init`. It creates `context-library/` and `outputs/` with all subfolders and copies the starter templates. It never overwrites an existing file.
4. Fill `context-library/engagement-info-template.md`, especially the key question, scope, gates and approved platforms.
5. Run `/problem-statement`, `/kickoff-plan` or `/day-one-answer`.

Everything the OS writes goes to `outputs/` in that folder. Close the session, open another client's folder, and you are in a different engagement with its own context.

## How it works

| Piece | Where it lives |
|---|---|
| Rules, voice, skill list, path map | `GEMINI.md` in the extension. Loaded every session |
| 55 skills | `skills/<name>/SKILL.md`. Gemini activates one when a task matches |
| 56 slash commands | `commands/<name>.toml`. `/issue-tree` activates the issue-tree skill. `/engagement-init` runs the setup script |
| Frameworks, engagement model, templates, review personas | The extension folder, `~/.gemini/extensions/consulting-os/`. Read-only |
| Client context and outputs | Your client folder: `context-library/` and `outputs/` |

Skills and `GEMINI.md` already point to the right places. Core files use absolute extension paths, and engagement files use the current folder.

## Differences from the Claude Code version

- Skills activate by task match or by slash command. Gemini asks you to confirm before it loads a skill.
- `/connect-mcps` and `/google-workspace-output` are not included. They depend on Claude's connectors. To add live tools, install an extension such as Google Workspace: `gemini extensions install https://github.com/gemini-cli-extensions/workspace`. Its Docs tools can create and edit, Drive has no upload tool, and Sheets and Slides are read-only.
- For Google Sheets or Slides, build .xlsx and .pptx in `outputs/`, then upload to Drive and open with Sheets or Slides.
- `/review-panel` reads the persona files in the extension. It does not run parallel sub-agents.
- Not tested yet: the Windows shell. `/engagement-init` uses bash. On Windows use WSL.

## Rebuild after you change a skill

The extension files are generated from `.claude/skills/` and `CLAUDE.md`. After you edit either:

```
python3 gemini/tools/build_extension.py
```

Then raise `VERSION` in that script, commit, and tag. Edit the skills in `.claude/skills/`, not in `skills/`.

If you develop with `gemini extensions link`, note that a linked extension keeps only a pointer in `~/.gemini/extensions/consulting-os/`, so the absolute core paths in `GEMINI.md` and the skills do not resolve. Use `gemini extensions install <local path>` to test instead.

## Publish to the gallery (optional)

1. The repo must be public, and `gemini-extension.json` must be at its root. Both are true for `Agents4/Consulting-OS` once this branch is merged.
2. Add the GitHub topic `gemini-cli-extension`.
3. Tag a release that matches the manifest version, for example `v1.2.0`.
4. Google's crawler checks tagged repos daily and lists those that pass validation.

The repo holds no client data. Keep it that way: never commit `context-library/data/` or `client-materials/` from a real engagement (the `.gitignore` already excludes them).

## Sources

- [Build Gemini CLI extensions](https://geminicli.com/docs/extensions/writing-extensions/)
- [Extension reference](https://geminicli.com/docs/extensions/reference/)
- [Releasing an extension](https://geminicli.com/docs/extensions/releasing/)
- [Gemini CLI extensions](https://geminicli.com/docs/extensions/)
- [Custom commands](https://geminicli.com/docs/cli/custom-commands/)
- [Agent Skills](https://geminicli.com/docs/cli/skills/)
- [GEMINI.md context files](https://geminicli.com/docs/cli/gemini-md/)
- [Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/en/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
