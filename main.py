from program import Program
from api.main import get_data

#Läser in ny data från APIer
result = get_data()

#När funktionen är klar så retuneras True och resten av programmet körs
#(Skulle någon API inte fungera så kommer programmet att förlita sig på senast sparad data, det kommer då att meddelas när den senaste datan blev hämtad)
if result:
  #Skapar och kallar på klassen "program"
  Program() 
