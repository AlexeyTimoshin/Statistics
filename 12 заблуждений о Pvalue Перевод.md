Pvalue - это мера статистического доказательства, которая используется практически во  
всех медицинских исследованиях. Его интерпретация чрезвычайно сложна, поскольку он не  
является частью какой-либо формальной системы статистических выводов. В результате  
логическое значение Pvalue широко и часто совершенно неверно истолковывается, на  
что указывалось в бесчисленных статьях и книгах, появляющихся по крайней мере с 1940-х  
годов. В этом комментарии рассматривается дюжина таких распространенных неправильных  
толкований и объясняется, почему каждое из них неверно. В нем также рассматриваются  
возможные последствия такого неправильного понимания или представления его значения.  
Наконец, он сравнивает Pvalue с его байесовским аналогом, коэффициентом Байеса, который  
обладает практически всеми желательными свойствами доказательной меры, которых не хватает  
Pvalue, в первую очередь возможностью интерпретации. Наиболее серьезным последствием этого  
массива ошибочных представлений о Pvalue является ложное убеждение в том, что вероятность  
ошибочного вывода может быть вычислена на основе данных одного эксперимента, без ссылки на  
внешние доказательства или правдоподобие лежащего в его основе механизма.  

Pvalue, вероятно, является наиболее распространенным и в то же время неправильно понимаемым и  
иногда неправильно рассчитываемым показателем во всех биомедицинских исследованиях.  
В недавнем опросе ординаторов, опубликованном в JAMA, 88% опрошенных выразили почти полную  
уверенность в интерпретации Pvalue, однако только 62% из них смогли правильно ответить на  
элементарный вопрос об интерпретации Pvalue. Однако не только эти статистические данные  
свидетельствуют о сложности интерпретации Pvalue. По иронии судьбы, ни один из предложенных  
ответов на вопрос о Pvalue не был правильным, как мы выясним далее.  

Статьи о Pvalue, по-видимому, едва ли могут пробить брешь в горе заблуждений; в  
биомедицинской литературе уже по меньшей мере 70 лет появляются статьи, предупреждающие исследова  
телей о минном поле для интерпретации Pvalue, однако эти уроки, похоже, либо не читаются, либо  
игнорируются, либо им не верят, либо забываются с каждой новой волной группа исследователей знакомится  
с совершенно новым техническим лексиконом медицинских исследований.  

Исследователи не виноваты в том, что Pvalue трудно правильно интерпретировать. Человек, который ввел  
его в качестве формального исследовательского инструмента, статистик и генетик Р.А. Фишер,  
не смог точно объяснить его логический смысл. Он предложил довольно неформальную систему, которую  
можно было использовать, но он так и не смог прямо описать, что она означает с точки зрения  
логического вывода. В системе Фишера Pvalue должно было использоваться как приблизительный числовой  
анализ силы доказательств против нулевой гипотезы. В нем не упоминалось о “частоте ошибок” или 
“отклонении” гипотезы; предполагалось, что это инструмент доказательства, который можно гибко использовать  
в контексте конкретной проблемы.  

Фишер предложил использовать термин “значительный” применительно к малым Pvalue, и выбор   
этого конкретного слова был вполне осознанным. Значение, которое он имел в виду, было довольно  
близко к общепринятому языковому толкованию этого слова, что заслуживает внимания. 
В своей чрезвычайно влиятельной работе "Статистические методы для научных работников" -  
первое современное статистическое руководство, которым руководствовались поколения исследователей в  
области биомедицины, - он сказал:  
```
    Лично автор предпочитает устанавливать низкий уровень значимости на уровне 5% ....  
    Научный факт следует рассматривать как экспериментально установленный только в том случае,  
    если правильно спланированный эксперимент редко не дает такого уровня значимости
```

Другими словами, практический смысл Pvalue, меньшего, чем 0,05, заключался в том, что  
необходимо повторить эксперимент. Если последующие исследования также показали значимые  
Pvalue, можно было бы заключить, что наблюдаемые эффекты вряд ли были результатом одной лишь  
случайности. Таким образом, “значимость” - это всего лишь то, что достойно внимания в форме  
проведения дополнительных экспериментов, но не доказательство само по себе.  

История с Pvalue, какой бы тонкой она ни была в самом начале, стала несравнимо сложнее с  
внедрением механизма “проверки гипотез”, лежащего в основе современной практики.  
Проверка гипотез включает в себя нулевую и альтернативную гипотезы, “принятие и отклонение”  
гипотез типа I и II “частота ошибок”, “мощность” и другие связанные с этим понятия. Несмотря  
на то, что сегодня мы используем Pvalue в контексте этой системы тестирования, брак нельзя  
назвать комфортным, и многие неправильные представления, которые мы рассмотрим, проистекают из  
этого неестественного союза.  
Здесь мы сосредоточимся на неправильных представлениях о том, как следует интерпретировать Pvalue.  

Pvalue определяется следующим образом — на словах: вероятность наблюдаемого результата плюс  
более экстремальные результаты, если нулевая гипотеза верна; в алгебраической записи: 

$$P \left (X\ \geq x \middle | \ H0 \right)$$

где “X” - случайная величина, соответствующая некоторому  
способу обобщения данных (например, среднему значению или пропорции), а “x” - наблюдаемое  
значение этого обобщения в текущих данных.  

Теперь мы математически определили то, что мы называем Pvalue, но научный вопрос заключается  
в том, что оно означает? Это не то же самое, что спрашивать, что делают люди, когда они наблюдают  
P <= 0.05. Это обычай, который лучше всего описывается социологически.  Действия должны быть  
мотивированы или оправданы какой-либо концепцией основополагающего смысла, которую мы рассмотрим  
здесь.  

Поскольку Pvalue не является частью какого-либо формального математического вывода, его значение  
неуловимо. Ниже перечислены наиболее распространенные неверные интерпретации значения P с кратким  
объяснением того, почему они неверны. Некоторые из перечисленных неправильных представлений эквивалентны,  
хотя и не всегда осознаются как таковые. Затем мы рассмотрим Pvalue через байесовскую призму,  
чтобы лучше понять, что оно означает с точки зрения логических выводов.  

Для простоты мы предположим, что значение P получено в результате рандомизированного эксперимента  
с участием двух групп, в котором эффект вмешательства измеряется как разница в какой-либо средней  
характеристике, например, скорости излечения. Мы не будем рассматривать множество других причин,  
по которым исследование или статистический анализ могут вводить в заблуждение, от наличия скрытой  
предвзятости до использования неподходящих моделей; мы сосредоточимся исключительно на самом Pvalue  
при идеальных обстоятельствах. Нулевая гипотеза будет определяться как гипотеза об отсутствии  
эффекта от вмешательства  

#### №1: Если P = 0.05, вероятность того, что нулевая гипотеза окажется верной, составляет всего 5%.
Это, без сомнения, самое распространенное и пагубное из многих неправильных представлений о Pvalue.  
Оно закрепляет ложное представление о том, что только данные могут сказать нам, насколько вероятно,  
что мы будем правы или ошибемся в своих выводах. Самый простой способ убедиться в том, что это неверно, -  
отметить, что Pvalue вычисляется в предположении, что нулевая гипотеза верна. Следовательно, она не
может одновременно быть вероятностью того, что нулевая гипотеза ложна. Предположим, что мы подбрасываем  
монетку четыре раза и видим четыре орла, двустороннее P ≈ .125. Это не означает, что вероятность того,  
что монета окажется чистой, составляет всего 12,5%. Единственный способ рассчитать эту вероятность -  
использовать теорему Байеса, которая будет рассмотрена позже.  

#### №2: Незначительная разница (например, P >.05) означает, что между группами нет различий.  
Незначительная разница просто означает, что нулевой эффект статистически согласуется с наблюдаемыми  
результатами, а также с диапазоном эффектов, включенных в доверительный интервал. Это не делает  
нулевой эффект наиболее вероятным. Эффект, наилучшим образом подтверждаемый данными данного эксперимента,  
всегда является наблюдаемым эффектом, независимо от его значимости.  

#### №3: Статистически значимый результат является клинически (практически) важным. 
Часто это не соответствует действительности. Во-первых, разница может быть слишком мала, чтобы быть  
клинически значимой. Pvalue не несет никакой информации о величине эффекта, которая определяется оценкой  
эффекта и доверительным интервалом. Во-вторых, конечная точка сама по себе может не иметь клинического  
значения, как это может иметь место с некоторыми суррогатными результатами: частота ответа в сравнении  
с выживаемостью, количество CD4 в сравнении с клиническим заболеванием, изменение шкалы измерений в сравнении  
с улучшением функционирования и так далее.  

#### №4: Исследования, в которых Pvalue находятся на противоположных сторонах 0.05, противоречивы.  
Исследования могут иметь разную степень значимости, даже если оценки пользы от лечения идентичны, за счет  
изменения только точности оценки, обычно в зависимости от размера выборки (рис. 2А). Исследования
статистически противоречивы только тогда, когда разница между их результатами вряд ли была случайной, что  
соответствует случаям, когда их доверительные интервалы практически не совпадают, что формально  
оценивается с помощью теста на неоднородность.  
``` тут вставить картинку и не оч. понятно о чём речь ... мдамс```

#### №5: Исследования с одинаковым Pvalue дают одинаковые доказательства против нулевой гипотезы. 
При одинаковом Pvalue могут наблюдаться совершенно разные эффекты. На рисунке 2B показаны результаты двух  
исследований, в одном из которых эффект лечения составил 3% (доверительный интервал [ДИ] от 0% до 6%),  
а другой - с эффектом в 19% (ДИ от 0% до 38%). Оба они имеют Pvalue, равное 0.05, но тот факт, что они  
означают разные вещи, легко продемонстрировать. Если бы мы сочли, что для компенсации побочных эффектов этой  
терапии необходима 10%-ная польза, мы вполне могли бы принять терапию на основе исследования, показавшего  
значительный эффект и категорически отвергают эту терапию, основываясь на исследовании, показавшем небольшой   
эффект, что исключает 10%-ную выгоду. Конечно, также возможно получить такое же Pvalue, даже если нижний  
ДИ не близок к нулю.  
Это кажущееся несоответствие возникает из-за того, что Pvalue определяет “доказательства” только в отношении  
одной гипотезы — нулевой. Нет понятия положительного доказательства — если данные с значением P = 0.05  
свидетельствуют против нулевой, то в пользу чего они свидетельствуют?  
В этом примере наиболее убедительными доказательствами преимущества являются данные о 3% в одном исследовании  
и 19% в другом. Если бы мы провели относительную количественную оценку доказательств и спросили, в каком  
эксперименте было получено больше доказательств 10-процентного или более высокого эффекта (по сравнению с  
нулевым показателем), мы бы обнаружили, что в исследовании, показавшем 19-процентную пользу, доказательств  
было гораздо больше.

#### №6: P=0.05 означает, что мы наблюдали данные, которые при нулевой гипотезе встречались бы только в 5% случаев
То, что это не так, сразу видно из определения Pvalue, вероятности наблюдаемых данных плюс более экстремальных  
данных при нулевой гипотезе. Результат со Pvalue, равным 0,05 (или любым другим значением), является наиболее  
вероятным из всех других возможных результатов, включенных в “хвостовую область”, которая определяет Pvalue.  
Вероятность любого индивидуального результата на самом деле довольно мала, и Фишер сказал, что он внес свой  
вклад остальная часть хвостовой части “в приблизительном виде”. Как мы увидим далее в этой главе, включение этих  
редких результатов создает серьезные логические и количественные проблемы с точки зрения целевого значения, и  
использование сравнительных, а не единичных вероятностей для оценки фактических данных устраняет необходимость  
включать результаты, отличные от тех, которые наблюдались.  

Это ошибка, допущенная в опубликованном опросе ординаторов, приведенном во введении, в котором были предложены  
следующие четыре варианта ответа в качестве возможных интерпретаций P =.05:  
a. Вероятность того, что разница будет обнаружена снова, если исследование повторить, больше 1 к 20.  
b. Вероятность того, что такое большое различие могло возникнуть случайно, меньше 1 к 20.  
c. Вероятность того, что такое большое различие могло возникнуть случайно, больше 1 к 20.  
d. Вероятность того, что результаты исследования верны, составляет 95%.  
Правильный ответ был обозначен как “с”, в то время как  правильный ответ должен был звучать так:  
“Вероятность того, что такая большая разница может возникнуть случайно, превышает 1 к 20”.  

Эти “более экстремальные” значения, включенные в определение Pvalue, на самом деле создают оперативную сложность при  
расчете Pvalue, поскольку более экстремальные данные по определению являются ненаблюдаемыми данными. То, что  
“могло бы” наблюдаться, зависит от того, какой эксперимент мы предполагаем повторить. Это означает, что два  
эксперимента с идентичными данными об идентичных пациентах могли бы привести к разным Pvalue, если бы  
предполагаемый “долгосрочный период” был разным. Это может произойти, когда в одном исследовании используется  
правило остановки, а в другом - нет, или если в одном используется множественное сравнение, а в другом - нет.  

#### №7: P = 0,05 и P <=.05 означают одно и то же. 
Это неправильное представление показывает, как дьявольски трудно объяснить или понять Pvalue.  
Существует большая разница между этими результатами с точки зрения весомости доказательств,  
но поскольку с каждым из них связано одинаковое число (5%), эту разницу буквально невозможно передать.  
Его можно рассчитать и четко увидеть только с помощью байесовской метрики достоверности.  

#### №8: Pvalue правильно записываются в виде неравенств (например, “P <=.02”, когда P = 0.015).  
Выражение всех Pvalue в виде неравенств является путаницей, возникающей из-за сочетания  
проверки гипотез и Pvalue. При проверке гипотезы устанавливается заранее установленный  
порог “отклонения”. Обычно он устанавливается на уровне P=.05, что соответствует частоте ошибок  
первого типа (или “альфа”), равной 5%. В таком тесте единственной важной информацией является то,  
попала ли наблюдаемая разница в область отклонения или нет, например , соответствует ли Pvalue ≈.05.  
В этом случае имеет смысл выразить результат в виде неравенства (P <=.05 против P ≈.05).  

Но обычно нас интересует, сколько доказательств есть против нулевой гипотезы; именно по этой причине  
используются Pvalue. Для этой цели имеет значение, равно ли значение P .50, .06,.04 или .00001.  
Чтобы подчеркнуть силу доказательств, всегда следует указывать точный Pvalue.  Если неравенство используется  
просто для указания на то, следует ли отвергать нулевую гипотезу или нет, это может быть сделано только с  
заранее заданным порогом, например .05. Порог не может зависеть от наблюдаемого Pvalue, означающее, что  
мы не можем сообщить “P <.01”, если мы наблюдаем значение P ≈.008, а пороговое значение равно .05.  
Независимо от того, насколько низким было Pvalue, мы должны сообщить “P < .05”. Но отказ очень редко  
является проблемой, представляющей исключительный интерес. Многие медицинские журналы требуют, чтобы  
очень малые Pvalue (например, <.001) указывались как неравенства по стилистическим соображениям.  
Обычно это не является большой проблемой, за исключением случаев, когда ситуации, когда были проведены  
буквально тысячи статистических тестов (как в геномных экспериментах), когда многие очень малые Pvalue  
могут быть получены случайно, и различие между малыми и чрезвычайно малыми Pvalue важно для правильных  
выводов.  

#### №9: P=.05 означает, что если вы отвергнете нулевую гипотезу, вероятность ошибки первого типа составит всего 5%
Теперь мы попадаем в логический зыбучий песок. Это утверждение эквивалентно заблуждению № 1,  
хотя это может быть трудно заметить сразу. Ошибка первого типа - это “ложноположительный результат”,  
вывод о том, что разница есть, когда никакой разницы не существует. Если такой вывод представляет собой  
ошибку, то по определению разницы нет. Таким образом, 5%-ная вероятность ложного отклонения эквивалентна  
утверждению, что существует 5%-ная вероятность того, что нулевая гипотеза верна, что является заблуждением  
№ 1.

Другой способ убедиться в том, что это неверно, - представить, что мы исследуем серию экспериментов с терапией  
, в эффективности которой мы уверены, например, с инсулином для лечения диабета. Если мы отвергнем  
нулевую гипотезу, вероятность того, что отказ будет ложным (ошибка 1-го типа), равна нулю.  
Поскольку все отклонения нулевой гипотезы верны, не имеет значения, каково Pvalue. И наоборот, если  
бы мы тестировали бесполезную терапию, скажем, медные браслеты для лечения диабета, все отклонения были  
бы ложными, независимо от Pvalue.
Таким образом, вероятность того, что отказ является правильным или неправильным, очевидна зависит не только  
от Pvalue. Используя байесовский словарь, это также зависит от нашей априорной уверенности (или   
силы внешних свидетельств), которая количественно определяется как “априорная вероятность” гипотезы.  

#### №10: При пороговом значении значимости P =.05 вероятность ошибки I типа составит 5%. 
Отличие этого утверждения от заблуждения № 9 заключается в том, что здесь мы рассматриваем вероятность  
ошибки первого типа до завершения эксперимента, а не после его отклонения. Однако, как и в предыдущем  
случае, вероятность ошибки первого типа зависит от предварительной вероятности того, что нулевая гипотеза  
верна. Если она верна, то вероятность ложного отклонения действительно составляет 5%. Если мы знаем, что  
нулевая гипотеза ложна, вероятность ошибки первого типа исключена. Если мы если вы не уверены, вероятность  
ложноположительного результата составляет от нуля до 5%.  
Вышеприведенный пункт предполагает отсутствие проблем с множественностью или дизайном исследования.  
Однако в наш новый век геномной медицины часто случается так, что буквально тысячи неявных гипотез могут быть  
рассмотрены в рамках одного анализа, например, при сравнении экспрессии 5000 генов у больных и здоровых  
субъектов. Если мы определим “ошибку I рода” как вероятность того, что любой из тысяч возможных предикторов  
будет ложно объявлен как “реальный”, то Pvalue для любого конкретного предиктора имеет мало связи с  
ошибкой I рода, связанной со всем экспериментом целиком. Здесь проблема не только в самом Pvalue, но и в  
несоответствии между Pvalue, вычисленным для одного предиктора, и гипотезой, охватывающей множество  
возможных предикторов.  

Другой способ сформулировать проблему заключается в том, что поиск по тысячам  
предикторов подразумевает очень низкую априорную вероятность для любого из них, что делает
апостериорную вероятность для одиночного сравнения чрезвычайно низкой даже при низком Pvalue.  
Поскольку 1 - (апостериорная вероятность) это вероятность совершения ошибки при объявлении, что
отношение “реальное”, при довольно низком Pvalue все еще существует высокая вероятность 
ложного отклонения.  

#### №11:Вы должны использовать одностороннее значение P, когда вас не волнует результат в одном направлении, или разницав этом направлении невозможна. 
Это удивительно тонкий и сложный вопрос, который стал предметом многочисленных технических дискуссий,  
и есть разумные основания для разногласий. Но практический эффект использования одностороннего  
значения P заключается в повышении очевидной достоверности результатов, основанных на соображениях,  
которых нет в данных. Таким образом, использование одностороннего Pvalue означает, что Pvalue будет  
включать установки, убеждения или предпочтения экспериментатора в оценка силы доказательств.  
Если нас интересует Pvalue как показатель силы доказательств, то это не имеет смысла. Если нас  
интересуют вероятности возникновения ошибок типа I или типа II, то может иметь смысл рассмотреть  
области одностороннего или двустороннего отклонения, но в этом контексте нет необходимости  
использовать Pvalue.  

#### №12: Научное заключение или лечебная политика должны основываться на том, является ли Pvalue значимым.
Это неправильное представление распространяется на все остальные. Это равносильно утверждению, что  
величина эффекта не имеет значения, что в данном эксперименте содержатся только доказательства,  
имеющие отношение к научному заключению, и что как убеждения, так и действия непосредственно вытекают  
из статистических результатов. Доказательства, полученные в ходе данного исследования, должны быть  
объединены с результатами предыдущей работы, чтобы сделать вывод. В некоторых случаях научно обоснованный-  
возможным выводом может быть то, что нулевая гипотеза, вероятно, остается верной даже после получения  
значимого результата, а в других случаях незначительное Pvalue может по-прежнему приводить к  
выводу о том, что лечение работает. Формально это можно сделать только с помощью байесовских подходов.  
Чтобы оправдать действия, мы должны учитывать серьезность ошибок, вытекающих из этих действий, а также  
вероятность того, что выводы будут неверными.  

















