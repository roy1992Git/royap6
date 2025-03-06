import streamlit as st
mcqs = [
    {
        "situation": "Si Liza ay nagtatrabaho sa isang pabrika kung saan siya ay inaasahang mag-overtime araw-araw...",
        "question": "Ano ang pinakamainam na hakbang na maaaring gawin ni Liza upang maprotektahan ang kanyang karapatan bilang manggagawa?",
        "choices": {
            "A": "Hikayatin ang kanyang mga kasamahan na sama-samang hilingin ang pagtaas ng kanilang sahod.",
            "B": "Manahimik na lamang at magtiis dahil mahirap makahanap ng ibang trabaho.",
            "C": "Maghanap ng ibang trabaho upang maiwasan ang gulo sa kanyang kasalukuyang employer.",
            "D": "Magsampa ng reklamo sa Department of Labor and Employment (DOLE) upang maprotektahan ang kanyang karapatan."
        },
        "answer": "D",
        "explanation": "Ang tamang sagot ay D. Ang DOLE ay ahensyang tumutulong sa mga manggagawang may isyu sa benepisyo at sahod."
    },
    {
        "situation": "Si Mario ay isang masipag na estudyante na nais makatapos ng pag-aaral...",
        "question": "Ano ang dapat gawin ni Mario upang matuloy ang kanyang edukasyon?",
        "choices": {
            "A": "Magtrabaho muna at ipagpaliban ang kanyang pag-aaral upang makatulong sa pamilya.",
            "B": "Maghanap ng scholarship sa isang pribadong paaralan upang makapag-aral nang libre.",
            "C": "Mag-enroll sa isang pampublikong paaralan kung saan libre ang edukasyon.",
            "D": "Humingi ng tulong sa kanyang mga guro upang makahanap ng paraan para sa kanyang matrikula."
        },
        "answer": "C",
        "explanation": "Ang tamang sagot ay C. May batas sa Pilipinas na nagbibigay ng libreng edukasyon sa pampublikong paaralan."
    },
    {
        "situation": "Si Carlos ay isang first-time voter na excited bumoto sa darating na halalan...",
        "question": "Ano ang pinakamainam na desisyon na maaaring gawin ni Carlos sa sitwasyong ito?",
        "choices": {
            "A": "Maghanap ng ibang kandidato na maaari ding magbigay ng pera bago siya magdesisyon.",
            "B": "Huwag bumoto upang maiwasan ang ganitong klaseng panunuhol at panggigipit.",
            "C": "Ipagbigay-alam sa mga awtoridad ang nangyayaring vote buying upang mapanatili ang malinis na halalan.",
            "D": "Tanggapin ang pera ngunit bumoto ayon sa kanyang sariling paniniwala."
        },
        "answer": "C",
        "explanation": "Ang tamang sagot ay C. Ang vote buying ay isang ilegal na gawain na nakasisira sa demokratikong proseso."
    },
    {
        "situation": "Napansin ni Karen na hindi tamang itinatapon ng kanyang mga kapitbahay ang kanilang basura...",
        "question": "Ano ang dapat gawin ni Karen upang mapanatili ang kalinisan sa kanilang barangay?",
        "choices": {
            "A": "Huwag pansinin ang basura dahil hindi naman siya ang nagtapon.",
            "B": "Kausapin ang mga kapitbahay at hikayatin silang sumunod sa tamang pagtatapon ng basura.",
            "C": "Magtapon na rin ng basura kahit saan dahil ginagawa rin naman ito ng iba.",
            "D": "Umalis na lang sa kanilang barangay upang maiwasan ang problema."
        },
        "answer": "B",
        "explanation": "Ang tamang sagot ay B. Dapat hikayatin ni Karen ang kanyang mga kapitbahay na sumunod sa wastong pamamahala ng basura."
    },
    {
        "situation": "Habang naglalakad si Ben pauwi, nakakita siya ng isang pitaka sa daan...",
        "question": "Ano ang tamang gawin ni Ben sa sitwasyong ito?",
        "choices": {
            "A": "Kunin ang pitaka at gamitin ang pera para sa kanyang pangangailangan.",
            "B": "Ipagwalang-bahala na lamang ang pitaka at magpatuloy sa paglalakad.",
            "C": "Ibigay ito sa awtoridad o sa barangay upang mahanap ang may-ari.",
            "D": "Itago ang pitaka at hintayin kung may hahanap dito."
        },
        "answer": "C",
        "explanation": "Ang tamang sagot ay C. Dapat ibigay ni Ben ang pitaka sa awtoridad upang matulungan ang may-ari na makuha ito."
    }
]
mcqs.extend([
    {
        "situation": "Napansin ni Karen na hindi tamang itinatapon ng kanyang mga kapitbahay ang kanilang basura...",
        "question": "Ano ang dapat gawin ni Karen upang mapanatili ang kalinisan sa kanilang barangay?",
        "choices": {
            "A": "Huwag pansinin ang basura dahil hindi naman siya ang nagtapon.",
            "B": "Kausapin ang mga kapitbahay at hikayatin silang sumunod sa tamang pagtatapon ng basura.",
            "C": "Magtapon na rin ng basura kahit saan dahil ginagawa rin naman ito ng iba.",
            "D": "Umalis na lang sa kanilang barangay upang maiwasan ang problema."
        },
        "answer": "B",
        "explanation": "Ang tamang sagot ay B. Dapat hikayatin ni Karen ang kanyang mga kapitbahay na sumunod sa wastong pamamahala ng basura."
    },
    {
        "situation": "Habang naglalakad si Ben pauwi, nakakita siya ng isang pitaka sa daan...",
        "question": "Ano ang tamang gawin ni Ben sa sitwasyong ito?",
        "choices": {
            "A": "Kunin ang pitaka at gamitin ang pera para sa kanyang pangangailangan.",
            "B": "Ipagwalang-bahala na lamang ang pitaka at magpatuloy sa paglalakad.",
            "C": "Ibigay ito sa awtoridad o sa barangay upang mahanap ang may-ari.",
            "D": "Itago ang pitaka at hintayin kung may hahanap dito."
        },
        "answer": "C",
        "explanation": "Ang tamang sagot ay C. Dapat ibigay ni Ben ang pitaka sa awtoridad upang matulungan ang may-ari na makuha ito."
    },
    {
        "situation": "Si Rico ay madalas gumagamit ng social media upang magbahagi ng kanyang opinyon...",
        "question": "Ano ang dapat isaalang-alang ni Rico bago mag-post ng isang opinyon online?",
        "choices": {
            "A": "Siguraduhin na totoo at may basehan ang kanyang ibabahagi.",
            "B": "Ibahagi agad ang kanyang nararamdaman nang hindi iniisip ang epekto nito.",
            "C": "Mag-post ng kahit anong opinyon upang mapansin ng maraming tao.",
            "D": "Huwag magbigay ng opinyon upang maiwasan ang anumang diskusyon."
        },
        "answer": "A",
        "explanation": "Ang tamang sagot ay A. Dapat siguraduhin ni Rico na totoo at may basehan ang kanyang ibabahagi upang maiwasan ang maling impormasyon."
    },
    {
        "situation": "Napansin ni Lea na may kaklase siyang laging malungkot at hindi nakikihalubilo...",
        "question": "Ano ang pinakamainam na gawin ni Lea upang matulungan ang kanyang kaklase?",
        "choices": {
            "A": "Huwag siyang kausapin upang hindi maapektuhan ng kanyang lungkot.",
            "B": "Ipagkalat sa buong klase na palaging malungkot ang kanyang kaklase.",
            "C": "Lapitan siya, kausapin, at iparamdam na may handang makinig sa kanya.",
            "D": "Iwasan siya dahil baka mahawa rin siya sa kanyang lungkot."
        },
        "answer": "C",
        "explanation": "Ang tamang sagot ay C. Ang pagpapakita ng suporta at pakikinig ay makakatulong sa isang taong may pinagdaraanan."
    },
    {
        "situation": "Si Mark ay napansin na may kaklase siyang palaging nahuhuli sa klase...",
        "question": "Ano ang maaaring gawin ni Mark upang matulungan ang kanyang kaklase?",
        "choices": {
            "A": "Pagtawanan ang kanyang kaklase dahil lagi siyang nahuhuli.",
            "B": "Huwag pansinin dahil hindi naman ito ang kanyang problema.",
            "C": "Kaibiganin siya at alamin kung may maitutulong upang hindi siya mahuli.",
            "D": "Sabihin sa guro na palayasin ang kaklase dahil palagi siyang nahuhuli."
        },
        "answer": "C",
        "explanation": "Ang tamang sagot ay C. Dapat ipakita ni Mark ang malasakit sa kanyang kaklase sa pamamagitan ng pagtulong at pag-unawa."
    }
])

# Streamlit UI
st.title("📚 Interactive MCQ Quiz")

score = 0  # Score counter

for index, mcq in enumerate(mcqs):
    st.subheader(f"Tanong {index + 1}:")
    st.write(mcq["situation"])
    st.write(mcq["question"])

    # Gumamit ng unique key para sa bawat tanong
    user_answer = st.radio("Piliin ang sagot:", list(mcq["choices"].values()), key=f"q{index}")

    # Button para sa sagot
    if st.button(f"Ipakita ang Sagot {index + 1}", key=f"btn_{index}"):
        correct_choice = mcq["choices"][mcq["answer"]]
        
        if user_answer == correct_choice:
            st.success(f"✅ Tama! {mcq['explanation']}")
            score += 1
        else:
            st.error(f"❌ Mali. Ang tamang sagot ay: {correct_choice}\n\n💡 {mcq['explanation']}")

# Ipakita ang final score kapag natapos lahat ng tanong
st.write(f"### 🏆 Kabuuang Score: {score}/{len(mcqs)}")
