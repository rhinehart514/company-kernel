# Migrate from 0.5

0.5 found the right topology. 0.6 makes it useful out of the box.

## What changed

### Stronger shared prior

`KERNEL.md` now teaches the model the 2026 startup environment rather than only routing files.

### Stronger domain standards

Coding, Product, and GTM now explain:

- what changed
- what remains scarce
- how to make the call
- which historical defaults to reject
- where human authority begins
- what done means

### Simpler repository

The repository root is now the plugin.

Removed:

- nested `plugins/company-kernel/`
- mirrored canonical system files
- extra architecture documents saying the same thing differently
- version-specific skill names that sounded like internal machinery

### Clearer skills

- `$kernel-integrate` becomes `$kernel-setup`
- `$project-model` becomes `$project-update`
- `$kernel-review` remains `$kernel-review`

## Migration rule

Do not copy old files line for line.

Recompile them:

1. preserve stronger user-authored judgment
2. install the 0.6 shared kernel
3. move durable project truth into `PROJECT.md` and `.kernel/*`
4. delete Company Kernel-owned 0.5 duplication
5. keep uncertainty visible
6. validate routes

Run:

```text
$kernel-setup Migrate this machine and project from Company Kernel 0.5 to 0.6.
Preserve stronger rules and current project truth. Replace only Company Kernel-owned files and skills.
Do not copy old prose mechanically. Recompile it against current repository and market reality.
```
