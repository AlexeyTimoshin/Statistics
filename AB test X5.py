# Код для расчёта выборки
import numpy as np
from scipy import stats

alfa = 0.05
beta = 0.2
mu_control = 2500
std = 800
effect = 100
mu_pilot = mu_control + effect 

t_alfa = stats.norm.ppf(1-alfa/2, loc=0, scale=1) # == 1.96
t_beta = stats.norm.ppf(1-beta, loc=0, scale=1)   # == 1.28
var = 2 * std ** 2

sample_size = int((t_alfa + t_beta) ** 2 * var / (effect ** 2)) # == 1004

# Теперь надо проверить данный размер выборки на то что он гарантирует заданные уровни ошибок 1 и 2 рода
# Будем генерировать данные из нормального распределения, но на практике надо из эмпирического 
# Для этого сгенерируем данные для одного А/А теста и одного А/В - 2 контрольных распределения 
# между которыми нет различий и одно с заданным эффектом.
# По А/А расределению будем измерять ошибку 1 рода, по А/В ошибку 2 рода

# Здесь будем хранить полученные ошибки
first_type_err = [] 
second_type_err = []

sample_size = 1004
# Запустим 5000 симуляций - гулять, так гулять!

for _ in range(5000):
    control_one = np.random.normal(mu_control, std, sample_size)
    control_two = np.random.normal(mu_control, std, sample_size)
    pilot = np.random.normal(mu_pilot, std, sample_size)
    _, pvalue_aa = stats.ttest_ind(control_one, control_two)
    first_type_err.append(pvalue_aa < alfa) 
    _, pvalue_ab = stats.ttest_ind(control_one, pilot)
    second_type_err.append(pvalue_ab >= alfa)

# найдём среднее
first_type_err_count = np.mean(first_type_err) 
second_type_err_count = np.mean(second_type_err)

# т.к. мы генерируем случайные числа - ответ каждый раз будет отличаться
# в этот раз получились такие значения
print(f"Количество ошибок 1 рода - {first_type_err_count:0.3f}") # 0.048 
print(f"Количество ошибок 2 рода - {second_type_err_count:0.3f}") # 0.189
