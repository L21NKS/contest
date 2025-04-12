# Три модуля яндекс контеста
# М1
## A. Бинарный поиск
Ограничение времени	1 секунда
Ограничение памяти	64.0 Мб
Ввод	стандартный ввод
Вывод	стандартный вывод
Реализуйте рекурсивно алгоритм бинарного поиска. Реализация алгоритма должна быть инкапуслирована, т.е. не зависеть от форматов входных/выходных данных и непосредственно ввода/вывода.

Формат ввода
Ввод осуществляется со стандартного потока ввода. Первая строка всегда содержит отсортированный массив, в котором должен производится поиск. Остальные строки имеют формат search K, где K - некоторое число.

Формат вывода
Результат поиска - первый индекс числа в массиве. Если число в массиве отсутствует, то результатом будет -1. Результат работы программы выводится в стандартный поток вывода.


## B. Двунаправленная очередь
Ограничение времени	1 секунда
Ограничение памяти	64.0 Мб
Ввод	стандартный ввод
Вывод	стандартный вывод
Реализуйте дек (двунаправленную очередь), используя только массив.

Формат ввода
На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируются. Первая строка всегда содержит "set_size N", где N - максимальный размер дека, целое число. Каждая последующая строка содержит ровно одну команду: pushf X, pushb X, popf, popb или print, где X - произвольная строка без пробелов.

Формат вывода
Результат работы программы выводится в стандартный поток вывода и зависит от команды.

Команда print выводит содержимое дека одной строкой, значения разделяются пробелами. Если дек пуст, то выводится "empty".
Команда pushb добавляет элемент в конец дека.
Команда pushf добавляет элемент в начало дека.
Команда popf извлекает и выводит первый элемент или "underflow", если дек пуст.
Команда popb извлекает и выводит последний элемент или "underflow", если дек пуст.
В любой непонятной ситуации результатом работы любой команды будет "error".

## C. Обход графа
Ограничение времени	1 секунда
Ограничение памяти	64.0 Мб
Ввод	стандартный ввод
Вывод	стандартный вывод
Реализуйте обход графа в ширину и глубину.

Формат ввода
Первая строка стандартного потока ввода данных имеет формат "graph_type start_vertex search_type", где

"graph_type" - тип графа, ориентированный ('d') или неориентированный ('u');
"start_vertex" - идентификатор вершины, с которой начинать обход графа;
"search_type" - тип обхода, в ширину ('b') или в глубину ('d').
Каждая последующая строка содержит ребро, которая представляет собой идентификаторы начальной и конечной вершины, разделенные пробелом.

Формат вывода
Результат работы программы выводится в стандартный поток вывода. Идентификаторы посещенных вершин выводятся по одному в строке в порядке обхода.

# M2
## A. Двоичное дерево поиска
Ограничение времени	1 секунда
Ограничение памяти	64.0 Мб
Ввод	стандартный ввод
Вывод	стандартный вывод
Реализуйте двоичное дерево поиска. Реализация самой структуры данных должна быть инкапуслирована, т.е. не зависеть от форматов входных/выходных данных и непосредственно ввода/вывода.

Тесты предполагают левостороннюю реализацию, т.е. если действие можно реализовать двумя симметричными способами, надо делать тот, который больше использует левую сторону.

Формат ввода
На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируются. Каждая строка содержит ровно одну команду: add K V, set K V, delete K, search K, min, max или print, где K - целое число (64 бита вам хватит), ключ, V - произвольная строка без пробелов (значение).

Команда add добавляет значение V в дерево по ключу K;
Команда set изменяет значение по ключу K на V;
Команда delete удаляет вершину с ключом K;
Команда search ищет значение по ключу K;
Команды min и max находят ключ и значение вершины, с наименьшим/наибольшим ключом;
Команда print выводит все дерево целиком.
Формат вывода
Результат работы программы выводится в стандартный поток вывода и зависит от команды.

Команда search выводит либо "1 V", либо "0", где V - значение для найденного ключа;
Команды min и max выводят "K V", где K - минимальный или максимальный ключ дерева соответственно, V - значение по этому ключу;
При вызове команды print дерево выводится строго по уровням, слева направо, 1 строка - 1 уровень. Первая строка содержит только корень дерева в формате "[K V]" или "_", если дерево пустое. Каждая последующая строка содержит один уровень дерева. Вершины выводятся в формате "[K V P]", где P - ключ родительской вершины. Если вершина отсутствует, ставится "_". Вершины разделены пробелом.
В любой непонятной ситуации результатом работы любой команды будет "error".

## B. Косое дерево
Ограничение времени	1 секунда
Ограничение памяти	64.0 Мб
Ввод	стандартный ввод
Вывод	стандартный вывод
Реализуйте косое дерево. Реализация самой структуры данных должна быть инкапуслирована, т.е. не зависеть от форматов входных/выходных данных и непосредственно ввода/вывода.

Тесты предполагают левостороннюю реализацию, т.е. если действие можно реализовать двумя симметричными способами, надо делать тот, который больше использует левую сторону.

Формат ввода
На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируются. Каждая строка содержит ровно одну команду: add K V, set K V, delete K, search K, min, max или print, где K - целое число (64 бита вам хватит), ключ, V - произвольная строка без пробелов (значение).

Команда add добавляет значение V в дерево по ключу K;
Команда set изменяет значение по ключу K на V;
Команда delete удаляет вершину с ключом K;
Команда search ищет значение по ключу K;
Команды min и max находят ключ и значение вершины, с наименьшим/наибольшим ключом;
Команда print выводит все дерево целиком.
Формат вывода
Результат работы программы выводится в стандартный поток вывода и зависит от команды.

Команда search выводит либо "1 V", либо "0", где V - значение для найденного ключа;
Команды min и max выводят "K V", где K - минимальный или максимальный ключ дерева соответственно, V - значение по этому ключу;
При вызове команды print дерево выводится строго по уровням, слева направо, 1 строка - 1 уровень. Первая строка содержит только корень дерева в формате "[K V]" или "_", если дерево пустое. Каждая последующая строка содержит один уровень дерева. Вершины выводятся в формате "[K V P]", где P - ключ родительской вершины. Если вершина отсутствует, ставится "_". Вершины разделены пробелом.
В любой непонятной ситуации результатом работы любой команды будет "error".

## C. Куча
Ограничение времени	1 секунда
Ограничение памяти	64.0 Мб
Ввод	стандартный ввод
Вывод	стандартный вывод
Реализуйте двоичную min-кучу. Модифицируйте ее таким образом, чтобы внутреннее ее строение было таким же, но при этом доступ по ключу к любому элементу осуществлялся в среднем за константное время. Реализация самой структуры данных должна быть инкапуслирована, т.е. не зависеть от форматов входных/выходных данных и непосредственно ввода/вывода.

Формат ввода
На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируются. Каждая строка содержит ровно одну команду: add K V, set K V, delete K, search K, min, max, extract или print, где K - целое число (64 бита вам хватит), ключ, V - произвольная строка без пробелов (значение).

Команда add добавляет значение V в кучу по ключу K;
Команда set изменяет значение по ключу K на V;
Команда delete удаляет вершину с ключом K;
Команда search ищет значение и индекс по ключу K;
Команда extract извлекает корень кучи;
Команды min и max находят ключ, значение и индекс вершины, с наименьшим/наибольшим ключом;
Команда print выводит всю кучу целиком.
Формат вывода
Результат работы программы выводится в стандартный поток вывода и зависит от команды.

Команда search выводит либо "1 I V", либо "0", где I - индекс, V - значение для найденного ключа;
Команды min и max выводят "K I V", где K - минимальный или максимальный ключ кучи соответственно, I - индекс, V - значение по этому ключу; *Команда extract извлекает корень кучи и выводит "K V", где K, V - ключ и значение извлеченного элемента;
При вызове команды print куча выводится строго по уровням, слева направо, 1 строка - 1 уровень. Первая строка содержит только корень дерева в формате "[K V]" или "_", если дерево пустое. Каждая последующая строка содержит один уровень дерева. Вершины выводятся в формате "[K V P]", где P - ключ родительской вершины. Если вершина отсутствует, ставится "_". Вершины разделены пробелом.
В любой непонятной ситуации результатом работы любой команды будет "error".

# M3
## A. Блокировка логина
Ограничение времени: 1 секунда
Ограничение памяти: 64Mb
Ввод: стандартный ввод
Вывод: стандартный вывод

Реализуйте алгоритм, который на основе истории неуспешных попыток логина пользователя в систему блокирует ему доступ. Пользователь блокируется на некоторый период времени 
𝐵 
B в случае нескольких неуспешных попыток входа 
𝑁
N в течение определённого интервала времени 
𝑃
P.

Блокировка начинается сразу после последней неудачной попытки логина. В случае, если пользователь уже был недавно заблокирован, то время повторной блокировки удваивается за каждую блокировку, т.е. растёт экспоненциально. При этом время блокировки ограничено сверху некоторым периодом 
𝐵
𝑚
𝑎
𝑥
B 
max
​
 . При расчётах учитываются все попытки за период 
2
⋅
𝐵
𝑚
𝑎
𝑥
2⋅B 
max
​
 .

В примере ниже, если пользователь совершит 5 неуспешных попыток в течение часа, то он должен быть заблокирован на 2 часа. Если после окончания блока он еще раз не сможет залогиниться за 5 попыток в течение часа, то он будет заблокирован уже на 4 часа, потом на 8 и т.д., но не более чем на 30 дней.

Формат ввода
В первой строке стандартного потока записаны через пробел параметры задачи: количество попыток 
𝑁
N, интервал 
𝑃
P в секундах, начальное время блокировки 
𝐵
B в секундах, максимальное время блокировки 
𝐵
𝑚
𝑎
𝑥
B 
max
​
  в секундах и текущее Unix-время.

Каждая последующая строка содержит Unix-время неудачной попытки логина пользователя.

Все параметры и времена — целые неотрицательные числа.

Формат вывода
Вывод должен содержать Unix-время окончания блокировки пользователя или ok, если пользователя не надо блокировать или время его блокировки истекло. Результат работы программы выводится в стандартный поток вывода.

## B. Фильтр Блума
Ограничение времени: 1 секунда
Ограничение памяти: 64Mb
Ввод: стандартный ввод
Вывод: стандартный вывод

Реализуйте фильтр Блума, позволяющий дать быстрый, но вероятностный ответ, присутствует ли объект в коллекции. Реализация самой структуры данных должна быть инкапсулирована, т.е. не зависеть от форматов входных/выходных данных и непосредственно ввода/вывода.

Реализация битового массива также должна быть инкапсулирована. Массив битов должен быть эффективно расположен в памяти. Параметрами структуры данных являются 
𝑛 n — приблизительное количество элементов (целое), 𝑃 P — вероятность ложноположительного ответа.

Размер структуры, 𝑚 m, вычисляется как 𝑚=𝑛⋅log2𝑃/ln2m=n⋅log 2
​
 P/ln2, а количество хэш-функций — как 𝑘=−log⁡2𝑃 k=−log 2P.
 Оба значения округляются до ближайшего целого.

В качестве семейства функций используйте семейство хэш-функций вида ℎ𝑖(𝑥)=(((𝑖+1)⋅(𝑥+𝑝𝑖+1))mod
 
 
𝑀
)
m
o
d
 
 
𝑚
h 
i
​
 (x)=(((i+1)⋅(x+p 
i+1
​
 ))modM)modm,
где 
𝑥
x — ключ, 
0
≤
𝑖
≤
𝑘
−
1
0≤i≤k−1 — номер хэш-функции, 
𝑝
𝑖
p 
i
​
  — i-е простое число, а 
𝑀
M — 31-ое число Мерсенна.
Формат ввода

На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируются.

Первая строка содержит команду вида set n P. Каждая последующая строка содержит ровно одну команду: add K, search K или print, где K — неотрицательное число (64 бита вам хватит), ключ.

Команда set инициализирует структуру и выводит вычисленные параметры в формате "m k";

Команда add добавляет в структуру ключ K;

Команда search выводит либо "1", если элемент возможно присутствует в структуре, либо "0", если он там отсутствует;

Команда print выводит внутреннее состояние структуры — последовательность из 0 и 1, не разделённую пробелами.

Формат вывода

Результат работы программы выводится в стандартный поток вывода. В любой непонятной ситуации результатом работы любой команды будет "error"

## C. Приближенный рюкзак
<img width="498" alt="image" src="https://github.com/user-attachments/assets/5a4fcc45-6d76-4e92-ac89-c3083b156ca9" />
<img width="499" alt="image" src="https://github.com/user-attachments/assets/abfbd2ca-a1d3-4cfb-8d57-74beebb60888" />





