# Country Analyzer Europe

## Översikt

Country Analyzer Europe är en applikation utvecklad för att analysera och presentera ekonomisk data för Europas länder. Genom att använda sig av aktuella data från Världsbankens och Internationella Valutafondens API:er, möjliggör programmet insiktsfull analys av ekonomiska indikatorer så som BNP, inflation och räntor.

### Starta Programmet

För att starta Country Analyzer Europe, kör följande kommando i terminalen eller kommandotolken:

```
py main.py
```

### Programflöde

1. **Datahämtning:** Vid uppstart hämtar programmet automatiskt den senaste ekonomiska datan från definierade API:er och uppdaterar en lokal JSON-fil för offline-användning.

2. **Huvudmeny:** Användaren navigerar genom en interaktiv meny för att välja önskad funktion.

#### Analysalternativ:

- **Enskilt Land:** Analysera och presentera ekonomiska data för ett specifikt valt land.
***Prognos:*** Genererar en ekonomisk prognos baserad på linjär regression för ett specifikt år.
***Jämnför:*** Ställer två länder sida vid sida för att enkelt kunna jämnföra.
- **Alla Länder:** Jämför ekonomiska indikatorer (BNP, inflation, räntor) över alla Europas länder.

### Avsluta Programmet

Användaren kan när som helst välja att avsluta programmet genom att välja motsvarande alternativ i huvudmenyn.


## Datahantering

Applikationen fokuserar på analys av följande ekonomiska indikatorer:

- BNP (Gross domestic product - GDP)
- Inflation
- Räntor

Data för BNP och inflation hämtas från Världsbankens Data API (wbgapi), som erbjuder ett omfattande bibliotek för enkel åtkomst och hantering av ekonomisk data, räntedata hämtas från Internationella Valutafondens (IMF) API. Detta säkerställer att användarna alltid har tillgång till den senaste tillgängliga datan. 

## Hur Programmet Fungerar

Programmet fungerar enligt följande:

1. **Datahämtning:** Vid uppstart hämtar programmet den senaste datan från API:erna för att säkerställa att analyser baseras på den mest aktuella informationen som finns tillgänglig. Den nya datan kommer att uppdatera en lokalt sparad JSON-fil. Vid ett API-avbrott eller timeout vid uppstart så kommer programmet att förlita sig på den senast sparade lokala datan sen senast programmet kördes. Användaren kommer att meddelas om detta fallback inträffar. När funktionen för hämtning av data är genomförd (lyckad eller ej), så leds användaren till huvudmenyn.

2. **Huvudmeny:** Användaren presenteras med en startmeny som erbjuder olika alternativ för dataanalys. Beroende på val, kommer specifika typer av finansiell data att visas:

   - **Visa Finansiell Data för Ett Enskilt Land:** Analysera de ekonomiska indikatorerna för ett valt land.

   - **Visa BNP-data för Alla Länder:** Jämför och kontrastera BNP-siffror över Europas länder.

   - **Visa Inflationsdata för Alla Länder:** Undersök inflationstrender och data för varje land i Europa.

   - **Visa Räntedata för Alla Länder:** Bedöm räntorna för Europas länder.

3. **Meny "Finansiell Data för Ett Enskilt Land":**

   Vid detta val så tillfrågas användaren att välja ett land som man vill analysera data på. Klassen "summary_country" skapas och triggar funktionen "choose_country" som presenterar alla val av länder som finns tillgängliga. Vid felskrivning eller val av ett land som ej finns med på listan så kommer man få möjligheten att försöka igen. 

   Vid lyckad input så kommer funktionen "print_country_data" att kallas och presentera tillgänglig data för just det land som man valt.
   En ny meny kommer att visas och ger användaren ytteliggare val att göra för att jobba med datan som presenterats. 
   
   - **Jämför Data med Annat Land:** Möjliggör för användare att ställa ett lands data mot en annan sida vid sida för att enkelt och tydligt se vilket land som har bättre finansiella indikatorer. Likt tidigare så blir man tillfrågad att mata in vilket land man vill jämnföra med och funktionen "compare_countries" anropas med båda ländernas koder. Denna funktion kommer sen att skapa en ny dataframe där den ställer resultaten för båda ländernas data bredvid varanda samt visa en procent skillnad mellan dem.
   
   - **Skapa en Prognos för år X:** För närvarande förlitar sig programmet enbart på "Linjär Regression"-metoden, så resultatet kan inte ses som en pålitlig källa. För att ta fram det estimerat värdet, så använder sig programmet på biblioteket "sklearn.linear_model".
   Vid en senare version och mer utveklad program så hade man behövt använda sig av mer avancerade metoder för att estimera pålitlig data.

   Man blir tillfrågad att mata in vilket år som man vill ett etimerat värde på och funktionen "estimate_future" anropas med dess värde och landets kod.
   Data för landet hämtas in och programmat skapar en modell med "sklearn" baserat på den hämtade datan för att kunna genomföra .predict()-metoden som kommer att skapa ett värde.
   Det nya värdet och dess år läggs in med den andra datan och presenteras. 


### Ytterligare Funktioner:

När alternativ 2, 3, eller 4 väljs i huvudmenyn, presenteras data för den specifika indikatorn för samtliga länder i Europa. För detta ändamål skapas klassen "countries_data", vilken sedan används för att anropa den relevanta funktionen baserat på användarens val.

- **Visa BNP-data för Alla Länder:** När detta val väljs, visas en lista över alla Europas länder tillsammans med deras BNP-data för ett satt årsspann. Denna funktion låter användare förstå den ekonomiska storleken och produktiviteten för varje land i förhållande till andra. Funktionen "list_countries_gdp" anropas och data för den indikatorn hämtas från JSON-filen. En dataframe av datan skapas och värden avrundas ner för att vara mer lätt läst. 
Resultat för vilket land som har högst och lägst värde kommer att presenteras under listan på all data. Funktionen "get_higest_lowest" blir tilldelad data och retunerar en lista på två länder samt dess värde.

- **Visa Inflationsdata för Alla Länder:** Detta alternativ presenterar en lista över Europeiska länder och deras inflationstakt över en vald period. Användare kan analysera hur priser har ökat över olika nationer, vilket indikerar inflationstrycket inom varje ekonomi.
Likt val av BNP-data så kallas en funktion men nu list_countries istället. Denna funkar för både inflationsdata och räntedata då dess data inte behöver bearbetas på samma sätt som BNP-datan.

- **Visa Räntedata för Alla Länder:** Genom att välja detta, kan användare få tillgång till en lista som visar räntorna för Europeiska länder för ett satt årsspann. Denna data hjälper till att förstå penningpolitiken för varje land, inklusive hur det hanterar inflation och stimulerar eller svalnar ekonomin.

- **Avsluta:** Man kan på ett enkelt sätt avsluta programmet när man känner sig nöjd. Vid detta val så kallas funktionen "close_program" som ser till att loopen som håller igång programmet avslutas

## Sammanfattning

Var och en av dessa val ger användare omfattande insikter i de finansiella dynamikerna för Europas länder. Vid utökad tid så hade jag gärna jobbat vidare med att hämta in mer ekonomisk data över längre tid. Detta kommer sen bli användbart vid framtagning av fler estimerings metoder av framtida värden. Det hade även varit intressant att lägga till mer data som arbetskraft och valutaförändringar för respektive land. 






