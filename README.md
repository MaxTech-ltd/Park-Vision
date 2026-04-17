# Park-Vision
Park Vision - это система которая следит за парковочными местами и определяет какое из них свободное какое нет.

# Отличия системы от существующих аналогов
1. Использование одной камеры для контроля сразу нескольких парковочных мест, в отличие от систем с датчиком на каждое место
2. Снижение количества оборудования и упрощение установки
3. Более низкая стоимость внедрения и обслуживания
4. Отсутствие необходимости вмешательства в покрытие парковки
5. Возможность быстрого масштабирования системы
6. Использование методов компьютерного зрения вместо отдельных сенсоров
7. Гибкость настройки под различные парковочные зоны

# Состав системы:
## Система включает следующие основные элементы:
1. Камера для съёмки парковочной зоны
2. Устройство обработки (компьютер или одноплатный модуль)
3. Программное обеспечение на Python с использованием OpenCV
4. Средство передачи данных (кабель или беспроводное соединение)
5. Интерфейс отображения результатов (экран, монитор или веб-интерфейс)

## Дополнительно могут использоваться:
1. источник питания;
2. крепление для камеры;
3. защитный корпус для работы на улице.

# Логика моей системы:
Системная логика проекта заключается в последовательной обработке информации от камеры до получения результата о занятости парковочных мест.

Сначала камера фиксирует парковочную зону и передаёт изображение на устройство обработки. Затем программа получает кадр и выделяет на нём заранее заданные области, соответствующие парковочным местам. После этого каждая область отдельно анализируется для определения наличия или отсутствия автомобиля.

На основе результатов анализа система принимает решение о состоянии каждого места: свободно оно или занято. Далее формируется итоговая информация, которая выводится пользователю в виде выделенных зон и общего количества свободных мест.

Таким образом, логика системы строится по схеме: получение изображения, обработка кадра, анализ парковочных зон, определение занятости и вывод результата.

# Перспективы:
Перспективы проекта связаны с повышением точности распознавания, расширением функционала и возможностью внедрения на реальные парковочные объекты.
Так же планируется внедрение в рабочую систему. На этот раз код бол на Python). 


# __

Park-Vision
Park Vision is a system that monitors parking spaces and determines which ones are free and which ones are not.

Differences between the system and existing analogues
1. Using a single camera to monitor multiple parking spaces at once, unlike systems with a sensor for each space
2. Reducing the amount of equipment and simplifying installation
3. Lower implementation and maintenance costs
4. No need to interfere with the parking lot's surface
5. The ability to quickly scale the system
6. Using computer vision methods instead of individual sensors
7. Flexibility of configuration for different parking areas

System composition:
The system includes the following main elements:
1. A camera for capturing the parking area
2. A processing device (computer or single-board module)
3. Python software using OpenCV
4. A data transfer medium (cable or wireless connection)
5. A result display interface (screen, monitor, or web interface

Additionally, the following can be used:
1. a power supply;
2. a camera mount;
3. a protective case for outdoor use.

The logic of my system:
The system logic of the project involves the sequential processing of information from the camera until the result is obtained about the occupancy of parking spaces.

First, the camera captures the parking area and transmits the image to the processing device. Then, the program receives the frame and selects the predefined areas corresponding to the parking spaces. After that, each area is analyzed separately to determine whether a car is present or not.

Based on the analysis results, the system makes a decision about the status of each location: whether it is free or occupied. Finally, the system generates a summary report that displays the allocated zones and the total number of available spaces.

The system's logic follows a straightforward process: capturing an image, processing the frame, analyzing the parking zones, determining occupancy, and presenting the results.

Prospects:
The prospects of the project are associated with increasing the accuracy of recognition, expanding the functionality and the possibility of implementation on real parking facilities.
It is also planned to implement in the working system. This time the code bol on the Python).

