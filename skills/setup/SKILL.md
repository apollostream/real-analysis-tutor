---
name: setup
description: Environment doctor and guided Lean 4 + Mathlib install. Use when the learner accepts Lean setup, reports Lean/lake errors, or asks about their environment.
argument-hint: "[doctor|install]"
---

Use this skill whenever the learner accepts an offer to set up Lean, reports a Lean/lake error, or asks about their environment. The learner never reads documentation — you narrate every step in plain language and explain, in a sentence or two, why each step matters before you run it. Default to `doctor` when called with no argument and Lean already looks partially set up; default to `install` when nothing is set up yet.

## Platform detection (do this first, always)

Run:

```
uname -s
grep -qi microsoft /proc/version && echo "WSL2"
```

- `uname -s` returns `Linux` and `/proc/version` mentions "microsoft" → **WSL 2**. Proceed normally; every command below runs as-is.
- `uname -s` returns `Linux` and `/proc/version` does not mention Microsoft → **native Linux**. Proceed normally.
- `uname -s` returns `Darwin` → **macOS**. Use `brew` instead of `apt` in Step 1 of install mode; everything else is the same.
- `uname -s` fails, or returns something like `MINGW64_NT` / `CYGWIN`, or there is no `/proc/version` at all → you are running in a **native Windows** shell (Git Bash or similar), not WSL 2. Stop here and go to the **Windows-native branch** below instead of doctor/install mode.

## Execution policy (applies to every step below)

- Run safe, read-only checks yourself, no confirmation needed: version checks (`git --version`, `elan --version`, etc.), listing extensions, checking whether files or directories exist.
- Run workspace-local `lake` commands yourself, no confirmation needed: anything scoped to the learner's Lean project directory (`lake update`, `lake exe cache get`, creating `src/Test.lean`).
- Anything system-level — `apt`/`brew` installs, any `curl | sh` installer, anything that touches the system outside the workspace — show the exact command to the learner and get their confirmation before running it. Never run these silently.

## DOCTOR mode

Run each check, report OK / MISSING in plain language (not a raw terminal dump) as you go:

1. `git --version`
2. `curl --version`
3. `elan --version`
4. `lean --version`
5. `lake --version`
6. `code --version` — VS Code itself
7. `code --list-extensions | grep -i leanprover` — the Lean 4 extension specifically; report separately from VS Code itself, since having the editor without the extension is a common half-done state
7a. On WSL 2 only: `code --list-extensions | grep -i ms-vscode-remote.remote-wsl` — the "WSL by Microsoft" extension; without it, `code .` from inside WSL cannot connect VS Code on Windows into the WSL filesystem. Report separately, same half-done-state reasoning as the Lean extension check.
8. Workspace project health: check that `lakefile.lean` exists in the workspace and that `lake exe cache get` has already been run (a populated `.lake/` build cache is a reasonable signal). Do **not** run a full `lake build` as part of doctor without asking first — if Mathlib's binary cache was never fetched, a full build can take hours. If the learner wants a real build confirmation, offer it and confirm before running.

Summarize at the end: what's working, what's missing, and — if anything is missing — say you can walk them through install mode for exactly the missing pieces.

## INSTALL mode

Operationalizes SG Part III, in order. Narrate what each step does and why before running it.

**Step 1 — Prerequisites.** System-level: show the command, confirm first.
- Ubuntu / WSL 2: `sudo apt update && sudo apt upgrade -y` then `sudo apt install -y git curl build-essential`
- macOS: `brew install git curl` (and `xcode-select --install` if command-line tools are missing)

Verify afterward: `git --version`, `curl --version`.

**Step 2 — elan (the Lean version manager).** System-level installer script: show the command, confirm first.

```
curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
```

After it finishes: `source ~/.profile`, then verify with `elan --version` and `lean --version`.

**Step 3 — Create the Lean project inside the workspace.** Workspace-local: run yourself.

```
cd <workspace>
lake +v4.24.0 new real-analysis-lean math
cd real-analysis-lean
lake update
```

**Step 4 — Fetch the Mathlib binary cache.** Workspace-local: run yourself, but tell the learner what's happening first — this downloads Mathlib's prebuilt binaries and takes a few minutes depending on their connection.

```
lake exe cache get
```

State this warning to the learner verbatim in substance before running it: **Do NOT skip `lake exe cache get`. Without it, your first `lake build` compiles all of Mathlib from source — several hours. With it, everything is ready in minutes.**

**Step 5 — VS Code + Lean 4 extension.** Check `code --version` first. If VS Code itself is missing, you cannot install a GUI application via the shell — guide the learner to download it from code.visualstudio.com and tell them to come back once it's installed. Once VS Code is present, the extension install is a one-line CLI operation — confirm with the learner before running it, since it modifies their editor setup outside the workspace:

```
code --install-extension leanprover.lean4
```

On WSL 2, also check for and (confirm-first) install the "WSL by Microsoft" extension — without it, `code .` from inside WSL cannot connect VS Code on Windows into the WSL 2 filesystem:

```
code --install-extension ms-vscode-remote.remote-wsl
```

**Step 6 — Verify the full stack with the infoview.** Workspace-local file write: create `src/Test.lean` yourself with the SG test example:

```lean
import Mathlib.Analysis.SpecificLimits.Basic

example : Filter.Tendsto (fun n : Nat => (1 : Real) / n)
    Filter.atTop (nhds 0) := by
  exact?
```

Tell the learner to run `code .` from the workspace to open it in VS Code (WSL 2: this opens VS Code on Windows connected into the WSL 2 filesystem), open `src/Test.lean`, and watch the infoview panel on the right. Ask them to confirm: does a goal state and an `exact?` suggestion appear within about 30 seconds as Mathlib loads? That confirmation has to come from the learner — you cannot see their editor. Once they confirm it, the stack is fully operational; update the ledger/state fields that track Lean availability if the tutor skill's onboarding hasn't already.

## Windows-native branch

If platform detection found a native Windows shell (not WSL 2), do not run install mode at all — recommend WSL 2 first. Summarize the rationale from SG Part II in plain language: WSL 2 gives you a native Linux environment where the Lean toolchain "just works," `lake build` runs against a native filesystem (much faster than Windows filesystem access), every shell command in this workflow runs unmodified, and setup is a single command versus several separate installs. Native Windows is supported but rougher — slower builds, and scripts need rewriting.

Guide the learner to the command, but **never execute it yourself** — it requires Administrator PowerShell and a reboot, both outside what you can do from here:

```
wsl --install
```

Tell them, in plain language: open PowerShell as Administrator (right-click Start → Terminal (Admin)), run that command, restart when prompted, and after restart Ubuntu will ask for a username and password. Once that's done, they should reopen their session from inside WSL 2 / Ubuntu (not PowerShell), and then this skill's doctor/install modes apply normally.
