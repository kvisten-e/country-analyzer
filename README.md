# Country Analyzer Europe

Välkommen till Country Analyzer för Europa, en applikation designad för att analysera finansiell data för Europas länder. Detta verktyg erbjuder insiktsfull analys av nyckelekonomiska indikatorer, vilket hjälper användaren att förstå de finansiella trenderna för länder över hela Europa.

## Datahantering

Applikationen fokuserar på analys av följande ekonomiska indikatorer:

- BNP (Bruttonationalprodukt)
- Inflation
- Räntor

Data för BNP och inflation hämtas från Världsbankens Data API (wbgapi), som erbjuder ett omfattande bibliotek för enkel åtkomst och hantering av ekonomisk data, räntedata hämtas från Internationella Valutafondens (IMF) API. Detta säkerställer att användarna alltid har tillgång till den senaste tillgängliga datan.

## Hur Programmet Fungerar

Programmet fungerar enligt följande:

1. **Datahämtning:** Vid uppstart hämtar programmet den senaste datan från API:erna för att säkerställa att analyser baseras på den mest aktuella informationen som finns tillgänglig. Vid en API-avbrott eller timeout kommer programmet att förlita sig på den senast sparade lokala datan. Användare kommer att meddelas om detta fallback inträffar.

2. **Huvudmeny:** Användaren presenteras med en startmeny som erbjuder olika alternativ för dataanalys. Beroende på val, kommer specifika typer av finansiell data att visas:

   - **Visa Finansiell Data för Ett Enskilt Land:** Analysera de ekonomiska indikatorerna för ett valt land.

   - **Visa BNP-data för Alla Länder:** Jämför och kontrastera BNP-siffror över Europas länder.

   - **Visa Inflationsdata för Alla Länder:** Undersök inflationstrender och data för varje land i Europa.

   - **Visa Räntedata för Alla Länder:** Bedöm räntorna för Europas länder, vilket ger insikter om penningpolitik och ekonomiska förhållanden.

3. **Meny "Finansiell Data för Ett Enskilt Land":**
   
   - **Jämför Data med Annat Land:** Möjliggör för användare att ställa ett lands data mot en annan sida vid sida för att enkelt och tydligt se vilket land som har bättre finansiella indikatorer.
   
   - **Skapa en Prognos för X År:** För närvarande förlitar sig programmet enbart på "Linjär Regression"-metoden, så resultatet kan inte ses som en pålitlig källa. För att ta fram ett estimerat värde, förlitar sig programmet på biblioteket "sklearn.linear_model".

### Ytterligare Funktioner:

- **Visa BNP-data för Alla Länder:** När detta val väljs, visas en lista över alla Europas länder tillsammans med deras BNP-data för ett angivet årsspann. Denna funktion låter användare förstå den ekonomiska storleken och produktiviteten för varje land i förhållande till andra.

- **Visa Inflationsdata för Alla Länder:** Detta alternativ presenterar en lista över Europeiska länder och deras inflationstakt över en vald period. Användare kan analysera hur priser har ökat över olika nationer, vilket indikerar inflationstrycket inom varje ekonomi.

- **Visa Räntedata för Alla Länder:** Genom att välja detta, kan användare få tillgång till en lista som visar räntorna för Europeiska länder för en given tidsram. Denna data hjälper till att förstå penningpolitiken för varje land, inklusive hur det hanterar inflation och stimulerar eller svalnar ekonomin.

Var och en av dessa funktioner ger användare omfattande insikter i de finansiella dynamikerna för Europas länder.