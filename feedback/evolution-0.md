# Feedback on Evolution 0: skills inventory

File read: `Capstone/evolution-0/README.md`, as committed on 2026-09-04.

## Rubric outcome

| Dimension | Level | Reason |
|---|---|---|
| Completeness and quality | Strong | All eight rows give the course number and title, and all six columns are filled. |
| Evidence and artifacts | Proficient | Every link works but opens your public repository `gchung1/Capstone`. Two samples do not show what their rows claim. |
| Self-assessment accuracy | Developing | Thirteen of your 26 weakest entries contain the word "advanced". The CIDM 6325 row claims "basic HTML pages", and the repository it links holds a Django application. |
| Integration thinking | Proficient | The four areas read as different subjects. The CIDM 6375 row puts Tableau, Power BI, and ETL under Systems Development. |
| Professional presentation | Strong | The table renders on GitHub, and your AI line says which tool you used and for what. |

## What is working

Your security rows rest on your own results. The CIDM 6340 row claims basic analysis with Nmap and Wireshark. Item 2 of your audit plan reports what each tool showed: open SMB, UPnP, and printer services in the scan, and ordinary DNS, HTTPS, and ARP traffic in the capture.

Your note explains your Systems Development rows. Only one of your courses focused directly on that area, so CIDM 6325 is your primary course there, and the asterisk marks the CIDM 6375 row as the other.

## What needs attention

Remove the contact person's full name from page 1 of `Capstone/CN/artifacts/CIDM-6340/AuditPlan.pdf`, because that person is a third party. Replace the file in this repository with a copy that leaves out the name. The same file is in your public repository `gchung1/Capstone`, so remove the name there too or make that repository private.

Point each evidence link at the copy in this repository, for example `../BA/artifacts/CIDM-5310/StockPriceApp.pdf`. A personal repository can change after I read it. The CIDM 6325 link opens a file that holds only the address of `gchung1/HealthAppeals`. Copy the files that show that row's claims into `Capstone/SS/artifacts/CIDM-6325/`.

Check two rows against their samples. The CIDM 6351 row claims "Basic Snowflake schema development", and the sample shows PostgreSQL tables in pgAdmin. The CIDM 6375 row claims Tableau, Power BI, and ETL, and the sample is a set of answers about ransomware. The prompt asks for a link "that shows the work behind this row". For each claim, cite a sample that shows it, or describe it as a claim you cannot yet show.

## Integration readiness

The skills inventory does not ask for integration, so I read it for whether you treat the four areas as distinct. You mostly do. The CIDM 6375 row is the clearest mix of areas, pairing analytics tools with risk management.

## Question to carry forward

The linked CIDM 6325 repository holds a Django application with 14 architecture decision records. Which parts of that application could you build again without help?
