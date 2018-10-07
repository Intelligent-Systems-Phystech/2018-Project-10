# Задача 10

## Постановка задачи
* **Название**: Сравнение нейросетевых и непрерывно-морфологических методов в задаче детекции текста (Text Detection).

* **Задача**: Automatically Detect Text in Natural Images.

* **Данные**: синтетические сгенерированные данные + подготовленная выборка фотографий + [COCO text dataset] + [Конкурс Avito 2014].

* **Литература**: [COCO benchmark], [One of a state-of-the-art architecture]

* **Базовой алгоритм**: [code] + морфологические методы, [Avito 2014 winner’s solution].

* **Решение**: Предлагается сравнить работы нескольких state-of-the-art алгоритмов, которым нужна обширная обучающая выборка, с морфологическими методы, требующие небольшого числа данных. Предлагается определить границы применимости тех или иных методов.

* **Новизна**: предложить алгоритм, основанный на использовании как нейросетевых, так и морфологических методов (решение задачи word detection).

* **Авторы**: И. Н. Жариков.

* **Эксперт**: Л. М. Местецкий (морфологические методы).

## Работа с репозиторием

[Link Review] - обзор литературы и её анализ. Для редактирования, запросите доступ. Редактировать могут только участники проекта и администрация.

<!-- Links -->

[COCO text dataset]:https://vision.cornell.edu/se3/coco-text-2/

[Конкурс Avito 2014]:http://www.machinelearning.ru/wiki/index.php?title=%D0%9A%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D1%81_Avito.ru-2014:_%D1%80%D0%B0%D1%81%D0%BF%D0%BE%D0%B7%D0%BD%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%BD%D0%BE%D0%B9_%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8_%D0%BD%D0%B0_%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F%D1%85

[COCO benchmark]:https://vision.cornell.edu/se3/wp-content/uploads/2016/01/1601.07140v1.pdf

[One of a state-of-the-art architecture]:https://vision.cornell.edu/se3/wp-content/uploads/2016/01/1601.07140v1.pdf

[code]:https://github.com/eragonruan/text-detection-ctpn

[Avito 2014 winner’s solution]:http://www.machinelearning.ru/wiki/images/f/f1/Avito.ru-2014_Ulyanov_presentation.pdf

[Link Review]:https://docs.google.com/document/d/1Gocn0x-FfYkD_L7ZLZdULxNTBfo25OMMKPBr2-otw-w/edit?usp=sharing