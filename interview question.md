### Меры центральной тенденцию и меры изменчивости

#### 0. 
  
#### 1. В чём разница между средним и медианой?

#### 2. Когда предпочтительнее использовать среднее? А когда медиану?

#### 3. Что такое мода? Чем она отличается от медианы?

#### 4. Назовите известые вам меры центральной тенденции? И в чем между ними разница?

#### 5. Что такое меры изменчивости? Назовите известные вам меры.  
  Дисперсия. Стандартное отклонение. Межквартильный размах. Коэффицент вариации.  

#### 5. Что такое дисперсия? А какие у неё есть свойства?

  * Свойства дисперсии:  
    * Если значения измеренного признака не отличаются друг от друга (равны между собой),  
      дисперсия равна нулю.  
    * Прибавление одного и того же числа к каждому значению переменной не меняет дисперсию.  
      Прибавление константы к каждому значению переменной сдвигает график распределения этой  
      переменной на эту константу (меняется среднее), но изменчивость (дисперсия) при  
      этом остается неизменной.  
    * Умножение каждого значения переменной на константу с изменяет дисперсию в с² раз.  
    * При объединении двух выборок с одинаковой дисперсией, но с разными средними  
      значениями дисперсия увеличивается.

#### 6. Что такое стандратное отклонение?

#### 7. Квартиль, квантиль, дециль, перцентиль и другие фантастические твари

#### 8. А что такое меры центральной тенденции?
  * Число характеризрующее выборку по уровню выраженности измеренного признака.
  * 

#### 9.

### ЦПТ и нормальное распределение

#### 1. Что такое ЦПТ?

#### 3. Следствия из ЦПТ

Следствием из ЦПТ явлются следующие свойства:  
- Если мы многократно извлекаем выборки размера n и вычисляем среднее значение для  
  каждой выборки, то распределение этих средних значений будет приближаться к  
  нормальному распределению;  
- Среднее значение этого распределения будет практически совпадать со средним значением  
  генеральной совокупности (μ);  
- А стандартное отклонение распределения выборочных средних (σ​) будет меньше стандартного  
  отклонения генеральной совокупности (σ), причем в корень из n раз!  

#### 2. Какие свойства нормального распределения вы знаете?

#### 3. Какие виды распределений существуют? 

#### 4. Расскажите о правиле 2/3 сигм

#### 5. 

#### .

### AB TESTs

#### 1. Что такое Pvalue?
  
  * Как оно распределено когда есть эффект? А когда эффекта нет (синтетический А/А)? 

#### 2. Что такое доверительный интервал?

#### 3. Ошибки 1 и 2 рода

#### 4. Почему 5% уровень значимости? Можно ли другой?

#### 5. Каого размера выборка нужна?

#### 6. Как долго проводить эксперимент?

#### 7. Почему нельзя запустить эксперимент и ждать пока из вариантов не будет значимее?

#### 8. Каким стат.критерием будем пользоваться? Почему им? 

#### 9. Какие стат.критерии вы знаете?

#### 10. MDE
  * Что будет если реальный эффект >, = , < **MDE**?
      * Если больше то хорошо - мы обнаружим эффект
      * Если = то вероятность ошибки 2 рода равна той которую мы ожидаем
      * Если < то вероятность ошибки 2 рода больше и эффект не обнаружим
        (почему ошибка 2 рода?)
  * Сколько нужно пользотателей чтобы задетектить эффект в 10р? Известно  
    что для нахождения различия в 5р нам нужно 100 000 пользователей.  
      * Чем больше эффект, тем меньше нужна выборка. В 4 раза т.е. 25 000.
  
#### 11. Что такое сетевой эффект? Какие методы борьбы с ним вы знаете?

#### 12. Что такое каннибализция?

#### 13. Что такое статистический критерий? 

#### 14. Допустим мы провели эксперимент и получили значения для A и B групп. Чтобы проверить гипотезу о равенстве средних с помощью бутстрепа, что нужно сделать
1) Сгенерировать две подвыборки, одну из значений контрольной группы, вторую из  
   значений экспериментальной группы;  
2) Посчитать статистику по значениям подвыборок. В случае проверки гипотезы о равенстве  
   средних, статистика — разница средних значений подвыборок;  
3) Повторить первые два шага 1000 раз, получим 1000 оценок разницы средних;  
4) По полученным значениям построить доверительный интервал;  
5) Проверить значимость отличий: ноль находится вне доверительного интервала —  
   отличия статистически значимы, иначе — нет.

#### 15. Что такое стат. мощность? 

#### 16. Что такое уровень значимости?

#### 17. Какие риски возникают при многократном А/В тестировании?
  Многократные тесты увеличивают вероятность ошибки типа I (ложноположительные результаты).  
  Это может быть исправлено с использованием коррекции на множественные проверки, например,  
  методом Бонферрони или контролем False Discovery Rate (FDR).  
  Также важно фиксировать количество тестов заранее, чтобы избежать искривления результатов.  

### Общие вопросы

#### 0. Чему равняется матожидание константы?
  Самой константе

#### 1. Что такое мультиколлинеарность? Как с ней бороться?

#### 2. Какие типы метрик бывают?
  
  Количественные  
  Конверсия  
  Метрики отношения  
  
#### 3. Мы выбрали альфу = 0.05. Провели 1000 экспериментов. В каком числе экспов мы увидим стат.значимое различие?
  В 50.

#### 4. Что такое бутстреп? Какие его плюсы и минусы?

#### 5. Корреляция VS причинность. Почему это не одно и тоже.

#### 6. Какие есть подходы к принятию решений?

  1) HiPPO (the highest paid person’s opinion) — мнение самого высокооплачиваемого человека.  
     Это позволяет принимать решения быстро, что может быть полезно на ранних стадиях развития,  
     когда важна скорость и нет возможности провести более детальный анализ. Однако, такой  
     подход обладает низкой точностью, так как мнение одного человека не может учитывать  
     всех нюансов и особенностей поведения клиентов.  
     
  3) Сбор информации непосредственно от клиентов. Можно провести опрос или пригласить людей  
     на интервью для сбора мнений о наших идеях. Этот способ тоже довольно быстрый, поскольку  
     провести опрос или организовать интервью можно за пару дней.  
     Тут мы не опираемся на мнение одного человека, а смотрим на ответы наших клиентов,  
     что может привести к более взвешенному решению. Несмотря на это, нужно понимать, что мы  
     используем мнения людей, которые могут отличаться от их реального поведения.  
   
  5) A/B тестирование — наиболее точный способ принятия решений, но в то же время наиболее  
     трудозатратный, так как требует усилий для проведения эксперимента и анализа результатов.  

#### 7. Какие методы поиска выбросов вы знаете?
  1. Расчет границ межквартильного размаха. Все, что не попадает в его границы - выбросы.  
     Межквартильный размах (IQR) является мерой статистической дисперсии, равной разнице  
     между 75-м и 25-м процентилями или между верхним и нижним квартилями, IQR = Q3 - Q1.  

  2. IsolationForest  
     IsolationForest - это алгоритм обнаружения аномалий с обучением ансамблю, который  
     особенно полезен при обнаружении выбросов в наборах данных большой размерности.  

  3. DBSCAN 
     Пространственная кластеризация приложений с шумом на основе плотности  
     (или, проще говоря, DBSCAN) на самом деле является неконтролируемым алгоритмом  
     кластеризации, как и KMeans. Однако одно из его применений - это также возможность  
     обнаруживать выбросы в данных.
     
  [details](https://skine.ru/articles/185838/)

#### . Какие есть типы переменных? 
  **Количественные** – измеряемое (например, рост);    
  **Непрерывные** – переменная принимает любое значение на опр. промежутке;  
  **Дискретные** – только определенные значения (3.5 ребенка в семье не будет).  
  **Номинативные** (= качественные) – разделение испытуемых на группы, цифры как  
  маркеры (например: 1 -женщины, 2 – мужчины). Цифры как имена групп, не для расчетов.  
  **Ранговые** – похоже на номинативные, только возможны сравнения (быстрее/медленнее и т.п.)  


###  Немного матстата.

#### 1. Что такое случайная величина?

#### 2. Что такое функции случайной величиы?

#### 3. Что такое плотность распределения случайной величины?

#### 4.

#### .

#### .

###  Немного носков.

#### . В коробке 7 красных, 14 зеленых и 21 синий носков.
1. Какое минимальное количество носков нужно вытянуть наугад чтобы гарантированно  
   образовалась одна пара одного цвета?  
2. Какое минимально количество носков нужно вытягуть наугад чтобы в итоге гарантированно  
   получилось три разных?
1. Вытаскиваем 3 носка, а 4ый гарантированно будет из тех цветов, которые уже имеем.  
2. Аналогично, можем вытянуть 14 зеленых и 21 синий (35 в сумме). Следующий носок – уже красный.  
   
