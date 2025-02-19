import streamlit as st

# Titre de l'application
st.title("Calcul de l'IMC")

# Initialisation du compteur d'utilisateurs dans la session
if "user_count" not in st.session_state:
    st.session_state["user_count"] = 0
st.session_state["user_count"] += 1

# Affichage du compteur d'utilisateurs
st.write("Nombre d'utilisateurs :", st.session_state["user_count"])

# Saisie des données par l'utilisateur
poids = st.number_input("Entrez votre poids en kilogrammes (kg) :", min_value=0.0, step=0.1, format="%.1f")
taille = st.number_input("Entrez votre taille en mètres (m) :", min_value=0.0, step=0.01, format="%.2f")

if st.button("Calculer l'IMC"):
    if taille > 0:
        imc = poids / (taille ** 2)
        st.write("Votre IMC est :", round(imc, 2), "kg/m²")  # Unité ajoutée

        # Calcul des limites de poids de santé
        healthy_min = 18.5 * (taille ** 2)
        healthy_max = 24.9 * (taille ** 2)

        # Détermination de l'interprétation et du conseil de prise/perte de poids
        if imc < 18.5:
            interpretation = "Insuffisance pondérale"
            st.warning("Vous êtes en insuffisance pondérale.")
            weight_to_gain = healthy_min - poids
            st.info(
                f"Pour atteindre le poids minimum de santé ({healthy_min:.1f} kg), vous devez gagner environ {weight_to_gain:.1f} kg.")
        elif imc < 25:
            interpretation = "Poids normal"
            st.success("Vous avez un poids normal.")
            st.info(f"Votre poids de santé se situe entre {healthy_min:.1f} kg et {healthy_max:.1f} kg.")
        elif imc < 30:
            interpretation = "Surpoids"
            st.info("Vous êtes en surpoids.")
            weight_to_lose = poids - healthy_max
            st.info(f"Pour atteindre le poids normal, vous devez perdre environ {weight_to_lose:.1f} kg.")
        else:
            # Classification de l'obésité selon l'OMS
            if imc < 35:
                interpretation = "Obésité Classe I"
                st.error("Vous êtes en situation d'obésité (Classe I).")
            elif imc < 40:
                interpretation = "Obésité Classe II"
                st.error("Vous êtes en situation d'obésité (Classe II).")
            else:
                interpretation = "Obésité Classe III"
                st.error("Vous êtes en situation d'obésité (Classe III).")
            weight_to_lose = poids - healthy_max
            st.info(f"Pour atteindre le poids normal, vous devez perdre environ {weight_to_lose:.1f} kg.")
    else:
        st.error("La taille doit être supérieure à 0.")

# Signature de l'application
st.markdown("---")
st.write("exact_data"
         "Dr abdoulaziz aoudi")

# Référence récente de la classification de l'obésité (< 10 ans)
st.markdown("""
**Référence :**  
Organisation Mondiale de la Santé. *Obésité et surpoids*. Fait mis à jour en 2020.  
[WHO Fact Sheet](https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight)
""")
