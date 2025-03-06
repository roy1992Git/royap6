import streamlit as st
import time
import random
import streamlit.components.v1 as components

questions = [
 {
        "situation": "Si Liza ay nagtatrabaho sa isang pabrika kung saan siya ay inaasahang mag-overtime araw-araw. Gayunpaman, hindi siya binabayaran para sa dagdag na oras ng trabaho at wala siyang natatanggap na benepisyo tulad ng health insurance. Nang tanungin niya ang kanyang employer tungkol dito, sinabi lamang na 'ganyan talaga dito.' Sa kabila ng kanyang pag-aalinlangan, napag-alaman niya na may batas na nagpoprotekta sa mga manggagawa laban sa hindi makatarungang pasahod at benepisyo. Ngayon, nais niyang malaman kung paano niya maipaglalaban ang kanyang karapatan nang hindi nawawalan ng trabaho.",
        "question": "Ano ang pinakamainam na hakbang na maaaring gawin ni Liza upang maprotektahan ang kanyang karapatan bilang manggagawa?",
        "choices": {
            "A": "Hikayatin ang kanyang mga kasamahan na sama-samang hilingin ang pagtaas ng kanilang sahod.",
            "B": "Manahimik na lamang at magtiis dahil mahirap makahanap ng ibang trabaho.",
            "C": "Maghanap ng ibang trabaho upang maiwasan ang gulo sa kanyang kasalukuyang employer.",
            "D": "Magsampa ng reklamo sa Department of Labor and Employment (DOLE) upang maprotektahan ang kanyang karapatan."
        },
        "answer": "D",
        "explanation": "Ang tamang sagot ay D. Ang DOLE ay may mandato na tiyakin ang karapatan ng mga manggagawa, kabilang ang tamang pasahod at benepisyo. Ang pagsasampa ng reklamo ay isang lehitimong paraan upang maprotektahan ang kanyang karapatan."
    },
    {
        "situation": "Si Mario ay isang masipag na estudyante na nais makatapos ng pag-aaral. Sa kasamaang-palad, kulang ang kinikita ng kanyang mga magulang upang ipagpatuloy niya ang kanyang pag-aaral sa isang pribadong paaralan. Dahil dito, napag-isipan niyang huminto na lang at maghanap ng trabaho upang makatulong sa kanyang pamilya. Sa isang talakayan sa kanilang barangay, nalaman niyang may batas na nagsasaad na ang bawat batang Pilipino ay may karapatan sa libreng edukasyon sa pampublikong paaralan. Nais niyang malaman kung ano ang kanyang pinakamainam na opsyon upang makapagpatuloy sa pag-aaral.",
        "question": "Ano ang dapat gawin ni Mario upang matuloy ang kanyang edukasyon?",
        "choices": {
            "A": "Magtrabaho muna at ipagpaliban ang kanyang pag-aaral upang makatulong sa pamilya.",
            "B": "Maghanap ng scholarship sa isang pribadong paaralan upang makapag-aral nang libre.",
            "C": "Mag-enroll sa isang pampublikong paaralan kung saan libre ang edukasyon.",
            "D": "Humingi ng tulong sa kanyang mga guro upang makahanap ng paraan para sa kanyang matrikula."
        },
        "answer": "C",
        "explanation": "Ang tamang sagot ay C. Ayon sa batas ng Pilipinas, may libreng edukasyon sa pampublikong paaralan, kaya ito ang pinaka-angkop na opsyon para kay Mario."
    },
    {
        "situation": "Si Carlos ay isang first-time voter na excited bumoto sa darating na halalan. Isang araw, may lumapit sa kanya na kinatawan ng isang kandidato at inalok siya ng pera kapalit ng kanyang boto. Alam ni Carlos na ilegal ang ganitong gawain ngunit naisip niyang sayang ang perang inaalok. Sa parehong pagkakataon, napagtanto rin niyang mahalaga ang kanyang boto sa pagpili ng tamang lider para sa bayan. Ngayon, nalilito siya kung ano ang dapat niyang gawin.",
        "question": "Ano ang pinakamainam na desisyon na maaaring gawin ni Carlos sa sitwasyong ito?",
        "choices": {
            "A": "Maghanap ng ibang kandidato na maaari ding magbigay ng pera bago siya magdesisyon.",
            "B": "Huwag bumoto upang maiwasan ang ganitong klaseng panunuhol at panggigipit.",
            "C": "Ipagbigay-alam sa mga awtoridad ang nangyayaring vote buying upang mapanatili ang malinis na halalan.",
            "D": "Tanggapin ang pera ngunit bumoto ayon sa kanyang sariling paniniwala."
        },
        "answer": "C",
        "explanation": "Ang tamang sagot ay C. Ang vote buying ay isang ilegal na gawain na maaaring ipagbigay-alam sa mga awtoridad upang mapanatili ang patas na halalan."
    },
    {
        "situation": "Si Jenny ay mahilig bumili ng imported na damit at pagkain mula sa ibang bansa. Kahit maraming Pilipinong negosyante ang gumagawa ng de-kalidad na produkto, hindi niya ito binibigyang pansin dahil mas nasanay siyang bumili ng dayuhang tatak. Isang araw, nalaman niya sa klase na ang pagtangkilik sa produktong Pilipino ay isang paraan upang suportahan ang ekonomiya ng bansa. Napaisip siya kung paano makakatulong ang kanyang mga pagbili sa kaunlaran ng Pilipinas.",
        "question": "Ano ang pinakamainam na gawin ni Jenny upang makatulong sa ekonomiya ng bansa?",
        "choices": {
            "A": "Patuloy na bumili ng imported na produkto dahil mas nasanay na siyang gamitin ito.",
            "B": "Simulang bigyang-pansin at pahalagahan ang kalidad ng mga produktong Pilipino.",
            "C": "Bumili ng lokal na produkto kahit hindi ito ang kanyang personal na gusto.",
            "D": "Umiwas na lang sa pamimili upang hindi na mamili ng lokal o imported na produkto."
        },
        "answer": "B",
        "explanation": "Ang tamang sagot ay B. Ang pagtangkilik sa produktong Pilipino ay nakakatulong sa ekonomiya at sa mga lokal na negosyo na lumago."
    },
    {
        "situation": "Si Mark ay isang estudyante na mahilig gumamit ng social media upang manatiling updated sa mga balita. Isang araw, kumalat ang isang video na nagpapakita ng isang insidente ng kaguluhan sa kanilang lungsod. Maraming tao ang agad nagbahagi ng video nang hindi sinusuri ang pinagmulan nito, kaya’t lalong lumala ang panic at maling impormasyon. Nais ni Mark na siguraduhin na tama ang impormasyong kanyang pinaniniwalaan at ibinabahagi sa iba.",
        "question": "Ano ang pinakamahusay na gawin ni Mark upang makatulong sa pagpapanatili ng kapayapaan?",
        "choices": {
            "A": "Magbahagi lamang ng impormasyon kung galing ito sa mapagkakatiwalaang pinagmulan.",
            "B": "Iwasan ang social media upang hindi na maapektuhan ng mga balita.",
            "C": "Mag-react at mag-komento agad sa post upang ipahayag ang kanyang opinyon.",
            "D": "Makiisa sa pagpapakalat ng balita kahit hindi tiyak kung ito ay totoo."
        },
        "answer": "A",
        "explanation": "Ang tamang sagot ay A. Mahalaga ang pagiging mapanuri sa impormasyon upang maiwasan ang maling balita at hindi makatulong sa pagkakalat ng panik."
    },
    {
        "situation": "Sa kanilang barangay, maraming residente ang nagrereklamo tungkol sa hindi maayos na koleksyon ng basura. Sa kabila ng reklamo, patuloy pa rin ang tambak ng basura sa mga lansangan. Napansin din ni Miguel na may mga ulat ng katiwalian sa paggamit ng pondo ng barangay, ngunit walang konkretong aksyon ang ginagawa ng kanilang opisyal. Nais niyang malaman kung paano makakatulong upang matiyak ang pananagutan ng mga namumuno.",
        "question": "Ano ang pinaka-angkop na hakbang na maaaring gawin ni Miguel upang matugunan ang isyu sa kanilang barangay?",
        "choices": {
            "A": "Makipagtulungan sa mga residente upang maghain ng reklamo sa tamang ahensya ng gobyerno.",
            "B": "Lumipat na lamang sa ibang barangay na mas maayos ang sistema.",
            "C": "Huwag na lang makialam at umasa na maaayos ito sa paglipas ng panahon.",
            "D": "Magsumbong sa social media upang mabatikos ang mga opisyal at mapilitan silang umaksyon."
        },
        "answer": "A",
        "explanation": "Ang paghahain ng reklamo sa tamang ahensya ay isang makatarungan at sistematikong paraan upang matiyak ang pananagutan ng mga namumuno at maayos ang problema."
    },
    {
        "situation": "Kakatapos lamang ni Anton sa kolehiyo at kasalukuyan siyang naghahanap ng trabaho. May alok siyang trabaho sa ibang bansa na may mas mataas na sahod, ngunit nais din niyang magtrabaho sa Pilipinas upang makatulong sa pag-unlad ng sariling bayan. Alam niyang ang pagpili ng trabaho ay hindi lamang tungkol sa personal na kita kundi pati na rin sa kanyang kontribusyon sa ekonomiya ng bansa. Ngayon, iniisip niya kung anong desisyon ang makakatulong sa kaunlaran ng Pilipinas.",
        "question": "Ano ang pinakamainam na gawin ni Anton upang makatulong sa ekonomiya ng bansa?",
        "choices": {
            "A": "Magtayo ng negosyo sa Pilipinas upang makatulong sa lokal na ekonomiya.",
            "B": "Pumunta sa ibang bansa upang kumita nang mas malaki at makapagpadala ng pera sa pamilya.",
            "C": "Maghintay muna bago magtrabaho upang pag-isipan ang kanyang mga oportunidad.",
            "D": "Magtrabaho sa isang multinasyunal na kumpanya sa Maynila upang magkaroon ng mataas na kita."
        },
        "answer": "A",
        "explanation": "Ang pagtatayo ng negosyo sa Pilipinas ay nakakatulong sa pagbibigay ng trabaho sa iba at pagpapalakas ng lokal na ekonomiya."
    },
    {
        "situation": "Sa isang paaralan, isinasagawa ang flag ceremony tuwing Lunes upang magbigay galang sa watawat ng Pilipinas. Habang inaawit ang Lupang Hinirang, may ilang estudyanteng hindi seryosong umaawit at may ilan pang nakaupo habang tinutugtog ang pambansang awit. Napansin ito ng kanilang guro at ipinaalala sa kanila ang kahalagahan ng paggalang sa pambansang sagisag ng bansa. Nais niyang siguraduhin na ang mga estudyante ay natututo ng tamang asal sa ganitong okasyon.",
        "question": "Ano ang tamang gawin ng mga estudyante kapag tinutugtog ang pambansang awit?",
        "choices": {
            "A": "Manatiling nakaupo kung hindi pabor sa kasalukuyang administrasyon.",
            "B": "Kumanta nang malakas upang ipakita ang pagiging makabayan kahit hindi tama ang tono.",
            "C": "Tumayo nang tuwid at ipakita ang paggalang sa watawat ng Pilipinas.",
            "D": "Magpatuloy sa pakikipag-usap sa kaklase habang tinutugtog ito."
        },
        "answer": "C",
        "explanation": "Ang pagtayo nang tuwid habang tinutugtog ang pambansang awit ay isang paraan ng pagpapakita ng respeto sa watawat at sa bansa."
    },
    {
        "situation": "Si Nica ay mahilig gumamit ng social media upang ipahayag ang kanyang opinyon tungkol sa mga isyu sa lipunan. Isang araw, nag-post siya ng kanyang pananaw at may isang taong hindi sumang-ayon sa kanya. Sa halip na makipag-usap nang maayos, sinimulan siyang siraan online gamit ang masasakit na salita. Sa kabila nito, nais ni Nica na ipakita ang tamang asal sa paggamit ng social media.",
        "question": "Ano ang pinakamainam na hakbang na maaaring gawin ni Nica sa ganitong sitwasyon?",
        "choices": {
            "A": "Hayaan na lang at huwag nang patulan ang mga negatibong komento.",
            "B": "Balikan at awayin ang taong naninira sa kanya online upang ipagtanggol ang sarili.",
            "C": "Mag-post din ng masasakit na salita bilang ganti sa taong naninira sa kanya.",
            "D": "Magsampa ng reklamo kung lumalabag na ito sa kanyang karapatan."
        },
        "answer": "D",
        "explanation": "Ang pagsasampa ng reklamo ay isang legal na paraan upang maprotektahan ang sarili laban sa cyberbullying o paninirang-puri sa social media."
    },
    {
        "situation": "Si Rico ay nagmamadaling umuwi nang biglang parahin siya ng isang pulis dahil sa paglabag sa batas-trapiko. Nang ipakita sa kanya ang violation ticket, inalok siya ng pulis na magbayad nang direkta upang hindi na siya tiketan. Alam ni Rico na ang ganitong gawain ay isang anyo ng katiwalian. Gayunpaman, gusto niyang makaalis kaagad at maiwasan ang abala.",
        "question": "Batay sa sitwasyon ni Rico, ano ang pinaka-angkop na hakbang na nagpapakita ng tamang pagsunod sa batas?",
        "choices": {
            "A": "Bayaran ang pulis upang mabilis na makaalis at hindi na maabala.",
            "B": "Tumanggi sa alok ng pulis at bayaran ang tamang multa ayon sa batas.",
            "C": "I-post sa social media ang nangyari upang ipahiya ang pulis.",
            "D": "Umalis na lamang nang hindi pinapansin ang sinasabi ng pulis."
        },
        "answer": "B",
        "explanation": "Ang pagbabayad ng tamang multa sa legal na paraan ay nagpapakita ng integridad at pagsunod sa batas."
    },
]

st.title("Practice Exam")

if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.show_explanation = False
    st.session_state.user_answer = None

def reset_question():
    st.session_state.current_question = (st.session_state.current_question + 1) % len(questions)
    st.session_state.show_explanation = False
    st.session_state.user_answer = None

q = questions[st.session_state.current_question]
st.subheader(f"Tanong {st.session_state.current_question + 1}")
st.write(q["situation"])
st.write(f"**{q['question']}**")

choices = list(q["choices"].items())
random.shuffle(choices)

user_answer = st.radio("Piliin ang sagot:", choices, index=None, format_func=lambda x: f"{x[0]}: {x[1]}")

if st.button("I-submit"):
    if user_answer:
        st.session_state.user_answer = user_answer[0]
        st.session_state.show_explanation = True

if st.session_state.show_explanation:
    time.sleep(0.5)
    if st.session_state.user_answer == q["answer"]:
        st.success("🎉 Tama ang sagot! Mahusay! 🎉")
        components.html("""
        <div style='text-align: center;'>
            <img src='https://media.giphy.com/media/26FPOCMy0WWagaf3G/giphy.gif' width='200'>
        </div>
        """, height=200)
        time.sleep(2)
        reset_question()
    else:
        st.error("❌ Maling sagot. Subukan muli! ❌")
        components.html("""
        <div style='text-align: center;'>
            <img src='https://media.giphy.com/media/3o6ZsYc6H0wFPpabZS/giphy.gif' width='200'>
        </div>
        """, height=200)
        time.sleep(2)
        reset_question()
