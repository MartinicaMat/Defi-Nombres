import time

print("Create Studios Presente")
print("--- DEFI NOMBRES ---")
print("Pense a un nombre entre 1 et 100 dans ta tete.")
print("Je vais essayer de le devine en moins de 7 coups. Ne triche pas !")
time.sleep(2)  

bas = 1
haut = 100
gagne = False
tentatives = 0

while not gagne and bas <= haut:
    proposition = (bas + haut) // 2
    tentatives += 1

    print(f"\n[Coup {tentatives}] Est-ce que c'est {proposition} ?")
    reponse = input("Reponds par '+' (plus grand), '-' (plus petit) ou '=' (trouve) : ").strip()
    
    if reponse == '=':
        # Correction ici : ajout du f"" pour que les variables s'affichent bien
        print(f"\nGG ! J'ai trouve ton nombre ({proposition}) en {tentatives} coups !")
        gagne = True
    elif reponse == '+':
        bas = proposition + 1
    elif reponse == '-':
        haut = proposition - 1
    else:
        print("Je n'ai pas compris ta reponse... Utilise +, - ou = !")
        tentatives -= 1 

if not gagne:
    print("\nTu as du te tromper dans tes reponses, c'est impossible !")