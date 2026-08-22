# Coding Standard

Optimize for verified product change, not code volume: speed, coherence, reversibility, reliability, and operational burden are one decision.
Prefer the smallest architecture that preserves important future choices; add abstraction only after repeated pressure reveals a stable boundary.
Scale rigor with consequence, uncertainty, and irreversibility. Security, data, money, external effects, and hard migrations require stronger isolation, evidence, and human judgment.
Change systems coherently, not timidly or indiscriminately: inspect ownership and flows, repair adjacent causes when needed, remove dead paths, and avoid unrelated redesign.
Match evidence to the claim. Types and unit tests do not prove integrated, runtime, operational, or user-visible behavior.
Use agents and parallelism when ownership, interfaces, and verification remain clear; generated volume never substitutes for understanding.
Treat context as an engineering input: load the smallest decision-relevant model, preserve constraints and provenance, and do not compensate for missing truth with generated code.
Investigate when the unknown can change architecture or failure surface; otherwise make the most reversible sound call and continue.
Escalate decisions that materially alter security, product behavior, external commitments, cost structure, or irreversible architecture.
