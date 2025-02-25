<template>
    <div class="margin-passive" :id="'div' + id" style="position: relative;"
        :style="isValidate ? 'margin-bottom: 10px' : 'padding-bottom: 16px; margin-bottom: 15px'">
        <label :id="'label' + id" :for="id">{{ pler }}{{ required ? ' *' : '' }}</label>
        <input maxlength="50" :class="isValidate ? 'hide-shadow' : 'show-shadow'" :id="'input' + id" @blur="setClassBottom"
            @focus="setClassTop" @input="updateInput" :type="type.split(' ')[0]">
        <div class="border-bottom" :class="isValidate ? 'hide-alert-border' : 'show-alert-border'"></div>
        <p :id="'alert' + id" :class="isValidate ? 'hide-alert' : 'show-alert'" v-if="required">{{ message }}</p>
    </div>
</template>
<script>
export default {
    name: 'MyInput',
    props: {
        pler: { //плейсхолдер
            type: String,
            required: true
        },
        type: {
            type: String,
            required: true
        },
        id: {
            type: Number,
            required: true
        },
        active: { //
            type: Boolean,
            default: true
        },
        required: { // нужна ли проверка инпуту
            type: Boolean,
            default: false
        },
        updValidate: { //обновление валидации
            type: Number,
            default: 0
        },
        comparedValue: { //обновление валидации
            type: String,
            default: ''
        },
        cleanValue:{
            type: Boolean,
            default: false
        }

    },
    data() {
        return {
            value: '',
            message: '',
            isValidate: true, // по дефолту ошибки у поля нет
        }
    },
    methods: {
        updateInput(event) {
            this.value = document.getElementById('input' + this.id).value
            this.$emit('update:inputValue', { value: event.target.value, isValidate: this.isValidate }) // отправляем объект в родитель, первое свойство - само значение, второе - нет ли ошибки в поле
        },
        setClassTop() {
            this.isValidate = true // сбрасываем состояние того, что произошла ошибка: клик по полю -> ошибка пропадает (чтобы не мозолило глаз)
            let label = document.getElementById('label' + this.id)
            if (this.value == '') {
                document.getElementById('div' + this.id).className = 'margin-active'
                label.className = "show-top"
            }
        },
        setClassBottom() {
            let label = document.getElementById('label' + this.id)
            if (this.value == '') {
                document.getElementById('div' + this.id).className = 'margin-passive'
                label.className = "show-bottom"
            }
        },
        validation() {
            if (this.required) { // если это вообще нуждается в валидации
                if (this.type === 'text') { // для чего делаем проверку
                    this.message = 'Обязательно к заполнению' // текст ошибки
                    if (this.value === '') this.isValidate = false // условие (если по условию не проходит, то в родитель отправляется {значение и false}, что препятствует отправки формы (по условию будет еще раз вызвана функция отображающая ошибки))
                    else this.isValidate = true // если все хорошо, то отправляем в родитель статус успешного заполнения поля
                }
                if (this.type === 'email') { // если это почта
                    if (this.value === '') { //если поле пустое
                        this.message = 'Обязательно к заполнению' // выводим ошибку
                        this.isValidate = false // отправляем в родитель отрицательный результат проверки
                    }
                    else { // если поле не пустое
                        this.message = 'Некорректный формат' // заранее объявляем название ошибки
                        let reg = /^\w+@\w+\.[a-z]{2,}$/i // создаем условие проверки почта ли это
                        if (!reg.test(this.value)) this.isValidate = false // если это не почта передаем в родитель отрицательный результат проверки
                        else this.isValidate = true // если почта то все хорошо
                    }
                }
                if (this.type === 'password') {
                    if (this.value === '') {
                        this.message = 'Обязательно к заполнению'
                        this.isValidate = false
                    }
                    else {
                        this.message = 'Некорректный формат'
                        let reg = /\w/i
                        if (!(reg.test(this.value)) || this.value.length < 5) this.isValidate = false
                        else this.isValidate = true
                    }
                }
                if (this.type == 'password return') {
                    if (this.value === '') {
                        this.message = 'Обязательно к заполнению'
                        this.isValidate = false
                    }
                    else {
                        this.message = 'Пароли не совпадают'
                        if (this.value != this.comparedValue.value) this.isValidate = false
                        else this.isValidate = true
                    }
                }
            }
        }
    },
    watch: {
        updValidate() { // вызывется при отправке формы
            this.validation()
        },
        cleanValue(){
            console.log("sdfmдьдж");
            //this.setClassTop()
            this.value = '';
            document.getElementById('input' + this.id).value = '' 
            this.setClassBottom()
        }
    }
}
</script>

<style scoped>
label {
    font-family: gothammedium;
    font-size: 16px;
    position: absolute;
    color: #9986a3;
    margin-bottom: 4px;
    top: 10px;
    left: 10px;
    z-index: 3;
    transition: all 0.2s ease-in-out;
    pointer-events: none;
}

p {
    position: absolute;
    z-index: 1;
    font-family: gothammedium;
    font-size: 11px;
    color: #ef4c4c;
}

.hide-alert {
    top: 0;
    transition: 0.2s ease-in-out;
}

.show-alert {
    top: 80%;
    transition: 0.2s ease-in-out;
}

.border-bottom {
    position: absolute;
    z-index: 1;
    height: 20%;
    top: 53%;
    border-radius: 4px;
    background: #ef4c4c;
    transition: all 0.7s cubic-bezier(.32, .66, .45, .99);
}

.hide-alert-border {
    width: 0%;
    transition: all 0.7s cubic-bezier(.32, .66, .45, .99);
}

.show-alert-border {
    width: 100%;
    transition: all 0.7s cubic-bezier(.32, .66, .45, .99);
}

.margin-active {
    margin: 31px 0 10px 0;
    transition: all 0.2s ease-in-out;
}

.margin-passive {
    margin: 10px 0 10px 0;
    transition: all 0.2s ease-in-out;
}

.margin-active-alert {
    margin: 31px 0 20px 0;
    transition: all 0.2s ease-in-out;
}

.margin-passive-alert {
    margin: 10px 0 20px 0;
    transition: all 0.2s ease-in-out;
}

.show-top {
    top: -20px;
    font-size: 13px;
    color: rgb(129 110 135);
    left: 0px;
    transition: all 0.2s ease-in-out;
}

.show-bottom {
    color: #9986a3;
    top: 10px;
    left: 10px;
    transition: all 0.2s ease-in-out;
}

input {
    outline: none;
    border-radius: 4px;
    font-family: gothammedium;
    font-size: 16px;
    width: 100%;
    height: auto;
    padding: 10px;
    background: rgb(235, 230, 244);
    border: none;
    position: relative;
    z-index: 2;
    top: 0;
    box-shadow: 0 0 0 0 rgb(177, 173, 185);
    transition: all 0.2s ease-in-out;
}

input:focus {
    top: -2px;
    box-shadow: 0 2px 0 0 rgb(177, 173, 185);
    transition: all 0.2s ease-in-out;
}
</style>