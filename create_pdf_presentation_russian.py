
#!/usr/bin/env python3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, blue, red, green
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def create_pdf_presentation_russian():
    # Create PDF document
    filename = "attached_assets/Pose_Recognition_Presentation_Russian.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=HexColor('#0066CC')
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=20,
        textColor=HexColor('#0066CC')
    )
    
    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=8,
        leftIndent=20,
        bulletIndent=10
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=12,
        alignment=TA_JUSTIFY
    )
    
    # Story array to hold content
    story = []
    
    # Title Page
    story.append(Paragraph("Veb-prilozhenie raspoznavaniya poz", title_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("II-sistema raspoznavaniya poz v realnom vremeni", heading_style))
    story.append(Paragraph("s podderzhkoy lokalnykh modeley", heading_style))
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("Komanda razrabotchikov Replit", normal_style))
    story.append(Paragraph("9 iyulya 2025", normal_style))
    story.append(PageBreak())
    
    # Slide 2: What is Pose Recognition App?
    story.append(Paragraph("Chto takoye prilozhenie raspoznavaniya poz?", heading_style))
    story.append(Paragraph("• Raspoznavanie poz v realnom vremeni s ispolzovaniem veb-kamery", bullet_style))
    story.append(Paragraph("• Avtonomnaya funktsionalnost - internet ne trebuetsya posle nastroyki", bullet_style))
    story.append(Paragraph("• Nastraivaemye parametry dlya 1-7 poz", bullet_style))
    story.append(Paragraph("• Podderzhka lokalnykh modeley s integratsiey Teachable Machine", bullet_style))
    story.append(Paragraph("• Kalibrovka rasstoyaniya dlya optimalnogo pozitsionirovaniya", bullet_style))
    story.append(Paragraph("• Zvukovaya obratnaya svyaz i vizualnoye rukovodstvo", bullet_style))
    story.append(PageBreak())
    
    # Slide 3: Core Features
    story.append(Paragraph("Osnovnye funktsii", heading_style))
    story.append(Paragraph("<b>Sistema raspoznavaniya poz:</b>", normal_style))
    story.append(Paragraph("• Podderzhka 1-7 nastraivaemykh poz", bullet_style))
    story.append(Paragraph("• Otsenka uverennosti v realnom vremeni (porog 30-90%)", bullet_style))
    story.append(Paragraph("• Vizualnoye sravnenie poz s etalonymi izobrazheniyami", bullet_style))
    story.append(Paragraph("• Otslezhivanie skeleta s 17 klyuchevymi tochkami", bullet_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Parametry nastroyki:</b>", normal_style))
    story.append(Paragraph("• Reguliruemaya zaderzhka raspoznavaniya (1-10 sekund)", bullet_style))
    story.append(Paragraph("• Polzovatelskie nazvaniya poz (redaktiruemye yarlyki)", bullet_style))
    story.append(Paragraph("• Pereklyuchatel zvukovogo signala dlya obratnoy svyazi ob uspehe", bullet_style))
    story.append(Paragraph("• Kalibrovka rasstoyaniya s rukovodstvom v realnom vremeni", bullet_style))
    story.append(PageBreak())
    
    # Slide 4: GUI Settings Interface
    story.append(Paragraph("GUI: Interfeys nastroyek", heading_style))
    story.append(Paragraph("<b>Klyuchevye osobennosti:</b>", normal_style))
    story.append(Paragraph("• Zagruzka lokalnykh faylov modeli (model.json, metadata.json, weights.bin)", bullet_style))
    story.append(Paragraph("• Flazhki vybora poz dlya 1-7 poz", bullet_style))
    story.append(Paragraph("• Zagruzka etalonnykh izobrazheniy dlya kazhdoy pozy", bullet_style))
    story.append(Paragraph("• Upravlenie zvukom, zaderzhkoy i porogom tochnosti", bullet_style))
    story.append(Paragraph("• Rukovodstvo po kalibrovke rasstoyaniya", bullet_style))
    
    # Try to add image if it exists
    if os.path.exists("attached_assets/GUI1_1752049448296.png"):
        try:
            story.append(Spacer(1, 0.2*inch))
            story.append(Image("attached_assets/GUI1_1752049448296.png", width=6*inch, height=3*inch))
        except:
            pass
    story.append(PageBreak())
    
    # Slide 5: GUI Recognition Interface
    story.append(Paragraph("GUI: Interfeys raspoznavaniya", heading_style))
    story.append(Paragraph("<b>Funktsii v realnom vremeni:</b>", normal_style))
    story.append(Paragraph("• Pryamaya translyatsiya s veb-kamery s obnaruzheniem poz", bullet_style))
    story.append(Paragraph("• Otobrazenie tekushchey i ozhidaemoy pozy", bullet_style))
    story.append(Paragraph("• Polosa uverennosti s tsvetovym kodirovaniem (zelenyy = pravilno, krasnyy = nepravilno)", bullet_style))
    story.append(Paragraph("• Sravnenie s etalonnym izobrazheniem", bullet_style))
    story.append(Paragraph("• Obnovlenie i vozvrat k nastroykam", bullet_style))
    
    # Try to add image if it exists
    if os.path.exists("attached_assets/GUI2_1752049449853.png"):
        try:
            story.append(Spacer(1, 0.2*inch))
            story.append(Image("attached_assets/GUI2_1752049449853.png", width=6*inch, height=3*inch))
        except:
            pass
    story.append(PageBreak())
    
    # Slide 6: Technical Specifications
    story.append(Paragraph("Tekhnicheskie kharakteristiki", heading_style))
    story.append(Paragraph("<b>II-freymvork:</b>", normal_style))
    story.append(Paragraph("• TensorFlow.js s modelyami Teachable Machine", bullet_style))
    story.append(Paragraph("• PoseNet dlya otslezhivaniya skeleta iz 17 tochek", bullet_style))
    story.append(Paragraph("• Lokalnoye khranilishche s IndexedDB dlya avtonomnogo ispolzovaniya", bullet_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Sovmestimost:</b>", normal_style))
    story.append(Paragraph("• Sovremennye brauzery s podderzhkoy WebRTC", bullet_style))
    story.append(Paragraph("• Optimizirovano dlya sovmestimosti s Windows", bullet_style))
    story.append(Paragraph("• Avtomaticheskoye szhatiye izobrazheniy dlya khraneniya", bullet_style))
    story.append(Paragraph("• Neskolko rezervnykh razresheniy kamery", bullet_style))
    story.append(PageBreak())
    
    # Slide 7: Easy Setup Process
    story.append(Paragraph("Prostoy protsess nastroyki", heading_style))
    story.append(Paragraph("1. <b>Obuchite model:</b> ispolzuyte Teachable Machine dlya sozdaniya modeli poz", normal_style))
    story.append(Paragraph("2. <b>Zagruzite fayly:</b> importiruyte model.json, metadata.json, weights.bin", normal_style))
    story.append(Paragraph("3. <b>Nastroyte pozy:</b> vyberite 1-7 poz i zagruzite etalonyne izobrazheniya", normal_style))
    story.append(Paragraph("4. <b>Nastroyte parametry:</b> ustanovite zvuk, zaderzhku i predpochteniya tochnosti", normal_style))
    story.append(Paragraph("5. <b>Nachnite raspoznavanie:</b> zapustite obnaruzhenie poz v realnom vremeni", normal_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("<font color='red'><b>Polnostyu avtonomno:</b> rabotaet polnostyu bez interneta posle pervonachalnoy nastroyki</font>", normal_style))
    story.append(PageBreak())
    
    # Slide 8: Advanced Features
    story.append(Paragraph("Rasshirennye funktsii", heading_style))
    story.append(Paragraph("<b>Kalibrovka rasstoyaniya:</b>", normal_style))
    story.append(Paragraph("• Avtomaticheskoye opredelenie rasstoyaniya polzovatelya ot kamery", bullet_style))
    story.append(Paragraph("• Obratnaya svyaz v realnom vremeni dlya optimalnogo pozitsionirovaniya (3-4 futa)", bullet_style))
    story.append(Paragraph("• Vizualye podskazki: zelenyy = idealno, krasnyy = otregulirovat rasstoyanie", bullet_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Upravlenie dannymi:</b>", normal_style))
    story.append(Paragraph("• Sokhranenie vsekh nastroyek i faylov modeli lokalno", bullet_style))
    story.append(Paragraph("• Funktsiya ochistki pamyati s podtverzhdeniem", bullet_style))
    story.append(Paragraph("• Avtosokhranenie dlya vybora poz i polzovatelskikh imen", bullet_style))
    story.append(Paragraph("• Postoyannye nastroyki mezhdu seansami brauzera", bullet_style))
    story.append(PageBreak())
    
    # Slide 9: Use Cases
    story.append(Paragraph("Sluchai ispolzovaniya", heading_style))
    story.append(Paragraph("• <b>Fitnes-trenirovki:</b> monitoring formy i tekhniki uprazhneniy", bullet_style))
    story.append(Paragraph("• <b>Praktika yogi:</b> rukovodstvo cherez posledovatelnosti poz s obratnoy svyazyu", bullet_style))
    story.append(Paragraph("• <b>Fizicheskaya terapiya:</b> otslezhivanie reabilitatsionnykh uprazhneniy", bullet_style))
    story.append(Paragraph("• <b>Sportivnoye trenerstvo:</b> analiz sportivnykh dvizheniy", bullet_style))
    story.append(Paragraph("• <b>Obrazovanie:</b> obuchenie pravilnoy osanke i dvizheniyu", bullet_style))
    story.append(Paragraph("• <b>Dostupnost:</b> vspomogatelnye tekhnologii dlya trenirovki dvizheniy", bullet_style))
    story.append(PageBreak())
    
    # Slide 10: Key Benefits
    story.append(Paragraph("Klyuchevye preimushchestva", heading_style))
    story.append(Paragraph("<b>Konfidentsialnost i bezopasnost:</b>", normal_style))
    story.append(Paragraph("• Nikakie dannye ne otpravlyayutsya na vneshnie servery", bullet_style))
    story.append(Paragraph("• Lokalnaya obrabotka obespechivaet konfidentsialnost", bullet_style))
    story.append(Paragraph("• Avtonomnaya funktsionalnost zashchishchaet polzovatelskie dannye", bullet_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Polzovatelskiy opyt:</b>", normal_style))
    story.append(Paragraph("• Mgnovennaya obratnaya svyaz so zvukovymi i vizualnymi podskazkami", bullet_style))
    story.append(Paragraph("• Nastraivaemaya slozhnost i vremya", bullet_style))
    story.append(Paragraph("• Chetkoe otslezhivanie progressa cherez posledovatelnosti poz", bullet_style))
    story.append(PageBreak())
    
    # Slide 11: Get Started Today!
    story.append(Paragraph("Nachnite segodnya!", heading_style))
    story.append(Paragraph("<b>Preobrazite svoy trenirovochnyy opyt s veb-prilozheniem raspoznavaniya poz</b>", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("✓ <b>Dostupno na Replit:</b> prostoye razvertyvanie i sovmestnoye ispolzovanie", normal_style))
    story.append(Paragraph("✓ <b>Otkrytyy iskhodnyy kod:</b> nastraivaemyy dlya vashikh nuzhd", normal_style))
    story.append(Paragraph("✓ <b>Bez ustanovki:</b> zapuskaetsya pryamo v vashem brauzere", normal_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("<b>Gotovo k ispolzovaniyu:</b>", normal_style))
    story.append(Paragraph("• Mgnovennoe razvertyvanie na Replit", bullet_style))
    story.append(Paragraph("• Podelites s vashey komandoy ili studentami", bullet_style))
    story.append(Paragraph("• Nastroyte dlya konkretnykh sluchaev ispolzovaniya", bullet_style))
    
    # Build PDF
    doc.build(story)
    print("Prezentatsiya PDF uspeshno sozdana!")
    print(f"PDF fayl sokhranyen: {filename}")
    
    return filename

if __name__ == "__main__":
    create_pdf_presentation_russian()
