# Feedback on Evolution 4: Networking and Cybersecurity

File read: `Capstone/CN/evolution.md`, as committed on 2026-10-08.

## Rubric outcome

| Dimension | Level | Reason |
|---|---|---|
| Completeness and quality | Developing | The appraisal lists no sources you consulted. The third tier repeats your weaknesses (enterprise networks, advanced tools, new threats). |
| Evidence and artifacts | Proficient | The audit plan and the ShieldsUP report in `Capstone/CN/artifacts/` show your Nmap, Wireshark, and ShieldsUP work. The appraisal reports none of their findings, and the configuration and architecture exercises have no sample. |
| Self-assessment accuracy | Proficient | You place this area between Software and Systems and the data areas, and you separate your understanding of risk from your ability to implement controls. |
| Integration thinking | Developing | One paragraph repeats five sentences of Evolution 3 word for word, and the new statement repeats its four-part chain. |
| Professional presentation | Proficient | The twelve typed "•" bullets in Supporting Evidence render on GitHub as two run-on paragraphs. |

## What is working

You explain your ranking of the area. You understand security "as an organizational and healthcare risk" better than you can implement controls, and you say that your hands-on networking has been in small environments.

Your integration section lists controls that a builder could act on: authentication, authorization, access controls, secure transmission, protection of stored information, and a routine security assessment.

## What needs attention

Remove the contact person's full name from page 1 of `Capstone/CN/artifacts/CIDM-6340/AuditPlan.pdf`. This appraisal cites CIDM 6340, and that file is its sample. Your Evolution 0 feedback gives the steps, including those for the public copy in `gchung1/Capstone`.

Add an AI-use line so that a reader knows what help you had. In one sentence, say which tool, if any, helped and with what. At the final commit, this appraisal moves to `portfolio/CN/README.md`.

Report what your samples found. Your Supporting Evidence lists topics such as "NMAP scans" without results. Your audit plan records about 18 active devices, active SMB, UPnP, and printer services, and no network segmentation. Your CIDM 6341 report records that ShieldsUP found the tested ports stealthed while the network still answered a ping. Cite each file by path with the result it shows. That report also cites Gibson Research Corporation, which is the kind of source the prompt asks you to list.

## Integration readiness

Not yet ready. The controls are concrete, but the next paragraph repeats Evolution 3. Your CIDM 6325 requirements document for the same appeals generator rules out login and data storage. This appraisal plans authentication and protection of stored information and does not mention that earlier decision.

## Question to carry forward

Will the prototype keep your earlier decision to require no login and store no data? If it does, which controls on your list still apply?
