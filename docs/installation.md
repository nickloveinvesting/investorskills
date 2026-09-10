# Installing a Skill

Every skill is the same three files. `SKILL.md` is the only one the AI needs.

## Claude (web or desktop)

1. Create a Project.
2. Open **Project knowledge**.
3. Upload `SKILL.md`. Add `references/` files too if the skill has them.
4. Start a chat inside that Project.

The skill stays active for every conversation in the Project.

## Claude Code

```bash
mkdir -p .claude/skills/<skill-slug>
cp -r path/to/<skill-slug>/* .claude/skills/<skill-slug>/
```

Or append the contents of `SKILL.md` to your `CLAUDE.md`.

## ChatGPT

1. Create a Project (or a Custom GPT).
2. Paste `SKILL.md` into the instructions field.
3. Upload `references/` files to the Project's files if present.

Note: Projects have an instruction length limit. For skills with references,
upload `SKILL.md` as a file rather than pasting it.

## Cursor

Append `SKILL.md` to `.cursorrules` in the project root, or save it as
`.cursor/rules/<slug>.mdc`.

## Verifying it worked

Ask the model: *"What skill are you running and what inputs do you require?"*

A correctly installed skill names itself and lists its required inputs. If it
gives a generic answer, the file is not in context.

## Skills with references

`multifamily-underwriting` ships 15 reference documents. Load `SKILL.md` always.
Load the reference files that match the task, or all of them if your tool has the
context budget. `SKILL.md` contains a navigation table telling the model which
reference to open for which question.

## Updating

Replace `SKILL.md` with the newer version. Check `version:` in the frontmatter to
see which you have.
