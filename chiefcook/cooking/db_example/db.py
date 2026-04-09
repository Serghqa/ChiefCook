
recipes_database = {
    # ==================== РУССКАЯ КУХНЯ (20 рецептов) ====================
    "RUSSIAN": [
        {
            "name": "Борщ",
            "description": "Наваристый красный борщ со свеклой и мясом, подается со сметаной и зеленью",
            "instructions": "Сварить мясной бульон. Отдельно обжарить свеклу с морковью и луком. Добавить в бульон нарезанный картофель и капусту. Через 15 минут добавить зажарку. Варить до готовности. Подавать со сметаной и чесноком.",
            "cooking_time": 90,
            "category": "FIRST",
            "tags": ["HEARTY", "SOUP"],
            "ingredients": [
                {"name": "Говядина на кости", "amount": 500, "unit": "G"},
                {"name": "Свекла", "amount": 300, "unit": "G"},
                {"name": "Капуста белокочанная", "amount": 300, "unit": "G"},
                {"name": "Картофель", "amount": 4, "unit": "PC"},
                {"name": "Морковь", "amount": 1, "unit": "PC"},
                {"name": "Лук репчатый", "amount": 1, "unit": "PC"},
                {"name": "Томатная паста", "amount": 30, "unit": "G"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"},
                {"name": "Сметана", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Щи из свежей капусты",
            "description": "Классические русские щи с говядиной",
            "instructions": "Сварить бульон. Добавить нарезанную капусту, картофель. Обжарить морковь и лук, добавить в суп. Варить 30 минут. Подавать с зеленью и сметаной.",
            "cooking_time": 70,
            "category": "FIRST",
            "tags": ["SOUP", "EASY"],
            "ingredients": [
                {"name": "Говядина", "amount": 400, "unit": "G"},
                {"name": "Капуста", "amount": 400, "unit": "G"},
                {"name": "Картофель", "amount": 4, "unit": "PC"},
                {"name": "Морковь", "amount": 1, "unit": "PC"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Томатная паста", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Солянка сборная мясная",
            "description": "Острый, наваристый суп с несколькими видами мяса",
            "instructions": "Сварить бульон из говядины. Добавить нарезанные колбасу, сосиски, ветчину. Добавить соленые огурцы, оливки, каперсы. Варить 15 минут. Подавать с лимоном и сметаной.",
            "cooking_time": 80,
            "category": "FIRST",
            "tags": ["HEARTY", "SOUP", "SPICY"],
            "ingredients": [
                {"name": "Говядина", "amount": 300, "unit": "G"},
                {"name": "Колбаса вареная", "amount": 150, "unit": "G"},
                {"name": "Сосиски", "amount": 150, "unit": "G"},
                {"name": "Ветчина", "amount": 100, "unit": "G"},
                {"name": "Огурцы соленые", "amount": 3, "unit": "PC"},
                {"name": "Оливки", "amount": 100, "unit": "G"},
                {"name": "Лимон", "amount": 0.5, "unit": "PC"}
            ]
        },
        {
            "name": "Рассольник",
            "description": "Суп с солеными огурцами и перловой крупой",
            "instructions": "Отварить перловку отдельно. Сварить мясной бульон. Добавить картофель, затем пассерованные овощи и перловку. В конце добавить нарезанные соленые огурцы и рассол.",
            "cooking_time": 80,
            "category": "FIRST",
            "tags": ["SOUP"],
            "ingredients": [
                {"name": "Говядина", "amount": 400, "unit": "G"},
                {"name": "Перловая крупа", "amount": 100, "unit": "G"},
                {"name": "Огурцы соленые", "amount": 3, "unit": "PC"},
                {"name": "Картофель", "amount": 3, "unit": "PC"},
                {"name": "Морковь", "amount": 1, "unit": "PC"},
                {"name": "Лук", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Оливье",
            "description": "Классический новогодний салат",
            "instructions": "Отварить картофель, морковь, яйца. Нарезать все ингредиенты кубиками. Добавить горошек и майонез. Перемешать.",
            "cooking_time": 50,
            "category": "SALAD",
            "tags": ["EASY", "PARTY"],
            "ingredients": [
                {"name": "Колбаса вареная", "amount": 300, "unit": "G"},
                {"name": "Картофель", "amount": 4, "unit": "PC"},
                {"name": "Морковь", "amount": 2, "unit": "PC"},
                {"name": "Яйца", "amount": 4, "unit": "PC"},
                {"name": "Огурцы соленые", "amount": 3, "unit": "PC"},
                {"name": "Горошек консервированный", "amount": 200, "unit": "G"},
                {"name": "Майонез", "amount": 150, "unit": "G"}
            ]
        },
        {
            "name": "Сельдь под шубой",
            "description": "Слоеный салат из селедки, овощей и свеклы",
            "instructions": "Отварить овощи. Выкладывать слоями: тертая свекла, морковь, картофель, нарезанная селедка, лук. Каждый слой промазывать майонезом. Верхний слой — свекла и майонез.",
            "cooking_time": 60,
            "category": "SALAD",
            "tags": ["PARTY", "GOURMET"],
            "ingredients": [
                {"name": "Сельдь соленая", "amount": 300, "unit": "G"},
                {"name": "Свекла", "amount": 2, "unit": "PC"},
                {"name": "Картофель", "amount": 3, "unit": "PC"},
                {"name": "Морковь", "amount": 2, "unit": "PC"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Майонез", "amount": 200, "unit": "G"}
            ]
        },
        {
            "name": "Винегрет",
            "description": "Овощной салат со свеклой и солеными огурцами",
            "instructions": "Отварить свеклу, картофель, морковь. Нарезать кубиками. Добавить соленые огурцы, квашеную капусту, лук. Заправить растительным маслом.",
            "cooking_time": 45,
            "category": "SALAD",
            "tags": ["VEGETARIAN", "LENTEN", "EASY"],
            "ingredients": [
                {"name": "Свекла", "amount": 2, "unit": "PC"},
                {"name": "Картофель", "amount": 3, "unit": "PC"},
                {"name": "Морковь", "amount": 2, "unit": "PC"},
                {"name": "Огурцы соленые", "amount": 2, "unit": "PC"},
                {"name": "Капуста квашеная", "amount": 150, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Масло растительное", "amount": 30, "unit": "ML"}
            ]
        },
        {
            "name": "Пельмени домашние",
            "description": "Домашние пельмени с сочным мясным фаршем",
            "instructions": "Замесить тесто из муки, яиц и воды. Приготовить фарш из свинины и говядины с луком. Раскатать тесто, вырезать кружки, слепить пельмени. Варить в подсоленной воде 5-7 минут после всплытия.",
            "cooking_time": 120,
            "category": "SECOND",
            "tags": ["HEARTY", "FAMILY"],
            "ingredients": [
                {"name": "Мука", "amount": 500, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Вода", "amount": 200, "unit": "ML"},
                {"name": "Свинина", "amount": 400, "unit": "G"},
                {"name": "Говядина", "amount": 300, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"}
            ]
        },
        {
            "name": "Котлеты по-киевски",
            "description": "Нежные куриные котлеты с маслом внутри",
            "instructions": "Отбить куриное филе. Завернуть внутрь сливочное масло и зелень. Обвалять в яйце и сухарях. Обжарить до золотистой корочки, затем довести до готовности в духовке.",
            "cooking_time": 50,
            "category": "SECOND",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Куриное филе", "amount": 600, "unit": "G"},
                {"name": "Сливочное масло", "amount": 100, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Панировочные сухари", "amount": 100, "unit": "G"},
                {"name": "Укроп", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Бефстроганов",
            "description": "Говядина в сметанном соусе",
            "instructions": "Нарезать говядину соломкой. Обжарить с луком. Добавить муку, затем сметану и бульон. Тушить 15 минут.",
            "cooking_time": 40,
            "category": "SECOND",
            "tags": ["QUICK"],
            "ingredients": [
                {"name": "Говядина", "amount": 500, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Сметана", "amount": 200, "unit": "G"},
                {"name": "Мука", "amount": 20, "unit": "G"},
                {"name": "Масло сливочное", "amount": 30, "unit": "G"}
            ]
        },
        {
            "name": "Голубцы",
            "description": "Капустные рулеты с мясом и рисом",
            "instructions": "Отварить капустные листья. Приготовить фарш с рисом. Завернуть начинку в листья. Тушить в томатно-сметанном соусе 40 минут.",
            "cooking_time": 100,
            "category": "SECOND",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Капуста белокочанная", "amount": 1, "unit": "PC"},
                {"name": "Фарш мясной", "amount": 500, "unit": "G"},
                {"name": "Рис", "amount": 100, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Томатная паста", "amount": 50, "unit": "G"},
                {"name": "Сметана", "amount": 150, "unit": "G"}
            ]
        },
        {
            "name": "Жаркое по-домашнему",
            "description": "Мясо с картофелем в горшочках",
            "instructions": "Нарезать мясо и овощи. Сложить в горшочки слоями: мясо, картофель, морковь, лук. Залить бульоном. Запекать в духовке 1 час.",
            "cooking_time": 80,
            "category": "SECOND",
            "tags": ["OVEN", "HEARTY"],
            "ingredients": [
                {"name": "Свинина", "amount": 500, "unit": "G"},
                {"name": "Картофель", "amount": 6, "unit": "PC"},
                {"name": "Морковь", "amount": 1, "unit": "PC"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Бульон", "amount": 200, "unit": "ML"}
            ]
        },
        {
            "name": "Драники",
            "description": "Картофельные оладьи",
            "instructions": "Натереть картофель на мелкой терке. Отжать сок. Добавить яйцо, муку, лук. Обжаривать на сковороде с двух сторон до золотистого цвета.",
            "cooking_time": 30,
            "category": "BREAKFAST",
            "tags": ["QUICK", "EASY", "PP"],
            "ingredients": [
                {"name": "Картофель", "amount": 800, "unit": "G"},
                {"name": "Яйца", "amount": 1, "unit": "PC"},
                {"name": "Мука", "amount": 50, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Соль", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Сырники",
            "description": "Творожные сырники на завтрак",
            "instructions": "Смешать творог, яйцо, сахар, муку. Сформировать сырники. Обжарить на сковороде до золотистой корочки. Подавать со сметаной.",
            "cooking_time": 25,
            "category": "BREAKFAST",
            "tags": ["QUICK", "BREAKFAST", "KIDS"],
            "ingredients": [
                {"name": "Творог", "amount": 400, "unit": "G"},
                {"name": "Яйца", "amount": 1, "unit": "PC"},
                {"name": "Мука", "amount": 60, "unit": "G"},
                {"name": "Сахар", "amount": 30, "unit": "G"},
                {"name": "Сметана", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Блины тонкие",
            "description": "Тонкие кружевные блины на молоке",
            "instructions": "Смешать яйца, сахар, соль. Добавить молоко, затем муку. Влить растительное масло. Жарить на раскаленной сковороде.",
            "cooking_time": 40,
            "category": "BREAKFAST",
            "tags": ["QUICK", "EASY"],
            "ingredients": [
                {"name": "Молоко", "amount": 500, "unit": "ML"},
                {"name": "Мука", "amount": 200, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Сахар", "amount": 30, "unit": "G"},
                {"name": "Масло растительное", "amount": 30, "unit": "ML"}
            ]
        },
        {
            "name": "Оладьи на кефире",
            "description": "Пышные оладьи на кефире",
            "instructions": "Смешать кефир, яйцо, сахар, соду. Добавить муку. Жарить на сковороде под крышкой.",
            "cooking_time": 25,
            "category": "BREAKFAST",
            "tags": ["QUICK", "EASY"],
            "ingredients": [
                {"name": "Кефир", "amount": 250, "unit": "ML"},
                {"name": "Мука", "amount": 200, "unit": "G"},
                {"name": "Яйца", "amount": 1, "unit": "PC"},
                {"name": "Сахар", "amount": 30, "unit": "G"},
                {"name": "Сода", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Гречневая каша с грибами",
            "description": "Рассыпчатая гречка с лесными грибами и луком",
            "instructions": "Отварить гречку до готовности. Обжарить грибы с луком. Смешать с кашей. Подавать с зеленью.",
            "cooking_time": 40,
            "category": "SECOND",
            "tags": ["VEGETARIAN", "LENTEN"],
            "ingredients": [
                {"name": "Гречневая крупа", "amount": 200, "unit": "G"},
                {"name": "Шампиньоны", "amount": 300, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Масло растительное", "amount": 30, "unit": "ML"}
            ]
        },
        {
            "name": "Медовик",
            "description": "Медовый торт со сметанным кремом",
            "instructions": "Испечь медовые коржи. Промазать сметанным кремом. Дать пропитаться 8 часов.",
            "cooking_time": 120,
            "category": "DESSERT",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Мед", "amount": 150, "unit": "G"},
                {"name": "Мука", "amount": 400, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Сахар", "amount": 200, "unit": "G"},
                {"name": "Сметана", "amount": 500, "unit": "G"},
                {"name": "Сливочное масло", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Наполеон",
            "description": "Классический слоеный торт с заварным кремом",
            "instructions": "Испечь слоеные коржи. Приготовить заварной крем. Промазать коржи, посыпать крошкой. Дать пропитаться.",
            "cooking_time": 180,
            "category": "DESSERT",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Мука", "amount": 500, "unit": "G"},
                {"name": "Маргарин", "amount": 250, "unit": "G"},
                {"name": "Молоко", "amount": 500, "unit": "ML"},
                {"name": "Яйца", "amount": 3, "unit": "PC"},
                {"name": "Сахар", "amount": 250, "unit": "G"},
                {"name": "Сливочное масло", "amount": 200, "unit": "G"}
            ]
        },
        {
            "name": "Квас домашний",
            "description": "Освежающий хлебный квас",
            "instructions": "Залить ржаные сухари кипятком. Настоять 8 часов. Добавить сахар, дрожжи. Оставить бродить на 2 дня. Разлить по бутылкам.",
            "cooking_time": 2880,
            "category": "DRINK",
            "tags": ["EASY"],
            "ingredients": [
                {"name": "Ржаной хлеб", "amount": 300, "unit": "G"},
                {"name": "Сахар", "amount": 150, "unit": "G"},
                {"name": "Дрожжи", "amount": 10, "unit": "G"},
                {"name": "Вода", "amount": 3, "unit": "L"}
            ]
        }
    ],

    # ==================== ИТАЛЬЯНСКАЯ КУХНЯ (20 рецептов) ====================
    "ITALIAN": [
        {
            "name": "Пицца Маргарита",
            "description": "Классическая неаполитанская пицца с томатным соусом, моцареллой и базиликом",
            "instructions": "Приготовить тесто из муки, воды, дрожжей, соли и оливкового масла. Дать подойти 2 часа. Раскатать, намазать томатным соусом, выложить моцареллу и листья базилика. Выпекать 10-12 минут при 250°C.",
            "cooking_time": 150,
            "category": "SECOND",
            "tags": ["OVEN", "EASY"],
            "ingredients": [
                {"name": "Мука 00", "amount": 300, "unit": "G"},
                {"name": "Вода", "amount": 200, "unit": "ML"},
                {"name": "Дрожжи", "amount": 5, "unit": "G"},
                {"name": "Моцарелла", "amount": 200, "unit": "G"},
                {"name": "Томатный соус", "amount": 100, "unit": "ML"},
                {"name": "Базилик", "amount": 10, "unit": "G"},
                {"name": "Масло оливковое", "amount": 15, "unit": "ML"}
            ]
        },
        {
            "name": "Пицца Пепперони",
            "description": "Пицца с пикантной колбасой пепперони и сыром",
            "instructions": "Приготовить тесто. Намазать томатным соусом. Выложить пепперони и моцареллу. Выпекать 12 минут при 250°C.",
            "cooking_time": 150,
            "category": "SECOND",
            "tags": ["OVEN"],
            "ingredients": [
                {"name": "Мука", "amount": 300, "unit": "G"},
                {"name": "Дрожжи", "amount": 5, "unit": "G"},
                {"name": "Моцарелла", "amount": 200, "unit": "G"},
                {"name": "Пепперони", "amount": 100, "unit": "G"},
                {"name": "Томатный соус", "amount": 100, "unit": "ML"}
            ]
        },
        {
            "name": "Пицца Четыре сыра",
            "description": "Пицца с четырьмя видами итальянских сыров",
            "instructions": "Приготовить тесто. Смешать моцареллу, горгонзолу, пармезан и фонтину. Выложить на тесто. Выпекать 10 минут.",
            "cooking_time": 130,
            "category": "SECOND",
            "tags": ["OVEN", "VEGETARIAN"],
            "ingredients": [
                {"name": "Мука", "amount": 300, "unit": "G"},
                {"name": "Моцарелла", "amount": 100, "unit": "G"},
                {"name": "Горгонзола", "amount": 80, "unit": "G"},
                {"name": "Пармезан", "amount": 50, "unit": "G"},
                {"name": "Фонтина", "amount": 80, "unit": "G"}
            ]
        },
        {
            "name": "Спагетти Карбонара",
            "description": "Классическая паста с яйцом, беконом и пармезаном",
            "instructions": "Отварить спагетти. Обжарить бекон. Смешать яйца с тертым пармезаном. Соединить пасту с беконом, добавить яичную смесь, прогреть на слабом огне.",
            "cooking_time": 20,
            "category": "SECOND",
            "tags": ["QUICK", "EASY"],
            "ingredients": [
                {"name": "Спагетти", "amount": 300, "unit": "G"},
                {"name": "Бекон", "amount": 150, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Пармезан", "amount": 50, "unit": "G"},
                {"name": "Чеснок", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Паста Болоньезе",
            "description": "Спагетти с мясным соусом болоньезе",
            "instructions": "Обжарить фарш с луком, морковью и сельдереем. Добавить томаты и вино. Тушить 1 час. Подавать со спагетти и пармезаном.",
            "cooking_time": 90,
            "category": "SECOND",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Спагетти", "amount": 300, "unit": "G"},
                {"name": "Говяжий фарш", "amount": 400, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Морковь", "amount": 1, "unit": "PC"},
                {"name": "Томаты в собственном соку", "amount": 400, "unit": "G"},
                {"name": "Красное вино", "amount": 100, "unit": "ML"},
                {"name": "Пармезан", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Лазанья",
            "description": "Слоеная запеканка с мясным соусом и бешамелью",
            "instructions": "Приготовить соус болоньезе. Приготовить соус бешамель. Собрать лазанью слоями: соус, листы, бешамель, пармезан. Запекать 40 минут при 180°C.",
            "cooking_time": 120,
            "category": "SECOND",
            "tags": ["GOURMET", "OVEN"],
            "ingredients": [
                {"name": "Листы лазаньи", "amount": 250, "unit": "G"},
                {"name": "Фарш", "amount": 500, "unit": "G"},
                {"name": "Молоко", "amount": 500, "unit": "ML"},
                {"name": "Мука", "amount": 50, "unit": "G"},
                {"name": "Моцарелла", "amount": 200, "unit": "G"},
                {"name": "Пармезан", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Ризотто с грибами",
            "description": "Кремовое ризотто с лесными грибами",
            "instructions": "Обжарить рис на масле. Постепенно добавлять бульон, помешивая. Добавить обжаренные грибы. В конце добавить пармезан и сливочное масло.",
            "cooking_time": 35,
            "category": "SECOND",
            "tags": ["VEGETARIAN"],
            "ingredients": [
                {"name": "Рис арборио", "amount": 300, "unit": "G"},
                {"name": "Грибы", "amount": 300, "unit": "G"},
                {"name": "Лук", "amount": 0.5, "unit": "PC"},
                {"name": "Бульон", "amount": 800, "unit": "ML"},
                {"name": "Пармезан", "amount": 50, "unit": "G"},
                {"name": "Масло сливочное", "amount": 30, "unit": "G"}
            ]
        },
        {
            "name": "Ризотто с морепродуктами",
            "description": "Изысканное ризотто с креветками и мидиями",
            "instructions": "Обжарить рис. Добавлять бульон. Отдельно обжарить морепродукты с чесноком. Соединить с ризотто. Добавить петрушку и лимонный сок.",
            "cooking_time": 35,
            "category": "SECOND",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Рис арборио", "amount": 300, "unit": "G"},
                {"name": "Креветки", "amount": 200, "unit": "G"},
                {"name": "Мидии", "amount": 200, "unit": "G"},
                {"name": "Бульон", "amount": 800, "unit": "ML"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"},
                {"name": "Петрушка", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Тирамису",
            "description": "Знаменитый итальянский десерт с маскарпоне и кофе",
            "instructions": "Взбить желтки с сахаром. Добавить маскарпоне. Взбить белки. Соединить. Обмакнуть печенье савоярди в кофе. Выложить слоями. Посыпать какао.",
            "cooking_time": 40,
            "category": "DESSERT",
            "tags": ["GOURMET", "NO_BAKE"],
            "ingredients": [
                {"name": "Маскарпоне", "amount": 500, "unit": "G"},
                {"name": "Яйца", "amount": 4, "unit": "PC"},
                {"name": "Сахар", "amount": 100, "unit": "G"},
                {"name": "Печенье савоярди", "amount": 200, "unit": "G"},
                {"name": "Кофе эспрессо", "amount": 200, "unit": "ML"},
                {"name": "Какао", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Панна котта",
            "description": "Нежный сливочный десерт с ягодным соусом",
            "instructions": "Нагреть сливки с сахаром. Добавить размоченный желатин. Разлить по формам. Охладить 4 часа. Подавать с ягодным соусом.",
            "cooking_time": 30,
            "category": "DESSERT",
            "tags": ["NO_BAKE", "EASY"],
            "ingredients": [
                {"name": "Сливки 33%", "amount": 500, "unit": "ML"},
                {"name": "Сахар", "amount": 80, "unit": "G"},
                {"name": "Желатин", "amount": 10, "unit": "G"},
                {"name": "Ваниль", "amount": 1, "unit": "PC"},
                {"name": "Ягоды", "amount": 150, "unit": "G"}
            ]
        },
        {
            "name": "Джелато",
            "description": "Итальянское пломбирное мороженое",
            "instructions": "Нагреть молоко со сливками. Взбить желтки с сахаром. Соединить, варить до загустения. Охладить, заморозить, периодически перемешивая.",
            "cooking_time": 60,
            "category": "DESSERT",
            "tags": ["KIDS"],
            "ingredients": [
                {"name": "Молоко", "amount": 500, "unit": "ML"},
                {"name": "Сливки", "amount": 250, "unit": "ML"},
                {"name": "Яйца", "amount": 4, "unit": "PC"},
                {"name": "Сахар", "amount": 150, "unit": "G"}
            ]
        },
        {
            "name": "Брускетта с томатами",
            "description": "Хрустящий хлеб с томатами и базиликом",
            "instructions": "Подсушить хлеб. Натереть чесноком. Выложить нарезанные томаты, соль, перец, оливковое масло, базилик.",
            "cooking_time": 10,
            "category": "SNACK",
            "tags": ["QUICK", "EASY", "VEGETARIAN"],
            "ingredients": [
                {"name": "Хлеб чиабатта", "amount": 8, "unit": "PC"},
                {"name": "Помидоры", "amount": 4, "unit": "PC"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"},
                {"name": "Базилик", "amount": 10, "unit": "G"},
                {"name": "Масло оливковое", "amount": 30, "unit": "ML"}
            ]
        },
        {
            "name": "Минестроне",
            "description": "Густой овощной суп с пастой",
            "instructions": "Обжарить лук, морковь, сельдерей. Добавить кабачок, фасоль, томаты. Залить бульоном. Добавить пасту. Варить до готовности. Подавать с пармезаном.",
            "cooking_time": 45,
            "category": "FIRST",
            "tags": ["VEGETARIAN", "SOUP"],
            "ingredients": [
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Морковь", "amount": 1, "unit": "PC"},
                {"name": "Кабачок", "amount": 1, "unit": "PC"},
                {"name": "Фасоль", "amount": 200, "unit": "G"},
                {"name": "Паста", "amount": 80, "unit": "G"},
                {"name": "Пармезан", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Гноччи",
            "description": "Картофельные клецки с томатным соусом",
            "instructions": "Сварить картофель. Сделать пюре. Добавить муку и яйцо. Сформировать гноччи. Варить 2 минуты. Подавать с соусом и пармезаном.",
            "cooking_time": 50,
            "category": "SECOND",
            "tags": ["VEGETARIAN"],
            "ingredients": [
                {"name": "Картофель", "amount": 800, "unit": "G"},
                {"name": "Мука", "amount": 200, "unit": "G"},
                {"name": "Яйца", "amount": 1, "unit": "PC"},
                {"name": "Томатный соус", "amount": 300, "unit": "ML"},
                {"name": "Пармезан", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Каннеллони",
            "description": "Трубочки из теста с мясом и сыром",
            "instructions": "Приготовить начинку из фарша и рикотты. Нафаршировать каннеллони. Выложить в форму, залить соусом бешамель. Запекать 30 минут.",
            "cooking_time": 70,
            "category": "SECOND",
            "tags": ["OVEN"],
            "ingredients": [
                {"name": "Каннеллони", "amount": 250, "unit": "G"},
                {"name": "Фарш", "amount": 400, "unit": "G"},
                {"name": "Рикотта", "amount": 200, "unit": "G"},
                {"name": "Молоко", "amount": 500, "unit": "ML"},
                {"name": "Пармезан", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Фриттата",
            "description": "Итальянский омлет с овощами",
            "instructions": "Обжарить овощи. Залить взбитыми яйцами с сыром. Готовить на медленном огне, затем перевернуть или допечь в духовке.",
            "cooking_time": 20,
            "category": "BREAKFAST",
            "tags": ["QUICK", "VEGETARIAN"],
            "ingredients": [
                {"name": "Яйца", "amount": 6, "unit": "PC"},
                {"name": "Кабачок", "amount": 0.5, "unit": "PC"},
                {"name": "Помидоры черри", "amount": 100, "unit": "G"},
                {"name": "Пармезан", "amount": 50, "unit": "G"},
                {"name": "Лук", "amount": 0.5, "unit": "PC"}
            ]
        },
        {
            "name": "Поллента",
            "description": "Кукурузная каша с сыром",
            "instructions": "Вскипятить воду с солью. Всыпать кукурузную муку. Варить 40 минут, помешивая. Добавить масло и сыр.",
            "cooking_time": 50,
            "category": "SECOND",
            "tags": ["VEGETARIAN", "EASY"],
            "ingredients": [
                {"name": "Кукурузная мука", "amount": 200, "unit": "G"},
                {"name": "Вода", "amount": 800, "unit": "ML"},
                {"name": "Сливочное масло", "amount": 50, "unit": "G"},
                {"name": "Пармезан", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Капрезе",
            "description": "Салат из моцареллы, томатов и базилика",
            "instructions": "Нарезать моцареллу и помидоры кружками. Выложить чередуя. Добавить листья базилика. Полить оливковым маслом, посыпать солью и перцем.",
            "cooking_time": 10,
            "category": "SALAD",
            "tags": ["QUICK", "VEGETARIAN", "EASY"],
            "ingredients": [
                {"name": "Моцарелла", "amount": 250, "unit": "G"},
                {"name": "Помидоры", "amount": 3, "unit": "PC"},
                {"name": "Базилик", "amount": 20, "unit": "G"},
                {"name": "Масло оливковое", "amount": 30, "unit": "ML"}
            ]
        },
        {
            "name": "Оссобуко",
            "description": "Тушеная телячья голяшка",
            "instructions": "Обжарить мясо. Добавить овощи, вино, бульон. Тушить 2 часа. Подавать с гремолатой (лимонная цедра, чеснок, петрушка).",
            "cooking_time": 150,
            "category": "SECOND",
            "tags": ["GOURMET", "HEARTY"],
            "ingredients": [
                {"name": "Телячья голяшка", "amount": 4, "unit": "PC"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Морковь", "amount": 1, "unit": "PC"},
                {"name": "Белое вино", "amount": 200, "unit": "ML"},
                {"name": "Бульон", "amount": 500, "unit": "ML"},
                {"name": "Лимон", "amount": 0.5, "unit": "PC"}
            ]
        },
        {
            "name": "Аранчини",
            "description": "Жареные рисовые шарики с начинкой",
            "instructions": "Приготовить ризотто. Охладить. Сформировать шарики, внутрь положить моцареллу и горошек. Обвалять в яйце и сухарях. Обжарить во фритюре.",
            "cooking_time": 60,
            "category": "SNACK",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Рис арборио", "amount": 300, "unit": "G"},
                {"name": "Моцарелла", "amount": 100, "unit": "G"},
                {"name": "Горошек", "amount": 100, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Панировочные сухари", "amount": 100, "unit": "G"}
            ]
        }
    ],

    # ==================== ГРУЗИНСКАЯ КУХНЯ (20 рецептов) ====================
    "GEORGIAN": [
        {
            "name": "Хачапури по-аджарски",
            "description": "Лепешка-лодочка с сулугуни и яйцом",
            "instructions": "Замесить дрожжевое тесто. Сформировать лодочку. Наполнить тертым сулугуни. Запечь 15 минут. В центр разбить яйцо и вернуть в духовку на 2 минуты.",
            "cooking_time": 90,
            "category": "SECOND",
            "tags": ["OVEN", "GOURMET"],
            "ingredients": [
                {"name": "Мука", "amount": 500, "unit": "G"},
                {"name": "Сулугуни", "amount": 400, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Масло сливочное", "amount": 50, "unit": "G"},
                {"name": "Дрожжи", "amount": 7, "unit": "G"}
            ]
        },
        {
            "name": "Хачапури по-имеретински",
            "description": "Закрытая лепешка с сыром",
            "instructions": "Замесить тесто на мацони. Раскатать, выложить тертый сулугуни. Защипать края. Выпекать 20 минут при 200°C. Смазать маслом.",
            "cooking_time": 60,
            "category": "SECOND",
            "tags": ["OVEN", "EASY"],
            "ingredients": [
                {"name": "Мука", "amount": 400, "unit": "G"},
                {"name": "Мацони", "amount": 250, "unit": "ML"},
                {"name": "Сулугуни", "amount": 400, "unit": "G"},
                {"name": "Сода", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Хинкали",
            "description": "Грузинские пельмени с мясом и бульоном внутри",
            "instructions": "Замесить тесто из муки, воды и соли. Приготовить фарш из говядины, свинины, лука, кинзы. Раскатать тесто, сформировать хинкали. Варить 10 минут в подсоленной воде.",
            "cooking_time": 120,
            "category": "SECOND",
            "tags": ["HEARTY", "GOURMET"],
            "ingredients": [
                {"name": "Мука", "amount": 500, "unit": "G"},
                {"name": "Вода", "amount": 250, "unit": "ML"},
                {"name": "Говядина", "amount": 400, "unit": "G"},
                {"name": "Свинина", "amount": 200, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Кинза", "amount": 30, "unit": "G"}
            ]
        },
        {
            "name": "Сациви",
            "description": "Курица в ореховом соусе",
            "instructions": "Отварить курицу. Приготовить соус из грецких орехов, чеснока, хмели-сунели. Залить курицу соусом. Дать настояться 6 часов.",
            "cooking_time": 90,
            "category": "SECOND",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Курица", "amount": 1, "unit": "PC"},
                {"name": "Грецкие орехи", "amount": 300, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Чеснок", "amount": 4, "unit": "PC"},
                {"name": "Хмели-сунели", "amount": 15, "unit": "G"}
            ]
        },
        {
            "name": "Чанах",
            "description": "Мясо с овощами в глиняном горшочке",
            "instructions": "Сложить в горшочек мясо, картофель, баклажаны, помидоры, перец. Добавить чеснок, кинзу. Тушить в духовке 1.5 часа.",
            "cooking_time": 120,
            "category": "SECOND",
            "tags": ["OVEN", "HEARTY"],
            "ingredients": [
                {"name": "Баранина", "amount": 500, "unit": "G"},
                {"name": "Картофель", "amount": 4, "unit": "PC"},
                {"name": "Баклажаны", "amount": 2, "unit": "PC"},
                {"name": "Помидоры", "amount": 3, "unit": "PC"},
                {"name": "Кинза", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Чахохбили",
            "description": "Курица с томатами и зеленью",
            "instructions": "Обжарить курицу. Добавить лук, помидоры. Тушить 40 минут. Добавить кинзу, чеснок, хмели-сунели.",
            "cooking_time": 60,
            "category": "SECOND",
            "tags": ["EASY"],
            "ingredients": [
                {"name": "Курица", "amount": 1, "unit": "PC"},
                {"name": "Помидоры", "amount": 500, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Кинза", "amount": 30, "unit": "G"},
                {"name": "Чеснок", "amount": 3, "unit": "PC"}
            ]
        },
        {
            "name": "Лобио",
            "description": "Острая фасоль с орехами и кинзой",
            "instructions": "Отварить красную фасоль. Обжарить лук, добавить фасоль, грецкие орехи, кинзу, чеснок, хмели-сунели. Прогреть 10 минут.",
            "cooking_time": 120,
            "category": "SECOND",
            "tags": ["VEGETARIAN", "LENTEN"],
            "ingredients": [
                {"name": "Красная фасоль", "amount": 300, "unit": "G"},
                {"name": "Грецкие орехи", "amount": 100, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Кинза", "amount": 30, "unit": "G"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"}
            ]
        },
        {
            "name": "Пхали",
            "description": "Овощная закуска с орехами",
            "instructions": "Отварить шпинат (или свеклу). Отжать. Добавить грецкие орехи, чеснок, кинзу, хмели-сунели. Сформировать шарики. Охладить.",
            "cooking_time": 40,
            "category": "SNACK",
            "tags": ["VEGETARIAN", "EASY"],
            "ingredients": [
                {"name": "Шпинат", "amount": 500, "unit": "G"},
                {"name": "Грецкие орехи", "amount": 150, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Кинза", "amount": 20, "unit": "G"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"}
            ]
        },
        {
            "name": "Оджахури",
            "description": "Жаркое из свинины с картофелем",
            "instructions": "Обжарить свинину до золотистой корочки. Отдельно обжарить картофель. Соединить, добавить лук, перец, кинзу.",
            "cooking_time": 45,
            "category": "SECOND",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Свинина", "amount": 500, "unit": "G"},
                {"name": "Картофель", "amount": 6, "unit": "PC"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Кинза", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Купаты",
            "description": "Домашние колбаски с пряностями",
            "instructions": "Смешать фарш с луком, чесноком, хмели-сунели. Начинить кишки. Обжарить на сковороде, затем довести до готовности в духовке.",
            "cooking_time": 60,
            "category": "SECOND",
            "tags": ["HEARTY", "GRILL"],
            "ingredients": [
                {"name": "Свинина", "amount": 600, "unit": "G"},
                {"name": "Говядина", "amount": 300, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Чеснок", "amount": 3, "unit": "PC"},
                {"name": "Кишки свиные", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Чурчхела",
            "description": "Грузинская сладость из виноградного сока и орехов",
            "instructions": "Нанизать грецкие орехи на нить. Сварить виноградный сок с мукой до густоты. Окунуть орехи в смесь. Сушить 2 недели.",
            "cooking_time": 20160,
            "category": "DESSERT",
            "tags": ["GOURMET", "EASY"],
            "ingredients": [
                {"name": "Виноградный сок", "amount": 1, "unit": "L"},
                {"name": "Мука", "amount": 200, "unit": "G"},
                {"name": "Грецкие орехи", "amount": 300, "unit": "G"}
            ]
        },
        {
            "name": "Гозинаки",
            "description": "Грецкие орехи в меду",
            "instructions": "Обжарить орехи. Растопить мед до жидкого состояния. Смешать с орехами. Выложить на пергамент, разровнять. Остудить, нарезать.",
            "cooking_time": 30,
            "category": "DESSERT",
            "tags": ["QUICK", "EASY"],
            "ingredients": [
                {"name": "Грецкие орехи", "amount": 300, "unit": "G"},
                {"name": "Мед", "amount": 200, "unit": "G"},
                {"name": "Сахар", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Аджапсандали",
            "description": "Овощное рагу из баклажанов",
            "instructions": "Обжарить баклажаны, перец, помидоры, лук. Тушить 30 минут. Добавить кинзу и чеснок.",
            "cooking_time": 50,
            "category": "SECOND",
            "tags": ["VEGETARIAN", "LENTEN"],
            "ingredients": [
                {"name": "Баклажаны", "amount": 3, "unit": "PC"},
                {"name": "Помидоры", "amount": 4, "unit": "PC"},
                {"name": "Перец болгарский", "amount": 2, "unit": "PC"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Кинза", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Кучмачи",
            "description": "Субпродукты с грецкими орехами",
            "instructions": "Отварить печень, сердце, легкие. Пропустить через мясорубку. Обжарить с луком. Добавить орехи, чеснок, гранатовый сок.",
            "cooking_time": 80,
            "category": "SNACK",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Говяжья печень", "amount": 300, "unit": "G"},
                {"name": "Сердце", "amount": 200, "unit": "G"},
                {"name": "Легкие", "amount": 200, "unit": "G"},
                {"name": "Грецкие орехи", "amount": 100, "unit": "G"},
                {"name": "Гранатовый сок", "amount": 50, "unit": "ML"}
            ]
        },
        {
            "name": "Суп харчо",
            "description": "Острый суп с говядиной и рисом",
            "instructions": "Сварить бульон. Добавить рис, обжаренный лук, ткемали, хмели-сунели. Варить до готовности. Добавить чеснок и кинзу.",
            "cooking_time": 90,
            "category": "FIRST",
            "tags": ["SOUP", "SPICY"],
            "ingredients": [
                {"name": "Говядина", "amount": 400, "unit": "G"},
                {"name": "Рис", "amount": 100, "unit": "G"},
                {"name": "Ткемали", "amount": 50, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Чеснок", "amount": 3, "unit": "PC"},
                {"name": "Кинза", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Мацони",
            "description": "Грузинский кисломолочный напиток",
            "instructions": "Вскипятить молоко, остудить до 40°C. Добавить закваску. Оставить в теплом месте на 8 часов. Охладить.",
            "cooking_time": 480,
            "category": "DRINK",
            "tags": ["EASY", "PP"],
            "ingredients": [
                {"name": "Молоко", "amount": 1, "unit": "L"},
                {"name": "Закваска", "amount": 2, "unit": "TBSP"}
            ]
        },
        {
            "name": "Лимонный ткемали",
            "description": "Соус из алычи",
            "instructions": "Сварить алычу с водой до размягчения. Протереть через сито. Добавить кинзу, чеснок, перец. Уварить до густоты.",
            "cooking_time": 60,
            "category": "SAUCE",
            "tags": ["EASY", "VEGETARIAN"],
            "ingredients": [
                {"name": "Алыча", "amount": 500, "unit": "G"},
                {"name": "Кинза", "amount": 30, "unit": "G"},
                {"name": "Чеснок", "amount": 3, "unit": "PC"},
                {"name": "Красный перец", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Баже",
            "description": "Ореховый соус",
            "instructions": "Измельчить грецкие орехи. Добавить чеснок, хмели-сунели, уксус. Развести водой до нужной консистенции.",
            "cooking_time": 15,
            "category": "SAUCE",
            "tags": ["QUICK", "VEGETARIAN"],
            "ingredients": [
                {"name": "Грецкие орехи", "amount": 200, "unit": "G"},
                {"name": "Чеснок", "amount": 4, "unit": "PC"},
                {"name": "Хмели-сунели", "amount": 10, "unit": "G"},
                {"name": "Винный уксус", "amount": 20, "unit": "ML"}
            ]
        },
        {
            "name": "Кубдари",
            "description": "Мясной пирог по-свански",
            "instructions": "Замесить тесто. Приготовить фарш с луком и пряностями. Раскатать тесто, выложить фарш, защипать. Выпекать 30 минут при 180°C.",
            "cooking_time": 80,
            "category": "SECOND",
            "tags": ["OVEN", "HEARTY"],
            "ingredients": [
                {"name": "Мука", "amount": 400, "unit": "G"},
                {"name": "Фарш", "amount": 500, "unit": "G"},
                {"name": "Лук", "amount": 3, "unit": "PC"},
                {"name": "Чеснок", "amount": 3, "unit": "PC"},
                {"name": "Кинза", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Лобиани",
            "description": "Лепешка с фасолью",
            "instructions": "Замесить тесто. Отварить фасоль, сделать пюре. Добавить лук, специи. Сформировать лепешки. Выпекать 25 минут.",
            "cooking_time": 90,
            "category": "SECOND",
            "tags": ["VEGETARIAN", "OVEN"],
            "ingredients": [
                {"name": "Мука", "amount": 400, "unit": "G"},
                {"name": "Фасоль", "amount": 300, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Кинза", "amount": 20, "unit": "G"}
            ]
        }
    ],

    # ==================== КИТАЙСКАЯ КУХНЯ (20 рецептов) ====================
    "CHINESE": [
        {
            "name": "Утка по-пекински",
            "description": "Хрустящая утка с тонкими блинчиками",
            "instructions": "Натереть утку специями, залить маринадом на 24 часа. Запекать до хрустящей корочки. Подавать с блинами, огурцом и соусом хойсин.",
            "cooking_time": 1500,
            "category": "SECOND",
            "tags": ["GOURMET", "OVEN"],
            "ingredients": [
                {"name": "Утка", "amount": 2, "unit": "KG"},
                {"name": "Мед", "amount": 100, "unit": "G"},
                {"name": "Соевый соус", "amount": 100, "unit": "ML"},
                {"name": "Имбирь", "amount": 30, "unit": "G"},
                {"name": "Мука для блинов", "amount": 200, "unit": "G"},
                {"name": "Огурец", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Курица Гунбао",
            "description": "Острая курица с арахисом",
            "instructions": "Обжарить курицу. Отдельно обжарить перец, имбирь, чеснок. Добавить соевый соус, уксус, сахар. Вернуть курицу, добавить арахис.",
            "cooking_time": 30,
            "category": "SECOND",
            "tags": ["QUICK", "SPICY"],
            "ingredients": [
                {"name": "Куриное филе", "amount": 500, "unit": "G"},
                {"name": "Арахис", "amount": 100, "unit": "G"},
                {"name": "Перец чили", "amount": 5, "unit": "G"},
                {"name": "Соевый соус", "amount": 50, "unit": "ML"},
                {"name": "Имбирь", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Свинина в кисло-сладком соусе",
            "description": "Хрустящая свинина с ананасом",
            "instructions": "Обжарить кусочки свинины в кляре. Приготовить соус из уксуса, сахара, кетчупа, ананасового сока. Смешать с мясом и овощами.",
            "cooking_time": 45,
            "category": "SECOND",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Свинина", "amount": 500, "unit": "G"},
                {"name": "Ананас консервированный", "amount": 200, "unit": "G"},
                {"name": "Перец болгарский", "amount": 1, "unit": "PC"},
                {"name": "Уксус", "amount": 50, "unit": "ML"},
                {"name": "Сахар", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Рис по-китайски с яйцом",
            "description": "Жареный рис с яйцом и горошком",
            "instructions": "Обжарить яйца. Добавить рис, горошек, кукурузу. Добавить соевый соус и кунжутное масло.",
            "cooking_time": 15,
            "category": "SECOND",
            "tags": ["QUICK", "EASY"],
            "ingredients": [
                {"name": "Рис отварной", "amount": 400, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Зеленый горошек", "amount": 100, "unit": "G"},
                {"name": "Соевый соус", "amount": 30, "unit": "ML"},
                {"name": "Масло кунжутное", "amount": 10, "unit": "ML"}
            ]
        },
        {
            "name": "Лапша с говядиной",
            "description": "Жареная лапша с говядиной и овощами",
            "instructions": "Отварить лапшу. Обжарить говядину. Добавить морковь, перец, лук. Добавить лапшу и соус.",
            "cooking_time": 30,
            "category": "SECOND",
            "tags": ["EASY"],
            "ingredients": [
                {"name": "Лапша яичная", "amount": 300, "unit": "G"},
                {"name": "Говядина", "amount": 400, "unit": "G"},
                {"name": "Морковь", "amount": 1, "unit": "PC"},
                {"name": "Соевый соус", "amount": 60, "unit": "ML"}
            ]
        },
        {
            "name": "Вонтоны",
            "description": "Китайские пельмени в супе",
            "instructions": "Приготовить фарш из свинины, имбиря, чеснока. Завернуть в тесто. Варить в бульоне 5-7 минут. Подавать с зеленым луком.",
            "cooking_time": 60,
            "category": "FIRST",
            "tags": ["SOUP", "HEARTY"],
            "ingredients": [
                {"name": "Мука", "amount": 300, "unit": "G"},
                {"name": "Свинина", "amount": 400, "unit": "G"},
                {"name": "Имбирь", "amount": 10, "unit": "G"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"},
                {"name": "Бульон", "amount": 1, "unit": "L"}
            ]
        },
        {
            "name": "Габао",
            "description": "Креветки с чесноком и чили",
            "instructions": "Обжарить креветки. Добавить чеснок, имбирь, чили. Добавить соевый соус и мед.",
            "cooking_time": 15,
            "category": "SECOND",
            "tags": ["QUICK", "SPICY"],
            "ingredients": [
                {"name": "Креветки", "amount": 500, "unit": "G"},
                {"name": "Чеснок", "amount": 4, "unit": "PC"},
                {"name": "Имбирь", "amount": 10, "unit": "G"},
                {"name": "Чили", "amount": 5, "unit": "G"},
                {"name": "Мед", "amount": 30, "unit": "G"}
            ]
        },
        {
            "name": "Яичный суп",
            "description": "Легкий суп с яйцом и кукурузой",
            "instructions": "Вскипятить бульон. Добавить кукурузу. Влить взбитое яйцо тонкой струйкой. Добавить зеленый лук и кунжутное масло.",
            "cooking_time": 10,
            "category": "FIRST",
            "tags": ["QUICK", "EASY"],
            "ingredients": [
                {"name": "Куриный бульон", "amount": 1, "unit": "L"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Кукуруза консервированная", "amount": 150, "unit": "G"},
                {"name": "Зеленый лук", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Острый суп Тофу",
            "description": "Суп с тофу и устричным соусом",
            "instructions": "Вскипятить бульон с имбирем. Добавить тофу, грибы. Приправить чили и устричным соусом.",
            "cooking_time": 20,
            "category": "FIRST",
            "tags": ["VEGETARIAN", "SPICY"],
            "ingredients": [
                {"name": "Тофу", "amount": 300, "unit": "G"},
                {"name": "Шитаке", "amount": 100, "unit": "G"},
                {"name": "Имбирь", "amount": 15, "unit": "G"},
                {"name": "Чили", "amount": 10, "unit": "G"},
                {"name": "Бульон", "amount": 800, "unit": "ML"}
            ]
        },
        {
            "name": "Цзяоцзы",
            "description": "Китайские пельмени со свининой и капустой",
            "instructions": "Приготовить тесто. Начинка из свинины, пекинской капусты, имбиря. Слепить цзяоцзы. Варить на пару или обжаривать.",
            "cooking_time": 90,
            "category": "SECOND",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Мука", "amount": 400, "unit": "G"},
                {"name": "Свинина", "amount": 400, "unit": "G"},
                {"name": "Пекинская капуста", "amount": 200, "unit": "G"},
                {"name": "Имбирь", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Баклажаны по-сычуаньски",
            "description": "Острые баклажаны с чесноком",
            "instructions": "Обжарить баклажаны. Добавить чеснок, имбирь, чили, соевый соус, уксус. Тушить 10 минут.",
            "cooking_time": 25,
            "category": "SECOND",
            "tags": ["VEGETARIAN", "SPICY"],
            "ingredients": [
                {"name": "Баклажаны", "amount": 3, "unit": "PC"},
                {"name": "Чеснок", "amount": 4, "unit": "PC"},
                {"name": "Соевый соус", "amount": 40, "unit": "ML"},
                {"name": "Рисовый уксус", "amount": 20, "unit": "ML"},
                {"name": "Чили", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Люйжоу",
            "description": "Блинчики с зеленым луком",
            "instructions": "Замесить тесто. Раскатать, смазать маслом, посыпать луком. Свернуть рулетом, затем улиткой. Раскатать. Обжарить до хруста.",
            "cooking_time": 45,
            "category": "SNACK",
            "tags": ["VEGETARIAN"],
            "ingredients": [
                {"name": "Мука", "amount": 300, "unit": "G"},
                {"name": "Зеленый лук", "amount": 100, "unit": "G"},
                {"name": "Масло растительное", "amount": 100, "unit": "ML"},
                {"name": "Соль", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Паровые булочки Баоцзы",
            "description": "Паровые булочки со свининой",
            "instructions": "Замесить дрожжевое тесто. Приготовить начинку из свинины с луком. Слепить булочки. Готовить на пару 15 минут.",
            "cooking_time": 120,
            "category": "SECOND",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Мука", "amount": 400, "unit": "G"},
                {"name": "Дрожжи", "amount": 7, "unit": "G"},
                {"name": "Свинина", "amount": 400, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"}
            ]
        },
        {
            "name": "Мою",
            "description": "Маринованный огурец по-китайски",
            "instructions": "Нарезать огурцы. Смешать с солью, сахаром, уксусом, соевым соусом, чесноком. Оставить на 1 час.",
            "cooking_time": 70,
            "category": "SNACK",
            "tags": ["QUICK", "EASY"],
            "ingredients": [
                {"name": "Огурцы", "amount": 500, "unit": "G"},
                {"name": "Соевый соус", "amount": 50, "unit": "ML"},
                {"name": "Уксус", "amount": 30, "unit": "ML"},
                {"name": "Сахар", "amount": 20, "unit": "G"},
                {"name": "Чеснок", "amount": 3, "unit": "PC"}
            ]
        },
        {
            "name": "Курица с апельсином",
            "description": "Сладкая курица в апельсиновом соусе",
            "instructions": "Обжарить курицу. Приготовить соус из апельсинового сока, соевого соуса, имбиря. Смешать, уварить до загустения.",
            "cooking_time": 35,
            "category": "SECOND",
            "tags": ["EASY"],
            "ingredients": [
                {"name": "Куриное филе", "amount": 500, "unit": "G"},
                {"name": "Апельсиновый сок", "amount": 150, "unit": "ML"},
                {"name": "Соевый соус", "amount": 50, "unit": "ML"},
                {"name": "Сахар", "amount": 50, "unit": "G"},
                {"name": "Имбирь", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Лапша Даньдань",
            "description": "Острая лапша с арахисом",
            "instructions": "Отварить лапшу. Приготовить соус из чили, арахисовой пасты, соевого соуса, уксуса. Смешать с лапшой.",
            "cooking_time": 20,
            "category": "SECOND",
            "tags": ["SPICY", "QUICK"],
            "ingredients": [
                {"name": "Лапша", "amount": 300, "unit": "G"},
                {"name": "Арахисовая паста", "amount": 50, "unit": "G"},
                {"name": "Соевый соус", "amount": 40, "unit": "ML"},
                {"name": "Чили", "amount": 10, "unit": "G"},
                {"name": "Зеленый лук", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Тофу по-мапо",
            "description": "Острый тофу с фаршем",
            "instructions": "Обжарить фарш с чили. Добавить тофу, соевый соус, бульон. Тушить 10 минут. Добавить крахмал для загустения.",
            "cooking_time": 25,
            "category": "SECOND",
            "tags": ["SPICY"],
            "ingredients": [
                {"name": "Тофу", "amount": 400, "unit": "G"},
                {"name": "Фарш свиной", "amount": 150, "unit": "G"},
                {"name": "Чили", "amount": 10, "unit": "G"},
                {"name": "Соевый соус", "amount": 30, "unit": "ML"},
                {"name": "Крахмал", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Рисовая каша Конджи",
            "description": "Рисовая каша с курицей",
            "instructions": "Варить рис в большом количестве воды 1 час. Добавить курицу, имбирь. Варить еще 30 минут. Подавать с зеленым луком.",
            "cooking_time": 90,
            "category": "BREAKFAST",
            "tags": ["EASY", "PP"],
            "ingredients": [
                {"name": "Рис", "amount": 150, "unit": "G"},
                {"name": "Курица", "amount": 200, "unit": "G"},
                {"name": "Имбирь", "amount": 15, "unit": "G"},
                {"name": "Вода", "amount": 1.5, "unit": "L"},
                {"name": "Зеленый лук", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Курица с кешью",
            "description": "Жареная курица с орехами кешью",
            "instructions": "Обжарить курицу. Добавить перец, лук. Добавить кешью и соус из соевого соуса, устричного соуса.",
            "cooking_time": 20,
            "category": "SECOND",
            "tags": ["QUICK"],
            "ingredients": [
                {"name": "Куриное филе", "amount": 500, "unit": "G"},
                {"name": "Кешью", "amount": 100, "unit": "G"},
                {"name": "Перец болгарский", "amount": 1, "unit": "PC"},
                {"name": "Соевый соус", "amount": 50, "unit": "ML"},
                {"name": "Устричный соус", "amount": 30, "unit": "ML"}
            ]
        },
        {
            "name": "Свиные ребрышки по-китайски",
            "description": "Ребрышки в сладком соусе",
            "instructions": "Обжарить ребрышки. Добавить соевый соус, мед, имбирь, чеснок. Тушить 1 час до мягкости.",
            "cooking_time": 75,
            "category": "SECOND",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Свиные ребра", "amount": 1, "unit": "KG"},
                {"name": "Соевый соус", "amount": 100, "unit": "ML"},
                {"name": "Мед", "amount": 80, "unit": "G"},
                {"name": "Имбирь", "amount": 20, "unit": "G"},
                {"name": "Чеснок", "amount": 4, "unit": "PC"}
            ]
        }
    ],

    # ==================== ЯПОНСКАЯ КУХНЯ (20 рецептов) ====================
    "JAPANESE": [
        {
            "name": "Суши",
            "description": "Рис с рыбой, завернутый в нори",
            "instructions": "Сварить рис для суши. Заправить рисовым уксусом. На лист нори выложить рис и начинку. Свернуть рулетом. Нарезать.",
            "cooking_time": 60,
            "category": "SECOND",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Рис для суши", "amount": 300, "unit": "G"},
                {"name": "Нори", "amount": 5, "unit": "PC"},
                {"name": "Лосось", "amount": 200, "unit": "G"},
                {"name": "Огурец", "amount": 1, "unit": "PC"},
                {"name": "Авокадо", "amount": 1, "unit": "PC"},
                {"name": "Рисовый уксус", "amount": 50, "unit": "ML"}
            ]
        },
        {
            "name": "Роллы Калифорния",
            "description": "Перевернутые роллы с крабом и авокадо",
            "instructions": "Приготовить рис. Выложить рис на нори, перевернуть. Выложить краб, авокадо, огурец. Свернуть. Обвалять в икре тобико.",
            "cooking_time": 45,
            "category": "SECOND",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Рис", "amount": 300, "unit": "G"},
                {"name": "Нори", "amount": 4, "unit": "PC"},
                {"name": "Крабовые палочки", "amount": 200, "unit": "G"},
                {"name": "Авокадо", "amount": 1, "unit": "PC"},
                {"name": "Икра тобико", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Рамен",
            "description": "Лапша в мясном бульоне с яйцом",
            "instructions": "Сварить свиной бульон. Отварить лапшу. Добавить чашу бульон, лапшу, свинину, яйцо, нори, зеленый лук.",
            "cooking_time": 180,
            "category": "FIRST",
            "tags": ["HEARTY", "SOUP"],
            "ingredients": [
                {"name": "Лапша рамен", "amount": 300, "unit": "G"},
                {"name": "Свинина", "amount": 400, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Нори", "amount": 2, "unit": "PC"},
                {"name": "Соевый соус", "amount": 100, "unit": "ML"}
            ]
        },
        {
            "name": "Удон",
            "description": "Толстая пшеничная лапша в бульоне",
            "instructions": "Отварить лапшу удон. Вскипятить даси (бульон из водорослей). Добавить соевый соус, мирин. Залить лапшу. Добавить зеленый лук.",
            "cooking_time": 25,
            "category": "FIRST",
            "tags": ["EASY"],
            "ingredients": [
                {"name": "Лапша удон", "amount": 400, "unit": "G"},
                {"name": "Водоросли комбу", "amount": 10, "unit": "G"},
                {"name": "Соевый соус", "amount": 60, "unit": "ML"},
                {"name": "Мирин", "amount": 30, "unit": "ML"},
                {"name": "Зеленый лук", "amount": 30, "unit": "G"}
            ]
        },
        {
            "name": "Темпура",
            "description": "Креветки и овощи в кляре во фритюре",
            "instructions": "Приготовить кляр из муки, яйца и ледяной воды. Обмакнуть креветки и овощи. Жарить во фритюре 2-3 минуты.",
            "cooking_time": 30,
            "category": "SECOND",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Креветки", "amount": 300, "unit": "G"},
                {"name": "Мука для темпуры", "amount": 100, "unit": "G"},
                {"name": "Яйца", "amount": 1, "unit": "PC"},                {"name": "Вода ледяная", "amount": 150, "unit": "ML"},
                {"name": "Баклажан", "amount": 0.5, "unit": "PC"},
                {"name": "Перец", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Тори-но-карааге",
            "description": "Японские жареные куриные кусочки",
            "instructions": "Замариновать курицу в соевом соусе, имбире, чесноке. Обвалять в крахмале. Обжарить во фритюре до хруста.",
            "cooking_time": 40,
            "category": "SECOND",
            "tags": ["QUICK"],
            "ingredients": [
                {"name": "Куриные бедра", "amount": 600, "unit": "G"},
                {"name": "Соевый соус", "amount": 60, "unit": "ML"},
                {"name": "Имбирь", "amount": 15, "unit": "G"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"},
                {"name": "Кукурузный крахмал", "amount": 80, "unit": "G"}
            ]
        },
        {
            "name": "Мисо-суп",
            "description": "Традиционный суп с пастой мисо и тофу",
            "instructions": "Сделать даси из водорослей и бонито. Растворить пасту мисо. Добавить тофу, водоросли вакаме, зеленый лук.",
            "cooking_time": 20,
            "category": "FIRST",
            "tags": ["VEGETARIAN", "EASY", "QUICK"],
            "ingredients": [
                {"name": "Паста мисо", "amount": 50, "unit": "G"},
                {"name": "Тофу", "amount": 200, "unit": "G"},
                {"name": "Водоросли вакаме", "amount": 5, "unit": "G"},
                {"name": "Бульон даси", "amount": 800, "unit": "ML"},
                {"name": "Зеленый лук", "amount": 15, "unit": "G"}
            ]
        },
        {
            "name": "Окономияки",
            "description": "Японская пицца с капустой и морепродуктами",
            "instructions": "Смешать капусту, муку, яйца, воду. Добавить креветки, бекон. Жарить на сковороде. Полить соусом окономияки, майонезом, посыпать сушеным тунцом.",
            "cooking_time": 30,
            "category": "SECOND",
            "tags": ["EASY"],
            "ingredients": [
                {"name": "Капуста", "amount": 300, "unit": "G"},
                {"name": "Мука", "amount": 150, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Креветки", "amount": 100, "unit": "G"},
                {"name": "Бекон", "amount": 80, "unit": "G"},
                {"name": "Соус окономияки", "amount": 50, "unit": "ML"}
            ]
        },
        {
            "name": "Такояки",
            "description": "Шарики с осьминогом во фритюре",
            "instructions": "Приготовить тесто из муки, яиц, даси. В специальную форму вылить тесто, добавить кусочки осьминога, имбирь. Переворачивать до золотистого цвета. Полить соусом и майонезом.",
            "cooking_time": 30,
            "category": "SNACK",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Мука", "amount": 200, "unit": "G"},
                {"name": "Осьминог", "amount": 150, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Даси", "amount": 400, "unit": "ML"},
                {"name": "Зеленый лук", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Гёдза",
            "description": "Японские пельмени с мясом и капустой",
            "instructions": "Приготовить начинку из свинины, капусты, чеснока, имбиря. Завернуть в тесто гёдза. Обжарить с одной стороны, добавить воду, накрыть крышкой до готовности.",
            "cooking_time": 50,
            "category": "SECOND",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Тесто гёдза", "amount": 40, "unit": "PC"},
                {"name": "Свинина", "amount": 300, "unit": "G"},
                {"name": "Капуста", "amount": 200, "unit": "G"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"},
                {"name": "Имбирь", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Якитори",
            "description": "Курица на бамбуковых шпажках с соусом таре",
            "instructions": "Нанизать кусочки курицы на шпажки. Жарить на гриле. Периодически смазывать соусом таре (соевый соус, мирин, сахар).",
            "cooking_time": 25,
            "category": "SECOND",
            "tags": ["GRILL", "QUICK"],
            "ingredients": [
                {"name": "Куриное филе", "amount": 500, "unit": "G"},
                {"name": "Соевый соус", "amount": 100, "unit": "ML"},
                {"name": "Мирин", "amount": 50, "unit": "ML"},
                {"name": "Сахар", "amount": 30, "unit": "G"}
            ]
        },
        {
            "name": "Кацудон",
            "description": "Свиная котлета с яйцом на рисе",
            "instructions": "Обжарить свиную отбивную в панировке. Отдельно в кастрюльке разогреть соус из даси, соевого соуса, лука. Добавить котлету, залить взбитым яйцом. Подавать на рисе.",
            "cooking_time": 35,
            "category": "SECOND",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Свиная вырезка", "amount": 400, "unit": "G"},
                {"name": "Яйца", "amount": 4, "unit": "PC"},
                {"name": "Рис", "amount": 300, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Соевый соус", "amount": 50, "unit": "ML"}
            ]
        },
        {
            "name": "Омурайсу",
            "description": "Омлет с рисом, политой кетчупом",
            "instructions": "Приготовить рис с курицей и луком, заправить кетчупом. Завернуть рис в тонкий омлет. Полить кетчупом сверху.",
            "cooking_time": 25,
            "category": "SECOND",
            "tags": ["KIDS", "QUICK"],
            "ingredients": [
                {"name": "Рис", "amount": 300, "unit": "G"},
                {"name": "Курица", "amount": 150, "unit": "G"},
                {"name": "Яйца", "amount": 3, "unit": "PC"},
                {"name": "Лук", "amount": 0.5, "unit": "PC"},
                {"name": "Кетчуп", "amount": 80, "unit": "ML"}
            ]
        },
        {
            "name": "Онигири",
            "description": "Рисовые треугольники с начинкой",
            "instructions": "Сварить рис. Сформировать треугольники, внутрь положить начинку (лосось, умебоши, тунец с майонезом). Завернуть в нори.",
            "cooking_time": 30,
            "category": "SNACK",
            "tags": ["EASY", "PP"],
            "ingredients": [
                {"name": "Рис", "amount": 400, "unit": "G"},
                {"name": "Лосось соленый", "amount": 150, "unit": "G"},
                {"name": "Нори", "amount": 4, "unit": "PC"},
                {"name": "Соль", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Моти",
            "description": "Рисовые лепешки со сладкой пастой",
            "instructions": "Сварить клейкий рис. Растолочь в ступке до пастообразного состояния. Сформировать лепешки. Положить внутрь пасту из красной фасоли (анко).",
            "cooking_time": 60,
            "category": "DESSERT",
            "tags": ["VEGETARIAN"],
            "ingredients": [
                {"name": "Клейкий рис", "amount": 300, "unit": "G"},
                {"name": "Сахар", "amount": 50, "unit": "G"},
                {"name": "Паста анко", "amount": 200, "unit": "G"},
                {"name": "Кукурузный крахмал", "amount": 30, "unit": "G"}
            ]
        },
        {
            "name": "Дораяки",
            "description": "Медовые блинчики с пастой анко",
            "instructions": "Приготовить блинчики из муки, меда, яиц. Остудить. Вложить между двумя блинчиками пасту анко.",
            "cooking_time": 30,
            "category": "DESSERT",
            "tags": ["KIDS", "EASY"],
            "ingredients": [
                {"name": "Мука", "amount": 150, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Мед", "amount": 50, "unit": "G"},
                {"name": "Сахар", "amount": 50, "unit": "G"},
                {"name": "Паста анко", "amount": 200, "unit": "G"}
            ]
        },
        {
            "name": "Пудинг Пурин",
            "description": "Японский заварной пудинг",
            "instructions": "Сделать карамель. Приготовить заварную смесь из яиц, молока, сахара. Залить в формочки, выпекать на водяной бане 30 минут.",
            "cooking_time": 60,
            "category": "DESSERT",
            "tags": ["EASY"],
            "ingredients": [
                {"name": "Молоко", "amount": 500, "unit": "ML"},
                {"name": "Яйца", "amount": 3, "unit": "PC"},
                {"name": "Сахар", "amount": 100, "unit": "G"},
                {"name": "Ваниль", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Васаби",
            "description": "Острая приправа из хрена васаби",
            "instructions": "Натереть корень васаби на мелкой терке. Дать настояться 10 минут для раскрытия остроты.",
            "cooking_time": 15,
            "category": "SAUCE",
            "tags": ["QUICK", "SPICY", "PP"],
            "ingredients": [
                {"name": "Корень васаби", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Терияки соус",
            "description": "Сладко-соленый соус для мяса и рыбы",
            "instructions": "Смешать соевый соус, мирин, сахар. Варить на медленном огне до загустения. Остудить.",
            "cooking_time": 15,
            "category": "SAUCE",
            "tags": ["QUICK", "EASY"],
            "ingredients": [
                {"name": "Соевый соус", "amount": 100, "unit": "ML"},
                {"name": "Мирин", "amount": 100, "unit": "ML"},
                {"name": "Сахар", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Тонкацу соус",
            "description": "Густой фруктовый соус для котлет",
            "instructions": "Смешать кетчуп, соус ворчестер, соевый соус, сахар, яблочное пюре. Варить 10 минут.",
            "cooking_time": 20,
            "category": "SAUCE",
            "tags": ["EASY"],
            "ingredients": [
                {"name": "Кетчуп", "amount": 100, "unit": "ML"},
                {"name": "Ворчестер соус", "amount": 30, "unit": "ML"},
                {"name": "Соевый соус", "amount": 20, "unit": "ML"},
                {"name": "Яблочное пюре", "amount": 50, "unit": "G"},
                {"name": "Сахар", "amount": 30, "unit": "G"}
            ]
        }
    ],

    # ==================== ФРАНЦУЗСКАЯ КУХНЯ (FRE) ====================
    "FRENCH": [
        {
            "name": "Круассан",
            "description": "Слоеный рогалик из дрожжевого теста",
            "instructions": "Приготовить слоеное тесто. Раскатать, нарезать треугольниками. Свернуть в рогалики. Дать подойти. Выпекать 15 минут при 200°C.",
            "cooking_time": 240,
            "category": "BREAKFAST",
            "tags": ["OVEN", "GOURMET"],
            "ingredients": [
                {"name": "Мука", "amount": 500, "unit": "G"},
                {"name": "Масло сливочное", "amount": 250, "unit": "G"},
                {"name": "Молоко", "amount": 200, "unit": "ML"},
                {"name": "Дрожжи", "amount": 10, "unit": "G"},
                {"name": "Сахар", "amount": 50, "unit": "G"},
                {"name": "Яйца", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Киш Лорен",
            "description": "Открытый пирог с беконом и сыром",
            "instructions": "Раскатать песочное тесто. Выложить в форму. Начинка: бекон, лук, смесь из яиц, сливок и сыра. Выпекать 35 минут.",
            "cooking_time": 60,
            "category": "SECOND",
            "tags": ["OVEN"],
            "ingredients": [
                {"name": "Мука", "amount": 200, "unit": "G"},
                {"name": "Масло сливочное", "amount": 100, "unit": "G"},
                {"name": "Бекон", "amount": 200, "unit": "G"},
                {"name": "Яйца", "amount": 3, "unit": "PC"},
                {"name": "Сливки", "amount": 200, "unit": "ML"},
                {"name": "Сыр Грюйер", "amount": 150, "unit": "G"}
            ]
        },
        {
            "name": "Фуа-гра",
            "description": "Паштет из утиной печени",
            "instructions": "Удалить жилы из печени. Посолить, поперчить. Добавить коньяк. Выложить в форму, запекать на водяной бане 40 минут. Охладить 12 часов.",
            "cooking_time": 60,
            "category": "SNACK",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Утиная печень", "amount": 500, "unit": "G"},
                {"name": "Коньяк", "amount": 50, "unit": "ML"},
                {"name": "Соль", "amount": 10, "unit": "G"},
                {"name": "Перец", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Рататуй",
            "description": "Овощное рагу из баклажанов и кабачков",
            "instructions": "Нарезать овощи. Выложить слоями в форму: соус из томатов, затем баклажаны, кабачки, перец, лук. Запекать 1 час при 160°C.",
            "cooking_time": 80,
            "category": "SECOND",
            "tags": ["VEGETARIAN", "LENTEN", "OVEN"],
            "ingredients": [
                {"name": "Баклажаны", "amount": 2, "unit": "PC"},
                {"name": "Кабачки", "amount": 2, "unit": "PC"},
                {"name": "Перец болгарский", "amount": 2, "unit": "PC"},
                {"name": "Помидоры", "amount": 4, "unit": "PC"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Тимьян", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Беф Бургиньон",
            "description": "Говядина, тушенная в красном вине",
            "instructions": "Обжарить мясо. Добавить лук, морковь, чеснок. Залить красным вином и бульоном. Тушить 3 часа. Добавить грибы и лук-жемчуг в конце.",
            "cooking_time": 210,
            "category": "SECOND",
            "tags": ["HEARTY", "GOURMET"],
            "ingredients": [
                {"name": "Говядина", "amount": 1, "unit": "KG"},
                {"name": "Красное вино", "amount": 750, "unit": "ML"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Морковь", "amount": 2, "unit": "PC"},
                {"name": "Шампиньоны", "amount": 200, "unit": "G"},
                {"name": "Бекон", "amount": 150, "unit": "G"}
            ]
        },
        {
            "name": "Утиное конфи",
            "description": "Утиные ножки, приготовленные в жире",
            "instructions": "Натереть ножки солью и травами на 24 часа. Залить утиным жиром. Томить при 100°C 4 часа. Затем обжарить до хруста.",
            "cooking_time": 300,
            "category": "SECOND",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Утиные ножки", "amount": 4, "unit": "PC"},
                {"name": "Утиный жир", "amount": 800, "unit": "G"},
                {"name": "Чеснок", "amount": 4, "unit": "PC"},
                {"name": "Тимьян", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Буйабес",
            "description": "Провансальский суп из рыбы и морепродуктов",
            "instructions": "Обжарить лук, томаты. Добавить рыбу, креветки, мидии. Залить рыбным бульоном с шафраном. Варить 30 минут. Подавать с гренками и соусом руй.",
            "cooking_time": 60,
            "category": "FIRST",
            "tags": ["SOUP", "GOURMET"],
            "ingredients": [
                {"name": "Рыбное ассорти", "amount": 800, "unit": "G"},
                {"name": "Креветки", "amount": 200, "unit": "G"},
                {"name": "Мидии", "amount": 200, "unit": "G"},
                {"name": "Томаты", "amount": 400, "unit": "G"},
                {"name": "Шафран", "amount": 1, "unit": "PINCH"}
            ]
        },
        {
            "name": "Суп с луком по-французски",
            "description": "Карамелизованный луковый суп под сырной корочкой",
            "instructions": "Карамелизовать лук на масле 30 минут. Добавить бульон, тимьян. Варить 20 минут. Разлить в горшочки, положить гренки с сыром. Запечь до золотистой корочки.",
            "cooking_time": 70,
            "category": "FIRST",
            "tags": ["SOUP", "OVEN"],
            "ingredients": [
                {"name": "Лук", "amount": 1, "unit": "KG"},
                {"name": "Говяжий бульон", "amount": 1.5, "unit": "L"},
                {"name": "Сыр Грюйер", "amount": 150, "unit": "G"},
                {"name": "Багет", "amount": 4, "unit": "PC"},
                {"name": "Масло сливочное", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Крем-брюле",
            "description": "Заварной крем с карамельной корочкой",
            "instructions": "Нагреть сливки с ванилью. Смешать желтки с сахаром. Соединить, разлить в формочки. Выпекать на водяной бане. Охладить. Посыпать сахаром и карамелизовать горелкой.",
            "cooking_time": 60,
            "category": "DESSERT",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Сливки 33%", "amount": 500, "unit": "ML"},
                {"name": "Желтки", "amount": 6, "unit": "PC"},
                {"name": "Сахар", "amount": 100, "unit": "G"},
                {"name": "Ваниль", "amount": 1, "unit": "PC"},
                {"name": "Тростниковый сахар", "amount": 30, "unit": "G"}
            ]
        },
        {
            "name": "Макарон",
            "description": "Французское миндальное печенье",
            "instructions": "Смешать миндальную муку с сахарной пудрой. Взбить белки с сахаром. Соединить. Отсадить круги. Выпекать 12 минут. Соединить с начинкой (ганаш, джем).",
            "cooking_time": 60,
            "category": "DESSERT",
            "tags": ["GOURMET", "GLUTEN_FREE"],
            "ingredients": [
                {"name": "Миндальная мука", "amount": 150, "unit": "G"},
                {"name": "Сахарная пудра", "amount": 150, "unit": "G"},
                {"name": "Яичные белки", "amount": 3, "unit": "PC"},
                {"name": "Сахар", "amount": 50, "unit": "G"},
                {"name": "Шоколадный ганаш", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Тарт Татен",
            "description": "Перевернутый яблочный пирог",
            "instructions": "Карамелизовать сахар с маслом. Выложить яблоки. Накрыть тестом. Выпекать 30 минут. Перевернуть.",
            "cooking_time": 50,
            "category": "DESSERT",
            "tags": ["OVEN"],
            "ingredients": [
                {"name": "Яблоки", "amount": 6, "unit": "PC"},
                {"name": "Сахар", "amount": 150, "unit": "G"},
                {"name": "Масло сливочное", "amount": 100, "unit": "G"},
                {"name": "Слоеное тесто", "amount": 250, "unit": "G"}
            ]
        },
        {
            "name": "Птифур",
            "description": "Маленькое печенье к чаю",
            "instructions": "Замесить песочное тесто. Раскатать, вырезать формочками. Выпекать 10 минут.",
            "cooking_time": 30,
            "category": "DESSERT",
            "tags": ["EASY"],
            "ingredients": [
                {"name": "Мука", "amount": 200, "unit": "G"},
                {"name": "Масло сливочное", "amount": 100, "unit": "G"},
                {"name": "Сахар", "amount": 50, "unit": "G"},
                {"name": "Яйца", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Суп-пюре из тыквы",
            "description": "Нежный крем-суп из тыквы",
            "instructions": "Обжарить лук, тыкву. Добавить бульон. Варить до мягкости. Пюрировать. Добавить сливки. Подавать с тыквенными семечками.",
            "cooking_time": 35,
            "category": "FIRST",
            "tags": ["VEGETARIAN", "QUICK"],
            "ingredients": [
                {"name": "Тыква", "amount": 800, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Сливки", "amount": 100, "unit": "ML"},
                {"name": "Бульон", "amount": 500, "unit": "ML"},
                {"name": "Тыквенные семечки", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Салат Нисуаз",
            "description": "Салат с тунцом, яйцом и анчоусами",
            "instructions": "Выложить листья салата. Добавить тунец, яйца, помидоры, оливки, анчоусы, фасоль. Заправить оливковым маслом и лимоном.",
            "cooking_time": 20,
            "category": "SALAD",
            "tags": ["EASY", "PP"],
            "ingredients": [
                {"name": "Тунец консервированный", "amount": 200, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Помидоры черри", "amount": 150, "unit": "G"},
                {"name": "Оливки", "amount": 80, "unit": "G"},
                {"name": "Анчоусы", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Фондю",
            "description": "Расплавленный сыр для обмакивания хлеба",
            "instructions": "Натереть сыр. Растопить с белым вином и чесноком. Подавать с кубиками хлеба.",
            "cooking_time": 20,
            "category": "SECOND",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Сыр Грюйер", "amount": 200, "unit": "G"},
                {"name": "Сыр Эмменталь", "amount": 200, "unit": "G"},
                {"name": "Белое вино", "amount": 200, "unit": "ML"},
                {"name": "Чеснок", "amount": 1, "unit": "PC"},
                {"name": "Багет", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Гратен Дофинуа",
            "description": "Запеченный картофель со сливками",
            "instructions": "Нарезать картофель тонкими кружками. Выложить в форму, залить сливками с чесноком и мускатным орехом. Запекать 1 час.",
            "cooking_time": 80,
            "category": "SECOND",
            "tags": ["VEGETARIAN", "OVEN"],
            "ingredients": [
                {"name": "Картофель", "amount": 1, "unit": "KG"},
                {"name": "Сливки 33%", "amount": 500, "unit": "ML"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"},
                {"name": "Мускатный орех", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Соус Бешамель",
            "description": "Классический белый соус",
            "instructions": "Растопить масло, добавить муку, обжарить. Постепенно влить молоко, постоянно помешивая до загустения.",
            "cooking_time": 15,
            "category": "SAUCE",
            "tags": ["QUICK", "EASY"],
            "ingredients": [
                {"name": "Молоко", "amount": 500, "unit": "ML"},
                {"name": "Масло сливочное", "amount": 50, "unit": "G"},
                {"name": "Мука", "amount": 50, "unit": "G"},
                {"name": "Мускатный орех", "amount": 3, "unit": "G"}
            ]
        },
        {
            "name": "Соус Голландез",
            "description": "Яично-масляный соус к рыбе и овощам",
            "instructions": "Растопить сливочное масло. Взбить желтки с лимонным соком на водяной бане. Постепенно влить масло.",
            "cooking_time": 20,
            "category": "SAUCE",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Желтки", "amount": 3, "unit": "PC"},
                {"name": "Масло сливочное", "amount": 150, "unit": "G"},
                {"name": "Лимонный сок", "amount": 15, "unit": "ML"},
                {"name": "Соль", "amount": 3, "unit": "G"}
            ]
        },
        {
            "name": "Сливочный соус с шампиньонами",
            "description": "Нежный грибной соус",
            "instructions": "Обжарить грибы с луком. Добавить сливки. Варить до загустения. Посолить, поперчить.",
            "cooking_time": 15,
            "category": "SAUCE",
            "tags": ["QUICK", "VEGETARIAN"],
            "ingredients": [
                {"name": "Шампиньоны", "amount": 200, "unit": "G"},
                {"name": "Сливки 20%", "amount": 200, "unit": "ML"},
                {"name": "Лук", "amount": 0.5, "unit": "PC"},
                {"name": "Масло сливочное", "amount": 20, "unit": "G"}
            ]
        }
    ],

    # ==================== УЗБЕКСКАЯ КУХНЯ (UZB) ====================
    "UZBEK": [
        {
            "name": "Плов",
            "description": "Рассыпчатый плов с бараниной и морковью",
            "instructions": "Обжарить мясо до корочки. Добавить лук, морковь. Залить водой, добавить зиру, барбарис. Засыпать рис. Томить под крышкой 20 минут.",
            "cooking_time": 90,
            "category": "SECOND",
            "tags": ["HEARTY", "GOURMET"],
            "ingredients": [
                {"name": "Баранина", "amount": 600, "unit": "G"},
                {"name": "Рис", "amount": 500, "unit": "G"},
                {"name": "Морковь", "amount": 500, "unit": "G"},
                {"name": "Лук", "amount": 300, "unit": "G"},
                {"name": "Чеснок", "amount": 1, "unit": "PC"},
                {"name": "Зира", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Самса",
            "description": "Слоеные треугольники с мясом",
            "instructions": "Раскатать слоеное тесто. Нарезать квадратами. Выложить фарш из баранины с луком. Сформировать треугольники. Выпекать 30 минут.",
            "cooking_time": 60,
            "category": "SNACK",
            "tags": ["OVEN", "HEARTY"],
            "ingredients": [
                {"name": "Слоеное тесто", "amount": 500, "unit": "G"},
                {"name": "Баранина", "amount": 400, "unit": "G"},
                {"name": "Лук", "amount": 200, "unit": "G"},
                {"name": "Кунжут", "amount": 20, "unit": "G"},
                {"name": "Зира", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Лагман",
            "description": "Лапша с мясом и овощами в соусе",
            "instructions": "Отварить лапшу. Обжарить мясо. Добавить лук, морковь, перец, баклажаны. Залить томатным соусом и бульоном. Тушить 30 минут. Подавать с лапшой и зеленью.",
            "cooking_time": 80,
            "category": "FIRST",
            "tags": ["SOUP", "HEARTY"],
            "ingredients": [
                {"name": "Лапша лагман", "amount": 400, "unit": "G"},
                {"name": "Говядина", "amount": 500, "unit": "G"},
                {"name": "Морковь", "amount": 2, "unit": "PC"},
                {"name": "Перец болгарский", "amount": 2, "unit": "PC"},
                {"name": "Редис дайкон", "amount": 200, "unit": "G"}
            ]
        },
        {
            "name": "Манты",
            "description": "Крупные паровые пельмени с мясом и тыквой",
            "instructions": "Замесить тесто. Приготовить начинку из фарша, тыквы, лука, зиры. Раскатать тесто, сформировать манты. Варить на пару 40 минут.",
            "cooking_time": 90,
            "category": "SECOND",
            "tags": ["HEARTY", "MULTICOOKER"],
            "ingredients": [
                {"name": "Мука", "amount": 500, "unit": "G"},
                {"name": "Баранина", "amount": 500, "unit": "G"},
                {"name": "Тыква", "amount": 300, "unit": "G"},
                {"name": "Лук", "amount": 300, "unit": "G"},
                {"name": "Зира", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Шурпа",
            "description": "Наваристый мясной суп с овощами",
            "instructions": "Обжарить мясо с луком. Добавить морковь, картофель, помидоры, перец. Залить водой. Варить 1.5 часа. Добавить зелень.",
            "cooking_time": 120,
            "category": "FIRST",
            "tags": ["SOUP", "HEARTY"],
            "ingredients": [
                {"name": "Баранина", "amount": 600, "unit": "G"},
                {"name": "Картофель", "amount": 4, "unit": "PC"},
                {"name": "Морковь", "amount": 2, "unit": "PC"},
                {"name": "Помидоры", "amount": 3, "unit": "PC"},
                {"name": "Лук", "amount": 2, "unit": "PC"}
            ]
        },
        {
            "name": "Лепешка",
            "description": "Узбекская хлебная лепешка",
            "instructions": "Замесить дрожжевое тесто. Сформировать лепешку. Сделать узоры вилкой. Смазать яйцом, посыпать кунжутом. Выпекать 20 минут.",
            "cooking_time": 90,
            "category": "SECOND",
            "tags": ["OVEN", "EASY"],
            "ingredients": [
                {"name": "Мука", "amount": 500, "unit": "G"},
                {"name": "Дрожжи", "amount": 10, "unit": "G"},
                {"name": "Вода", "amount": 250, "unit": "ML"},
                {"name": "Кунжут", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Куурдак",
            "description": "Жаркое из печени с картофелем",
            "instructions": "Обжарить мясо и печень. Добавить лук, затем картофель. Жарить до готовности картофеля. Подавать с зеленью.",
            "cooking_time": 40,
            "category": "SECOND",
            "tags": ["HEARTY", "QUICK"],
            "ingredients": [
                {"name": "Баранина", "amount": 300, "unit": "G"},
                {"name": "Печень баранья", "amount": 300, "unit": "G"},
                {"name": "Картофель", "amount": 500, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"}
            ]
        },
        {
            "name": "Чучвара",
            "description": "Маленькие пельмени в бульоне",
            "instructions": "Приготовить тесто. Фарш из баранины с луком. Слепить маленькие пельмени. Отварить в бульоне. Подавать с зеленью и сузьмой (кислое молоко).",
            "cooking_time": 70,
            "category": "FIRST",
            "tags": ["SOUP"],
            "ingredients": [
                {"name": "Мука", "amount": 400, "unit": "G"},
                {"name": "Баранина", "amount": 400, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Сузьма", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Салат Ачик-Чучук",
            "description": "Салат из помидоров, лука и зелени",
            "instructions": "Нарезать помидоры дольками, лук полукольцами. Добавить соль, перец, зиру. Заправить растительным маслом.",
            "cooking_time": 10,
            "category": "SALAD",
            "tags": ["VEGETARIAN", "QUICK", "EASY"],
            "ingredients": [
                {"name": "Помидоры", "amount": 500, "unit": "G"},
                {"name": "Лук репчатый", "amount": 150, "unit": "G"},
                {"name": "Масло растительное", "amount": 30, "unit": "ML"},
                {"name": "Зира", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Норин",
            "description": "Лапша с мясом и редькой",
            "instructions": "Отварить лапшу. Отдельно обжарить мясо с луком и редькой. Подавать лапшу с мясом и бульоном, посыпать зеленью.",
            "cooking_time": 60,
            "category": "SECOND",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Лапша", "amount": 400, "unit": "G"},
                {"name": "Говядина", "amount": 500, "unit": "G"},
                {"name": "Редька зеленая", "amount": 300, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"}
            ]
        },
        {
            "name": "Самбуса вареник",
            "description": "Вареники с зеленью и яйцом",
            "instructions": "Замесить тесто. Начинка из зелени (шпинат, кинза, укроп) и вареного яйца. Сформировать вареники. Варить 5 минут. Подавать с сузьмой.",
            "cooking_time": 50,
            "category": "SECOND",
            "tags": ["VEGETARIAN"],
            "ingredients": [
                {"name": "Мука", "amount": 400, "unit": "G"},
                {"name": "Шпинат", "amount": 200, "unit": "G"},
                {"name": "Кинза", "amount": 100, "unit": "G"},
                {"name": "Яйца", "amount": 3, "unit": "PC"}
            ]
        },
        {
            "name": "Халяим",
            "description": "Пшеничная каша с мясом",
            "instructions": "Замочить пшеницу на ночь. Варить с мясом 3-4 часа до полного разваривания. Постоянно помешивать. Подавать с корицей и сахаром.",
            "cooking_time": 300,
            "category": "SECOND",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Пшеница", "amount": 500, "unit": "G"},
                {"name": "Баранина", "amount": 400, "unit": "G"},
                {"name": "Молоко", "amount": 500, "unit": "ML"},
                {"name": "Корица", "amount": 5, "unit": "G"}
            ]
        },
        {
            "name": "Чак-чак",
            "description": "Сладкое блюдо из теста с медом",
            "instructions": "Нарезать тесто тонкой соломкой. Обжарить во фритюре. Залить горячим медом с сахаром. Сформировать горку.",
            "cooking_time": 45,
            "category": "DESSERT",
            "tags": ["GOURMET"],
            "ingredients": [
                {"name": "Мука", "amount": 300, "unit": "G"},
                {"name": "Яйца", "amount": 3, "unit": "PC"},
                {"name": "Мед", "amount": 150, "unit": "G"},
                {"name": "Сахар", "amount": 50, "unit": "G"},
                {"name": "Масло для фритюра", "amount": 300, "unit": "ML"}
            ]
        },
        {
            "name": "Халвайтар",
            "description": "Мучная халва с маслом",
            "instructions": "Обжарить муку на масле до золотистого цвета. Добавить сахар, воду. Варить до загустения. Охладить.",
            "cooking_time": 40,
            "category": "DESSERT",
            "tags": ["EASY"],
            "ingredients": [
                {"name": "Мука", "amount": 200, "unit": "G"},
                {"name": "Сливочное масло", "amount": 150, "unit": "G"},
                {"name": "Сахар", "amount": 150, "unit": "G"},
                {"name": "Вода", "amount": 100, "unit": "ML"}
            ]
        },
        {
            "name": "Каймак",
            "description": "Сливки с медом к чаю",
            "instructions": "Собрать пенки с кипяченого молока. Охладить. Подавать с медом и лепешкой.",
            "cooking_time": 30,
            "category": "DRINK",
            "tags": ["EASY", "BREAKFAST"],
            "ingredients": [
                {"name": "Молоко", "amount": 1, "unit": "L"},
                {"name": "Мед", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Уйгурский лагман",
            "description": "Лагман с острым соусом",
            "instructions": "Приготовить лапшу. Обжарить мясо с овощами и чили. Добавить соевый соус и уксус. Подавать с лапшой.",
            "cooking_time": 70,
            "category": "SECOND",
            "tags": ["SPICY", "HEARTY"],
            "ingredients": [
                {"name": "Лапша", "amount": 400, "unit": "G"},
                {"name": "Говядина", "amount": 500, "unit": "G"},
                {"name": "Перец чили", "amount": 10, "unit": "G"},
                {"name": "Соевый соус", "amount": 50, "unit": "ML"},
                {"name": "Уксус", "amount": 20, "unit": "ML"}
            ]
        },
        {
            "name": "Зеленый чай с чабрецом",
            "description": "Традиционный чай",
            "instructions": "Заварить зеленый чай. Добавить чабрец. Настоять 5 минут.",
            "cooking_time": 10,
            "category": "DRINK",
            "tags": ["QUICK", "PP"],
            "ingredients": [
                {"name": "Зеленый чай", "amount": 10, "unit": "G"},
                {"name": "Чабрец", "amount": 5, "unit": "G"},
                {"name": "Вода", "amount": 1, "unit": "L"}
            ]
        }
    ],

    # ==================== ЕВРОПЕЙСКАЯ КУХНЯ (EUR) ====================
    "EUROPEAN": [
        {
            "name": "Рёбра BBQ",
            "description": "Свиные ребра в дымном соусе барбекю",
            "instructions": "Натереть ребра специями. Запекать 2 часа при 150°C. Смазать соусом. Допекать 30 минут при 180°C.",
            "cooking_time": 150,
            "category": "SECOND",
            "tags": ["OVEN", "HEARTY"],
            "ingredients": [
                {"name": "Свиные ребра", "amount": 1, "unit": "KG"},
                {"name": "Соус BBQ", "amount": 200, "unit": "ML"},
                {"name": "Паприка", "amount": 10, "unit": "G"},
                {"name": "Чеснок", "amount": 4, "unit": "PC"}
            ]
        },
        {
            "name": "Шницель по-венски",
            "description": "Тонкая отбивная в панировке",
            "instructions": "Отбить телятину. Обвалять в муке, яйце, сухарях. Обжарить во фритюре до золотистого цвета.",
            "cooking_time": 25,
            "category": "SECOND",
            "tags": ["QUICK"],
            "ingredients": [
                {"name": "Телятина", "amount": 600, "unit": "G"},
                {"name": "Мука", "amount": 50, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Сухари", "amount": 100, "unit": "G"},
                {"name": "Лимон", "amount": 0.5, "unit": "PC"}
            ]
        },
        {
            "name": "Цезарь с курицей",
            "description": "Салат с курицей, пармезаном и сухариками",
            "instructions": "Обжарить курицу. Смешать листья салата, сухарики, пармезан. Заправить соусом Цезарь. Выложить курицу.",
            "cooking_time": 20,
            "category": "SALAD",
            "tags": ["QUICK", "EASY"],
            "ingredients": [
                {"name": "Куриное филе", "amount": 300, "unit": "G"},
                {"name": "Салат романо", "amount": 200, "unit": "G"},
                {"name": "Пармезан", "amount": 50, "unit": "G"},
                {"name": "Сухарики", "amount": 80, "unit": "G"},
                {"name": "Соус Цезарь", "amount": 100, "unit": "ML"}
            ]
        },
        {
            "name": "Греческий салат",
            "description": "Салат с фетой, оливками и овощами",
            "instructions": "Нарезать помидоры, огурцы, перец, лук. Добавить оливки и кубики феты. Заправить оливковым маслом и орегано.",
            "cooking_time": 10,
            "category": "SALAD",
            "tags": ["VEGETARIAN", "QUICK", "EASY"],
            "ingredients": [
                {"name": "Помидоры", "amount": 300, "unit": "G"},
                {"name": "Огурцы", "amount": 200, "unit": "G"},
                {"name": "Фета", "amount": 150, "unit": "G"},
                {"name": "Оливки", "amount": 80, "unit": "G"},
                {"name": "Масло оливковое", "amount": 30, "unit": "ML"}
            ]
        },
        {
            "name": "Чизкейк Нью-Йорк",
            "description": "Плотный сливочный чизкейк",
            "instructions": "Сделать основу из печенья и масла. Взбить сливочный сыр, сахар, яйца. Вылить на основу. Выпекать 1 час на водяной бане.",
            "cooking_time": 90,
            "category": "DESSERT",
            "tags": ["OVEN", "GOURMET"],
            "ingredients": [
                {"name": "Печенье", "amount": 200, "unit": "G"},
                {"name": "Масло сливочное", "amount": 100, "unit": "G"},
                {"name": "Сливочный сыр", "amount": 600, "unit": "G"},
                {"name": "Сахар", "amount": 150, "unit": "G"},
                {"name": "Яйца", "amount": 3, "unit": "PC"}
            ]
        },
        {
            "name": "Брауни",
            "description": "Шоколадное пирожное с орехами",
            "instructions": "Растопить шоколад с маслом. Взбить яйца с сахаром. Смешать, добавить муку и орехи. Выпекать 25 минут.",
            "cooking_time": 35,
            "category": "DESSERT",
            "tags": ["QUICK", "KIDS"],
            "ingredients": [
                {"name": "Темный шоколад", "amount": 200, "unit": "G"},
                {"name": "Масло сливочное", "amount": 150, "unit": "G"},
                {"name": "Сахар", "amount": 200, "unit": "G"},
                {"name": "Яйца", "amount": 3, "unit": "PC"},
                {"name": "Грецкие орехи", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Шоколадный фондан",
            "description": "Кекс с жидкой начинкой",
            "instructions": "Растопить шоколад с маслом. Взбить яйца с сахаром. Смешать, добавить муку. Выпекать 12 минут при 200°C.",
            "cooking_time": 20,
            "category": "DESSERT",
            "tags": ["GOURMET", "QUICK"],
            "ingredients": [
                {"name": "Темный шоколад", "amount": 100, "unit": "G"},
                {"name": "Масло сливочное", "amount": 80, "unit": "G"},
                {"name": "Яйца", "amount": 2, "unit": "PC"},
                {"name": "Сахар", "amount": 50, "unit": "G"},
                {"name": "Мука", "amount": 30, "unit": "G"}
            ]
        },
        {
            "name": "Картофель по-деревенски",
            "description": "Запеченный картофель со специями",
            "instructions": "Нарезать картофель дольками. Смешать с маслом, паприкой, чесноком. Запекать 40 минут при 200°C.",
            "cooking_time": 50,
            "category": "SECOND",
            "tags": ["VEGETARIAN", "OVEN", "EASY"],
            "ingredients": [
                {"name": "Картофель", "amount": 1, "unit": "KG"},
                {"name": "Масло растительное", "amount": 50, "unit": "ML"},
                {"name": "Паприка", "amount": 10, "unit": "G"},
                {"name": "Чеснок", "amount": 3, "unit": "PC"}
            ]
        },
        {
            "name": "Рыба с овощами в фольге",
            "description": "Запеченная рыба с овощами",
            "instructions": "Выложить рыбу на фольгу. Добавить лук, помидоры, лимон, зелень. Завернуть. Запекать 25 минут при 200°C.",
            "cooking_time": 35,
            "category": "SECOND",
            "tags": ["PP", "OVEN", "EASY"],
            "ingredients": [
                {"name": "Филе белой рыбы", "amount": 600, "unit": "G"},
                {"name": "Помидоры", "amount": 2, "unit": "PC"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Лимон", "amount": 0.5, "unit": "PC"}
            ]
        },
        {
            "name": "Куриное филе в сливочном соусе",
            "description": "Нежная курица в сливочном соусе с грибами",
            "instructions": "Обжарить курицу. Отдельно обжарить грибы с луком. Добавить сливки, мускатный орех. Соединить с курицей.",
            "cooking_time": 30,
            "category": "SECOND",
            "tags": ["QUICK"],
            "ingredients": [
                {"name": "Куриное филе", "amount": 500, "unit": "G"},
                {"name": "Шампиньоны", "amount": 300, "unit": "G"},
                {"name": "Сливки 20%", "amount": 200, "unit": "ML"},
                {"name": "Лук", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Спагетти с морепродуктами",
            "description": "Паста с креветками, мидиями и кальмарами",
            "instructions": "Отварить спагетти. Обжарить морепродукты с чесноком, добавить томаты, белое вино. Смешать с пастой.",
            "cooking_time": 25,
            "category": "SECOND",
            "tags": ["GOURMET", "QUICK"],
            "ingredients": [
                {"name": "Спагетти", "amount": 350, "unit": "G"},
                {"name": "Коктейль из морепродуктов", "amount": 400, "unit": "G"},
                {"name": "Томаты в собственном соку", "amount": 200, "unit": "G"},
                {"name": "Чеснок", "amount": 3, "unit": "PC"}
            ]
        },
        {
            "name": "Бургер домашний",
            "description": "Сочный бургер с говяжьей котлетой",
            "instructions": "Сформировать котлеты из фарша. Обжарить. Собрать бургер: булка, лист салата, котлета, сыр, помидор, лук, соус.",
            "cooking_time": 25,
            "category": "SECOND",
            "tags": ["QUICK", "HEARTY"],
            "ingredients": [
                {"name": "Булочка для бургера", "amount": 4, "unit": "PC"},
                {"name": "Говяжий фарш", "amount": 500, "unit": "G"},
                {"name": "Сыр чеддер", "amount": 4, "unit": "PC"},
                {"name": "Салат", "amount": 50, "unit": "G"},
                {"name": "Помидор", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Картофельный суп-пюре с беконом",
            "description": "Нежный суп с хрустящим беконом",
            "instructions": "Сварить картофель с луком и морковью. Пюрировать. Добавить сливки. Подавать с жареным беконом и зеленью.",
            "cooking_time": 35,
            "category": "FIRST",
            "tags": ["SOUP", "QUICK"],
            "ingredients": [
                {"name": "Картофель", "amount": 600, "unit": "G"},
                {"name": "Бекон", "amount": 150, "unit": "G"},
                {"name": "Сливки", "amount": 100, "unit": "ML"},
                {"name": "Лук", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Томатный суп с базиликом",
            "description": "Итальянский томатный суп",
            "instructions": "Обжарить лук, чеснок. Добавить томаты, бульон, базилик. Варить 20 минут. Пюрировать.",
            "cooking_time": 30,
            "category": "FIRST",
            "tags": ["VEGETARIAN", "SOUP", "QUICK"],
            "ingredients": [
                {"name": "Помидоры", "amount": 800, "unit": "G"},
                {"name": "Лук", "amount": 1, "unit": "PC"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"},
                {"name": "Базилик", "amount": 15, "unit": "G"},
                {"name": "Бульон", "amount": 500, "unit": "ML"}
            ]
        },
        {
            "name": "Соус Песто",
            "description": "Базиликовый соус с орехами и сыром",
            "instructions": "Измельчить базилик, чеснок, кедровые орехи. Добавить пармезан и оливковое масло. Взбить в пасту.",
            "cooking_time": 10,
            "category": "SAUCE",
            "tags": ["VEGETARIAN", "QUICK", "EASY"],
            "ingredients": [
                {"name": "Базилик", "amount": 50, "unit": "G"},
                {"name": "Кедровые орехи", "amount": 30, "unit": "G"},
                {"name": "Пармезан", "amount": 50, "unit": "G"},
                {"name": "Чеснок", "amount": 2, "unit": "PC"},
                {"name": "Масло оливковое", "amount": 80, "unit": "ML"}
            ]
        }
    ],

    # ==================== ПАН-АЗИАТСКАЯ КУХНЯ (PAN) ====================
    "PAN_ASIAN": [
        {
            "name": "Тайский суп Том Ям",
            "description": "Острый кисло-сладкий суп с креветками",
            "instructions": "Вскипятить бульон с лемонграссом, галангалом, листьями каффир. Добавить креветки, грибы. Приправить пастой том ям, рыбным соусом, соком лайма.",
            "cooking_time": 30,
            "category": "FIRST",
            "tags": ["SPICY", "SOUP", "GOURMET"],
            "ingredients": [
                {"name": "Креветки", "amount": 300, "unit": "G"},
                {"name": "Грибы", "amount": 150, "unit": "G"},
                {"name": "Лемонграсс", "amount": 2, "unit": "PC"},
                {"name": "Паста том ям", "amount": 30, "unit": "G"},
                {"name": "Рыбный соус", "amount": 30, "unit": "ML"},
                {"name": "Лайм", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Тайский зеленый карри",
            "description": "Острое карри с кокосовым молоком",
            "instructions": "Обжарить пасту зеленого карри с кокосовым молоком. Добавить курицу, баклажаны, бамбук. Тушить 15 минут. Добавить базилик.",
            "cooking_time": 35,
            "category": "SECOND",
            "tags": ["SPICY"],
            "ingredients": [
                {"name": "Курица", "amount": 400, "unit": "G"},
                {"name": "Кокосовое молоко", "amount": 400, "unit": "ML"},
                {"name": "Паста зеленого карри", "amount": 40, "unit": "G"},
                {"name": "Баклажаны", "amount": 2, "unit": "PC"},
                {"name": "Рыбный соус", "amount": 20, "unit": "ML"}
            ]
        },
        {
            "name": "Пад Тай",
            "description": "Жареная рисовая лапша с креветками",
            "instructions": "Замочить рисовую лапшу. Обжарить креветки, тофу, яйцо. Добавить лапшу, соус из тамаринда, рыбного соуса, сахара. Подавать с арахисом и лаймом.",
            "cooking_time": 25,
            "category": "SECOND",
            "tags": ["QUICK"],
            "ingredients": [
                {"name": "Рисовая лапша", "amount": 200, "unit": "G"},
                {"name": "Креветки", "amount": 200, "unit": "G"},
                {"name": "Тофу", "amount": 100, "unit": "G"},
                {"name": "Яйца", "amount": 1, "unit": "PC"},
                {"name": "Арахис", "amount": 50, "unit": "G"},
                {"name": "Ростки фасоли", "amount": 100, "unit": "G"}
            ]
        },
        {
            "name": "Нем (вьетнамские роллы)",
            "description": "Спринг-роллы с креветками и мятой",
            "instructions": "Размочить рисовую бумагу. Выложить креветки, рисовую лапшу, мяту, салат. Завернуть рулетом. Подавать с арахисовым соусом.",
            "cooking_time": 20,
            "category": "SNACK",
            "tags": ["NO_BAKE", "EASY", "PP"],
            "ingredients": [
                {"name": "Рисовая бумага", "amount": 10, "unit": "PC"},
                {"name": "Креветки", "amount": 200, "unit": "G"},
                {"name": "Рисовая лапша", "amount": 100, "unit": "G"},
                {"name": "Мята", "amount": 20, "unit": "G"},
                {"name": "Салат", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Фо Бо",
            "description": "Вьетнамский суп с говядиной и рисовой лапшой",
            "instructions": "Варить говяжий бульон 3 часа со специями (звездчатый анис, корица). Отварить рисовую лапшу. Подавать с тонко нарезанной говядиной, зеленью, ростками фасоли, лаймом.",
            "cooking_time": 210,
            "category": "FIRST",
            "tags": ["SOUP", "HEARTY"],
            "ingredients": [
                {"name": "Говядина на кости", "amount": 800, "unit": "G"},
                {"name": "Рисовая лапша", "amount": 300, "unit": "G"},
                {"name": "Говяжья вырезка", "amount": 200, "unit": "G"},
                {"name": "Звездчатый анис", "amount": 2, "unit": "PC"},
                {"name": "Корица", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Кхао Сой",
            "description": "Тайский карри-суп с яичной лапшой",
            "instructions": "Обжарить пасту карри с кокосовым молоком. Добавить курицу, бульон. Варить 15 минут. Подавать с отварной и жареной лапшой, луком, лаймом.",
            "cooking_time": 40,
            "category": "FIRST",
            "tags": ["SPICY", "SOUP"],
            "ingredients": [
                {"name": "Курица", "amount": 500, "unit": "G"},
                {"name": "Яичная лапша", "amount": 300, "unit": "G"},
                {"name": "Кокосовое молоко", "amount": 400, "unit": "ML"},
                {"name": "Паста карри", "amount": 40, "unit": "G"},
                {"name": "Лук", "amount": 50, "unit": "G"}
            ]
        },
        {
            "name": "Манаго (филиппинское мясо)",
            "description": "Свинина в кисло-сладком соусе с ананасом",
            "instructions": "Обжарить свинину. Добавить лук, перец, ананас. Залить соусом из уксуса, соевого соуса, сахара. Тушить 30 минут.",
            "cooking_time": 50,
            "category": "SECOND",
            "tags": ["HEARTY"],
            "ingredients": [
                {"name": "Свинина", "amount": 600, "unit": "G"},
                {"name": "Ананас", "amount": 200, "unit": "G"},
                {"name": "Перец болгарский", "amount": 1, "unit": "PC"},
                {"name": "Уксус", "amount": 50, "unit": "ML"},
                {"name": "Соевый соус", "amount": 40, "unit": "ML"}
            ]
        },
        {
            "name": "Соте из баклажанов по-таиландски",
            "description": "Баклажаны с базиликом и чили",
            "instructions": "Обжарить баклажаны. Добавить чеснок, чили, базилик, соевый соус, устричный соус. Жарить 2 минуты.",
            "cooking_time": 15,
            "category": "SECOND",
            "tags": ["VEGETARIAN", "QUICK", "SPICY"],
            "ingredients": [
                {"name": "Баклажаны", "amount": 4, "unit": "PC"},
                {"name": "Базилик", "amount": 30, "unit": "G"},
                {"name": "Чили", "amount": 5, "unit": "G"},
                {"name": "Чеснок", "amount": 3, "unit": "PC"},
                {"name": "Устричный соус", "amount": 20, "unit": "ML"}
            ]
        },
        {
            "name": "Клейкий рис с манго",
            "description": "Тайский десерт из риса и манго",
            "instructions": "Замочить клейкий рис на ночь. Сварить на пару. Смешать с кокосовым молоком и сахаром. Подавать с манго и кунжутом.",
            "cooking_time": 40,
            "category": "DESSERT",
            "tags": ["VEGETARIAN", "EASY"],
            "ingredients": [
                {"name": "Клейкий рис", "amount": 200, "unit": "G"},
                {"name": "Кокосовое молоко", "amount": 200, "unit": "ML"},
                {"name": "Манго", "amount": 2, "unit": "PC"},
                {"name": "Сахар", "amount": 50, "unit": "G"},
                {"name": "Кунжут", "amount": 10, "unit": "G"}
            ]
        }
    ],

    # ==================== ДРУГАЯ КУХНЯ (OTH) ====================
    "OTHER": [
        {
            "name": "Мексиканское гуакамоле",
            "description": "Паста из авокадо с лаймом",
            "instructions": "Размять авокадо. Добавить лук, помидор, кинзу, сок лайма, соль. Перемешать.",
            "cooking_time": 10,
            "category": "SNACK",
            "tags": ["VEGETARIAN", "QUICK", "EASY"],
            "ingredients": [
                {"name": "Авокадо", "amount": 3, "unit": "PC"},
                {"name": "Лайм", "amount": 1, "unit": "PC"},
                {"name": "Помидор", "amount": 1, "unit": "PC"},
                {"name": "Лук красный", "amount": 0.5, "unit": "PC"},
                {"name": "Кинза", "amount": 10, "unit": "G"}
            ]
        },
        {
            "name": "Мексиканские такос",
            "description": "Кукурузные лепешки с начинкой",
            "instructions": "Разогреть тортильи. Приготовить начинку из фарша с томатами и специями. Выложить в тортилью. Добавить сальсу, сыр, авокадо.",
            "cooking_time": 25,
            "category": "SECOND",
            "tags": ["QUICK", "HEARTY"],
            "ingredients": [
                {"name": "Кукурузные лепешки", "amount": 8, "unit": "PC"},
                {"name": "Фарш", "amount": 400, "unit": "G"},
                {"name": "Сальса", "amount": 100, "unit": "G"},
                {"name": "Сыр", "amount": 100, "unit": "G"},
                {"name": "Авокадо", "amount": 1, "unit": "PC"}
            ]
        },
        {
            "name": "Индийское куриное карри",
            "description": "Курица в пряном соусе на йогурте",
            "instructions": "Обжарить лук, имбирь, чеснок. Добавить специи (куркума, кумин, кориандр). Добавить курицу, йогурт, томаты. Тушить 30 минут.",
            "cooking_time": 50,
            "category": "SECOND",
            "tags": ["SPICY"],
            "ingredients": [
                {"name": "Курица", "amount": 600, "unit": "G"},
                {"name": "Йогурт", "amount": 200, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Томаты", "amount": 200, "unit": "G"},
                {"name": "Специи", "amount": 20, "unit": "G"}
            ]
        },
        {
            "name": "Индийский наан с чесноком",
            "description": "Пшеничная лепешка в тандуре",
            "instructions": "Замесить тесто из муки, йогурта, дрожжей. Дать подойти. Раскатать, посыпать чесноком и кинзой. Выпекать при 250°C.",
            "cooking_time": 90,
            "category": "SECOND",
            "tags": ["OVEN", "VEGETARIAN"],
            "ingredients": [
                {"name": "Мука", "amount": 400, "unit": "G"},
                {"name": "Йогурт", "amount": 150, "unit": "G"},
                {"name": "Дрожжи", "amount": 7, "unit": "G"},
                {"name": "Чеснок", "amount": 4, "unit": "PC"},
                {"name": "Кинза", "amount": 15, "unit": "G"}
            ]
        },
        {
            "name": "Марокканский тажин с курицей",
            "description": "Курица с курагой и миндалем",
            "instructions": "Обжарить курицу. Добавить лук, имбирь, шафран. Залить водой. Добавить курагу. Тушить 45 минут. Посыпать миндалем.",
            "cooking_time": 70,
            "category": "SECOND",
            "tags": ["GOURMET", "HEARTY"],
            "ingredients": [
                {"name": "Курица", "amount": 800, "unit": "G"},
                {"name": "Курага", "amount": 150, "unit": "G"},
                {"name": "Миндаль", "amount": 80, "unit": "G"},
                {"name": "Лук", "amount": 2, "unit": "PC"},
                {"name": "Шафран", "amount": 1, "unit": "PINCH"}
            ]
        }
    ]
}
