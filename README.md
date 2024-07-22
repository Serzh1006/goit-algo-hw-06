**San-Diego/Chicago/Houston/New York/Detroit**  
За допомогою алгоритму BFS ми отримали перелік всіх вершин, проходячи від одного рівня до іншого. Тобто беремо вершину і дивимось на сусідні, виводимо їх і йдемо нижче так само зліва направо перераховуємо всі вершини.

**Chicago/New York/Houston/Detroit/San-Diego**  
Потім алгоритм DFS пройшов у глибину графа по кожній гілці починаючи від вершини Chicago. В цьому випадку с початку беремо початкову вершину і дивимось її зв'язки. Якщо ми можемо перейти до іншої ми переходимо до неї і так далі. Коли ми доходимо до вершини, у якої немає далі дітей, ми повертаємось до попередньої вершини і шукаємо інші вершини, які пов'язані з цією. Таким чином пройшовши по всіх вершинах алгоритм завершує роботу.

Різниця між ними в тому, що інколи нам потрібно просто подивитись всі вершини які є, а інколи задача стоїть в тому щоб продивитись зв'язки та визначити чи граф має якісь цикли, чи він є зв'язним чи ні. Різні методи для різних задач.
