
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
    story.append(Paragraph("Веб-приложение распознавания поз", title_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("ИИ-система распознавания поз в реальном времени", heading_style))
    story.append(Paragraph("с поддержкой локальных моделей", heading_style))
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("Команда разработчиков Replit", normal_style))
    story.append(Paragraph("9 июля 2025", normal_style))
    story.append(PageBreak())
    
    # Slide 2: What is Pose Recognition App?
    story.append(Paragraph("Что такое приложение распознавания поз?", heading_style))
    story.append(Paragraph("• Распознавание поз в реальном времени с использованием веб-камеры", bullet_style))
    story.append(Paragraph("• Автономная функциональность - интернет не требуется после настройки", bullet_style))
    story.append(Paragraph("• Настраиваемые параметры для 1-7 поз", bullet_style))
    story.append(Paragraph("• Поддержка локальных моделей с интеграцией Teachable Machine", bullet_style))
    story.append(Paragraph("• Калибровка расстояния для оптимального позиционирования", bullet_style))
    story.append(Paragraph("• Звуковая обратная связь и визуальное руководство", bullet_style))
    story.append(PageBreak())
    
    # Slide 3: Core Features
    story.append(Paragraph("Основные функции", heading_style))
    story.append(Paragraph("<b>Система распознавания поз:</b>", normal_style))
    story.append(Paragraph("• Поддержка 1-7 настраиваемых поз", bullet_style))
    story.append(Paragraph("• Оценка уверенности в реальном времени (порог 30-90%)", bullet_style))
    story.append(Paragraph("• Визуальное сравнение поз с эталонными изображениями", bullet_style))
    story.append(Paragraph("• Отслеживание скелета с 17 ключевыми точками", bullet_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Параметры настройки:</b>", normal_style))
    story.append(Paragraph("• Регулируемая задержка распознавания (1-10 секунд)", bullet_style))
    story.append(Paragraph("• Пользовательские названия поз (редактируемые ярлыки)", bullet_style))
    story.append(Paragraph("• Переключатель звукового сигнала для обратной связи об успехе", bullet_style))
    story.append(Paragraph("• Калибровка расстояния с руководством в реальном времени", bullet_style))
    story.append(PageBreak())
    
    # Slide 4: GUI Settings Interface
    story.append(Paragraph("GUI: Интерфейс настроек", heading_style))
    story.append(Paragraph("<b>Ключевые особенности:</b>", normal_style))
    story.append(Paragraph("• Загрузка локальных файлов модели (model.json, metadata.json, weights.bin)", bullet_style))
    story.append(Paragraph("• Флажки выбора поз для 1-7 поз", bullet_style))
    story.append(Paragraph("• Загрузка эталонных изображений для каждой позы", bullet_style))
    story.append(Paragraph("• Управление звуком, задержкой и порогом точности", bullet_style))
    story.append(Paragraph("• Руководство по калибровке расстояния", bullet_style))
    
    # Try to add image if it exists
    if os.path.exists("attached_assets/GUI1_1752049448296.png"):
        try:
            story.append(Spacer(1, 0.2*inch))
            story.append(Image("attached_assets/GUI1_1752049448296.png", width=6*inch, height=3*inch))
        except:
            pass
    story.append(PageBreak())
    
    # Slide 5: GUI Recognition Interface
    story.append(Paragraph("GUI: Интерфейс распознавания", heading_style))
    story.append(Paragraph("<b>Функции в реальном времени:</b>", normal_style))
    story.append(Paragraph("• Прямая трансляция с веб-камеры с обнаружением поз", bullet_style))
    story.append(Paragraph("• Отображение текущей и ожидаемой позы", bullet_style))
    story.append(Paragraph("• Полоса уверенности с цветовым кодированием (зеленый = правильно, красный = неправильно)", bullet_style))
    story.append(Paragraph("• Сравнение с эталонным изображением", bullet_style))
    story.append(Paragraph("• Обновление и возврат к настройкам", bullet_style))
    
    # Try to add image if it exists
    if os.path.exists("attached_assets/GUI2_1752049449853.png"):
        try:
            story.append(Spacer(1, 0.2*inch))
            story.append(Image("attached_assets/GUI2_1752049449853.png", width=6*inch, height=3*inch))
        except:
            pass
    story.append(PageBreak())
    
    # Slide 6: Technical Specifications
    story.append(Paragraph("Технические характеристики", heading_style))
    story.append(Paragraph("<b>ИИ-фреймворк:</b>", normal_style))
    story.append(Paragraph("• TensorFlow.js с моделями Teachable Machine", bullet_style))
    story.append(Paragraph("• PoseNet для отслеживания скелета из 17 точек", bullet_style))
    story.append(Paragraph("• Локальное хранилище с IndexedDB для автономного использования", bullet_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Совместимость:</b>", normal_style))
    story.append(Paragraph("• Современные браузеры с поддержкой WebRTC", bullet_style))
    story.append(Paragraph("• Оптимизировано для совместимости с Windows", bullet_style))
    story.append(Paragraph("• Автоматическое сжатие изображений для хранения", bullet_style))
    story.append(Paragraph("• Несколько резервных разрешений камеры", bullet_style))
    story.append(PageBreak())
    
    # Slide 7: Easy Setup Process
    story.append(Paragraph("Простой процесс настройки", heading_style))
    story.append(Paragraph("1. <b>Обучите модель:</b> используйте Teachable Machine для создания модели поз", normal_style))
    story.append(Paragraph("2. <b>Загрузите файлы:</b> импортируйте model.json, metadata.json, weights.bin", normal_style))
    story.append(Paragraph("3. <b>Настройте позы:</b> выберите 1-7 поз и загрузите эталонные изображения", normal_style))
    story.append(Paragraph("4. <b>Настройте параметры:</b> установите звук, задержку и предпочтения точности", normal_style))
    story.append(Paragraph("5. <b>Начните распознавание:</b> запустите обнаружение поз в реальном времени", normal_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("<font color='red'><b>Полностью автономно:</b> работает полностью без интернета после первоначальной настройки</font>", normal_style))
    story.append(PageBreak())
    
    # Slide 8: Advanced Features
    story.append(Paragraph("Расширенные функции", heading_style))
    story.append(Paragraph("<b>Калибровка расстояния:</b>", normal_style))
    story.append(Paragraph("• Автоматическое определение расстояния пользователя от камеры", bullet_style))
    story.append(Paragraph("• Обратная связь в реальном времени для оптимального позиционирования (3-4 фута)", bullet_style))
    story.append(Paragraph("• Визуальные подсказки: зеленый = идеально, красный = отрегулировать расстояние", bullet_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Управление данными:</b>", normal_style))
    story.append(Paragraph("• Сохранение всех настроек и файлов модели локально", bullet_style))
    story.append(Paragraph("• Функция очистки памяти с подтверждением", bullet_style))
    story.append(Paragraph("• Автосохранение для выбора поз и пользовательских имен", bullet_style))
    story.append(Paragraph("• Постоянные настройки между сеансами браузера", bullet_style))
    story.append(PageBreak())
    
    # Slide 9: Use Cases
    story.append(Paragraph("Случаи использования", heading_style))
    story.append(Paragraph("• <b>Фитнес-тренировки:</b> мониторинг формы и техники упражнений", bullet_style))
    story.append(Paragraph("• <b>Практика йоги:</b> руководство через последовательности поз с обратной связью", bullet_style))
    story.append(Paragraph("• <b>Физическая терапия:</b> отслеживание реабилитационных упражнений", bullet_style))
    story.append(Paragraph("• <b>Спортивное тренерство:</b> анализ спортивных движений", bullet_style))
    story.append(Paragraph("• <b>Образование:</b> обучение правильной осанке и движению", bullet_style))
    story.append(Paragraph("• <b>Доступность:</b> вспомогательные технологии для тренировки движений", bullet_style))
    story.append(PageBreak())
    
    # Slide 10: Key Benefits
    story.append(Paragraph("Ключевые преимущества", heading_style))
    story.append(Paragraph("<b>Конфиденциальность и безопасность:</b>", normal_style))
    story.append(Paragraph("• Никакие данные не отправляются на внешние серверы", bullet_style))
    story.append(Paragraph("• Локальная обработка обеспечивает конфиденциальность", bullet_style))
    story.append(Paragraph("• Автономная функциональность защищает пользовательские данные", bullet_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Пользовательский опыт:</b>", normal_style))
    story.append(Paragraph("• Мгновенная обратная связь со звуковыми и визуальными подсказками", bullet_style))
    story.append(Paragraph("• Настраиваемая сложность и время", bullet_style))
    story.append(Paragraph("• Четкое отслеживание прогресса через последовательности поз", bullet_style))
    story.append(PageBreak())
    
    # Slide 11: Get Started Today!
    story.append(Paragraph("Начните сегодня!", heading_style))
    story.append(Paragraph("<b>Преобразите свой тренировочный опыт с веб-приложением распознавания поз</b>", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("✓ <b>Доступно на Replit:</b> простое развертывание и совместное использование", normal_style))
    story.append(Paragraph("✓ <b>Открытый исходный код:</b> настраиваемый для ваших нужд", normal_style))
    story.append(Paragraph("✓ <b>Без установки:</b> запускается прямо в вашем браузере", normal_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("<b>Готово к использованию:</b>", normal_style))
    story.append(Paragraph("• Мгновенное развертывание на Replit", bullet_style))
    story.append(Paragraph("• Поделитесь с вашей командой или студентами", bullet_style))
    story.append(Paragraph("• Настройте для конкретных случаев использования", bullet_style))
    
    # Build PDF
    doc.build(story)
    print("Презентация PDF успешно создана!")
    print(f"PDF файл сохранен: {filename}")
    
    return filename

if __name__ == "__main__":
    create_pdf_presentation_russian()
