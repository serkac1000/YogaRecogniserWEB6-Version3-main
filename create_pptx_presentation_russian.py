
#!/usr/bin/env python3
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import os

def create_pose_recognition_presentation_russian():
    # Create presentation object
    prs = Presentation()
    
    # Set slide layout
    title_slide_layout = prs.slide_layouts[0]  # Title slide
    bullet_slide_layout = prs.slide_layouts[1]  # Title and content
    
    # Define colors
    primary_color = RGBColor(0, 102, 204)  # Blue
    secondary_color = RGBColor(255, 153, 51)  # Orange
    
    # Slide 1: Title slide
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    
    title.text = "Веб-приложение распознавания поз"
    subtitle.text = "ИИ-система распознавания поз в реальном времени с поддержкой локальных моделей\n\nКоманда разработчиков Replit\n9 июля 2025"
    
    # Slide 2: What is pose recognition app?
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Что такое приложение распознавания поз?"
    tf = content.text_frame
    tf.text = "Распознавание поз в реальном времени с использованием веб-камеры"
    
    p = tf.add_paragraph()
    p.text = "Автономная функциональность - интернет не требуется после настройки"
    p = tf.add_paragraph()
    p.text = "Настраиваемые параметры для 1-7 поз"
    p = tf.add_paragraph()
    p.text = "Поддержка локальных моделей с интеграцией Teachable Machine"
    p = tf.add_paragraph()
    p.text = "Калибровка расстояния для оптимального позиционирования"
    p = tf.add_paragraph()
    p.text = "Звуковая обратная связь и визуальное руководство"
    
    # Slide 3: Core features
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Основные функции"
    tf = content.text_frame
    tf.text = "Система распознавания поз:"
    
    p = tf.add_paragraph()
    p.text = "• Поддержка 1-7 настраиваемых поз"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Оценка уверенности в реальном времени (порог 30-90%)"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Визуальное сравнение поз с эталонными изображениями"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Отслеживание скелета с 17 ключевыми точками"
    p.level = 1
    
    p = tf.add_paragraph()
    p.text = "Параметры настройки:"
    p = tf.add_paragraph()
    p.text = "• Регулируемая задержка распознавания (1-10 секунд)"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Пользовательские названия поз (редактируемые ярлыки)"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Переключатель звукового сигнала для обратной связи об успехе"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Калибровка расстояния с руководством в реальном времени"
    p.level = 1
    
    # Slide 4: GUI settings interface
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "GUI: Интерфейс настроек"
    tf = content.text_frame
    tf.text = "Ключевые особенности:"
    
    p = tf.add_paragraph()
    p.text = "• Загрузка локальных файлов модели (model.json, metadata.json, weights.bin)"
    p = tf.add_paragraph()
    p.text = "• Флажки выбора поз для 1-7 поз"
    p = tf.add_paragraph()
    p.text = "• Загрузка эталонных изображений для каждой позы"
    p = tf.add_paragraph()
    p.text = "• Управление звуком, задержкой и порогом точности"
    p = tf.add_paragraph()
    p.text = "• Руководство по калибровке расстояния"
    
    # Try to add image if it exists
    if os.path.exists("attached_assets/GUI1_1752049448296.png"):
        slide.shapes.add_picture("attached_assets/GUI1_1752049448296.png", 
                               Inches(1), Inches(3), Inches(8), Inches(4))
    
    # Slide 5: GUI recognition interface
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "GUI: Interfeys raspoznavaniya"
    tf = content.text_frame
    tf.text = "Funktsii v realnom vremeni:"
    
    p = tf.add_paragraph()
    p.text = "• Pryamaya translyatsiya s veb-kamery s obnaruzheniem poz"
    p = tf.add_paragraph()
    p.text = "• Otobrazenie tekushchey i ozhidaemoy pozy"
    p = tf.add_paragraph()
    p.text = "• Polosa uverennosti s tsvetovym kodirovaniem (zelenyy = pravilno, krasnyy = nepravilno)"
    p = tf.add_paragraph()
    p.text = "• Sravnenie s etalonnym izobrazheniem"
    p = tf.add_paragraph()
    p.text = "• Obnovlenie i vozvrat k nastroykam"
    
    # Try to add image if it exists
    if os.path.exists("attached_assets/GUI2_1752049449853.png"):
        slide.shapes.add_picture("attached_assets/GUI2_1752049449853.png", 
                               Inches(1), Inches(3), Inches(8), Inches(4))
    
    # Slide 6: Technical specifications
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Tekhnicheskie kharakteristiki"
    tf = content.text_frame
    tf.text = "II-freymvork:"
    
    p = tf.add_paragraph()
    p.text = "• TensorFlow.js s modelyami Teachable Machine"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• PoseNet dlya otslezhivaniya skeleta iz 17 tochek"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Lokalnoye khranilishche s IndexedDB dlya avtonomnogo ispolzovaniya"
    p.level = 1
    
    p = tf.add_paragraph()
    p.text = "Sovmestimost:"
    p = tf.add_paragraph()
    p.text = "• Sovremennye brauzery s podderzhkoy WebRTC"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Optimizirovano dlya sovmestimosti s Windows"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Avtomaticheskoye szhatiye izobrazheniy dlya khraneniya"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Neskolko rezervnykh razresheniy kamery"
    p.level = 1
    
    # Slide 7: Simple setup process
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Prostoy protsess nastroyki"
    tf = content.text_frame
    tf.text = "1. Obuchite model: ispolzuyte Teachable Machine dlya sozdaniya modeli poz"
    
    p = tf.add_paragraph()
    p.text = "2. Zagruzite fayly: importiruyte model.json, metadata.json, weights.bin"
    p = tf.add_paragraph()
    p.text = "3. Nastroyte pozy: vyberite 1-7 poz i zagruzite etalonyne izobrazheniya"
    p = tf.add_paragraph()
    p.text = "4. Nastroyte parametry: ustanovite zvuk, zaderzhku i predpochteniya tochnosti"
    p = tf.add_paragraph()
    p.text = "5. Nachnite raspoznavanie: zapustite obnaruzhenie poz v realnom vremeni"
    
    # Add note
    p = tf.add_paragraph()
    p.text = "\nPolnostyu avtonomno: rabotaet polnostyu bez interneta posle pervonachalnoy nastroyki"
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 0, 0)
    
    # Slide 8: Advanced features
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Rasshirennye funktsii"
    tf = content.text_frame
    tf.text = "Kalibrovka rasstoyaniya:"
    
    p = tf.add_paragraph()
    p.text = "• Avtomaticheskoye opredelenie rasstoyaniya polzovatelya ot kamery"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Obratnaya svyaz v realnom vremeni dlya optimalnogo pozitsionirovaniya (3-4 futa)"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Vizualye podskazki: zelenyy = idealno, krasnyy = otregulirovat rasstoyanie"
    p.level = 1
    
    p = tf.add_paragraph()
    p.text = "Upravlenie dannymi:"
    p = tf.add_paragraph()
    p.text = "• Sokhranenie vsekh nastroyek i faylov modeli lokalno"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Funktsiya ochistki pamyati s podtverzhdeniem"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Avtosokhranenie dlya vybora poz i polzovatelskikh imen"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Postoyannye nastroyki mezhdu seansami brauzera"
    p.level = 1
    
    # Slide 9: Use cases
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Случаи использования"
    tf = content.text_frame
    tf.text = "• Фитнес-тренировки: мониторинг формы и техники упражнений"
    
    p = tf.add_paragraph()
    p.text = "• Практика йоги: руководство через последовательности поз с обратной связью"
    p = tf.add_paragraph()
    p.text = "• Физическая терапия: отслеживание реабилитационных упражнений"
    p = tf.add_paragraph()
    p.text = "• Спортивное тренерство: анализ спортивных движений"
    p = tf.add_paragraph()
    p.text = "• Образование: обучение правильной осанке и движению"
    p = tf.add_paragraph()
    p.text = "• Доступность: вспомогательные технологии для тренировки движений"
    
    # Slide 10: Key benefits
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Klyuchevye preimushchestva"
    tf = content.text_frame
    tf.text = "Konfidentsialnost i bezopasnost:"
    
    p = tf.add_paragraph()
    p.text = "• Nikakie dannye ne otpravlyayutsya na vneshnie servery"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Lokalnaya obrabotka obespechivaet konfidentsialnost"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Avtonomnaya funktsionalnost zashchishchaet polzovatelskie dannye"
    p.level = 1
    
    p = tf.add_paragraph()
    p.text = "Polzovatelskiy opyt:"
    p = tf.add_paragraph()
    p.text = "• Mgnovennaya obratnaya svyaz so zvukovymi i vizualnymi podskazkami"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Nastraivaemaya slozhnost i vremya"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Chetkoe otslezhivanie progressa cherez posledovatelnosti poz"
    p.level = 1
    
    # Slide 11: Get started today!
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Nachnite segodnya!"
    tf = content.text_frame
    tf.text = "Preobrazite svoy trenirovochnyy opyt s veb-prilozheniem raspoznavaniya poz"
    tf.paragraphs[0].font.size = Pt(18)
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    
    p = tf.add_paragraph()
    p.text = "\nDostupno na Replit: prostoye razvertyvanie i sovmestnoye ispolzovanie"
    p.font.bold = True
    p = tf.add_paragraph()
    p.text = "Otkrytyy iskhodnyy kod: nastraivaemyy dlya vashikh nuzhd"
    p.font.bold = True
    p = tf.add_paragraph()
    p.text = "Bez ustanovki: zapuskaetsya pryamo v vashem brauzere"
    p.font.bold = True
    
    p = tf.add_paragraph()
    p.text = "\nGotovo k ispolzovaniyu:"
    p = tf.add_paragraph()
    p.text = "• Mgnovennoe razvertyvanie na Replit"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Podelites s vashey komandoy ili studentami"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "• Nastroyte dlya konkretnykh sluchaev ispolzovaniya"
    p.level = 1
    
    # Save presentation
    output_path = "attached_assets/Pose_Recognition_Presentation_Russian.pptx"
    prs.save(output_path)
    print("Prezentatsiya PowerPoint uspeshno sozdana!")
    print(f"PPTX fayl sokhranyen: {output_path}")
    
    return output_path

if __name__ == "__main__":
    create_pose_recognition_presentation_russian()
