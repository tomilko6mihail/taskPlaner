<template>
    <section @click="hideDialog" class="modal-bg">
        <div @click.stop class="modal-window">
            <div v-if="optionRender === 'viewTask'">
                <main>
                    <label>Название:</label>
                    <textarea @focus="autoGrow('task_textarea_title')" id="task_textarea_title"
                        @input="autoGrow('task_textarea_title')" maxlength="100" class="input-task title"
                        :placeholder="$store.state.currentDisplayTask.title">{{ $store.state.currentDisplayTask.title }}</textarea>
                    <label>Описание:</label>
                    <textarea @focus="autoGrow('task_textarea_description')" id="task_textarea_description"
                        @input="autoGrow('task_textarea_description')" maxlength="300" class="input-task description"
                        :placeholder="$store.state.currentDisplayTask.description">{{
                            $store.state.currentDisplayTask.description === "" ? 'Отсутствует' :
                                $store.state.currentDisplayTask.description }}</textarea>
                    <label>Ответственный:</label>
                    <textarea @focus="autoGrow('task_textarea_responsible')" id="task_textarea_responsible"
                        @input="autoGrow('task_textarea_responsible')" maxlength="50" class="input-task responsible"
                        :placeholder="$store.state.currentDisplayTask.responsible">{{
                            $store.state.currentDisplayTask.responsible === "" ? 'Отсутствует' :
                                $store.state.currentDisplayTask.responsible }}</textarea>
                </main>
                <footer class="footer-task">
                    <div class="select-div" style="display: flex; align-items: center;">
                        <img src="../../assets/img/menu.svg" height="13px" style="margin-right: 7px;" alt="">
                        <select id="task_select" name="selectStatus">
                            <option :selected="$store.state.currentDisplayTask.statusId === 0 ? true : false" value="0">
                                Бэклог</option>
                            <option :selected="$store.state.currentDisplayTask.statusId === 1 ? true : false" value="1">
                                В процессе</option>
                            <option :selected="$store.state.currentDisplayTask.statusId === 2 ? true : false" value="2">
                                Выполнено</option>
                        </select>
                    </div>
                    <div
                        :style="screen > 428 ? 'display: flex; flex-wrap: wrap;' : 'display: flex; flex-wrap: wrap; flex-direction: column'">
                        <MyLink :style="screen > 428 ? '' : 'margin-bottom: 5px'" @click="manipulateTask('editTask')"
                            :gotham="'book'" :color="'purple'">Сохранить изменения</MyLink>
                        <p v-if="screen > 428" style="margin-inline: 10px; color: #764ac9;"><b>/</b></p>
                        <MyLink
                            @click="$store.commit('deleteTask', $store.state.currentDisplayTask.id), $store.commit('toggleDialog')"
                            :gotham="'book'" :color="'purple'">Удалить задачу</MyLink>
                    </div>
                </footer>
            </div>
            <div v-if="optionRender === 'addTask'">
                <main>
                    <label>Название:</label>
                    <textarea rows="1" @focus="autoGrow('task_textarea_title')" id="task_textarea_title"
                        @input="autoGrow('task_textarea_title')" maxlength="100"
                        class="input-task-active input-task title" placeholder="Название задачи"></textarea>
                    <label>Описание:</label>
                    <textarea rows="1" @focus="autoGrow('task_textarea_description')" id="task_textarea_description"
                        @input="autoGrow('task_textarea_description')" maxlength="300"
                        class="input-task-active input-task description" placeholder="Описание задачи"></textarea>
                    <label>Ответственный:</label>
                    <textarea rows="1" @focus="autoGrow('task_textarea_responsible')" id="task_textarea_responsible"
                        @input="autoGrow('task_textarea_responsible')" maxlength="50"
                        class="input-task-active input-task responsible"
                        placeholder="Ответственный за выполнение"></textarea>
                    <label>Текущий статус:</label>
                    <div
                        style="display: flex; align-items: center; width: fit-content; height: auto; background: rgb(235, 230, 244); border-radius: 4px; padding: 8px;">
                        <img src="../../assets/img/menu.svg" height="13px" style="margin-right: 7px;" alt="">
                        <select id="task_select" name="selectStatus">
                            <option :selected="$store.state.currentDisplayTask.statusId === 0 ? true : false" selected
                                value="0">Бэклог</option>
                            <option :selected="$store.state.currentDisplayTask.statusId === 1 ? true : false" value="1">
                                В процессе</option>
                            <option :selected="$store.state.currentDisplayTask.statusId === 2 ? true : false" value="2">
                                Выполнено</option>
                        </select>
                    </div>
                </main>
                <footer style="margin-top: 25px; cursor: pointer;">
                    <MyLink @click="manipulateTask('addTask')" :gotham="'book'" :color="'purple'">Сохранить изменения
                    </MyLink>
                </footer>
            </div>
            <div v-if="optionRender === 'auth'">
                <header style="position: relative; height: 20px; margin-bottom: 10px;">
                    <h2 style="position: absolute; transform-origin: top;"
                        :class="showLogin ? 'show-login' : 'hide-login'">Вход в аккаунт</h2>
                    <h2 style="position: absolute; transform-origin: bottom;"
                        :class="showLogin ? 'hide-reg' : 'show-reg'">Регистрация</h2>
                </header>
                <main>
                    <form novalidate class="form-login" @submit="validationBeforeLoginUser" @submit.prevent="" action="" :method="showLogin ? 'get' : 'post'">
                        <div>
                            <MyInput :updValidate="updValidate" :required="true" v-model:inputValue="email" :type="'email'" :pler="'Почта'" :id="1"></MyInput>
                            <MyInput :updValidate="updValidate" :required="true" v-model:inputValue="password" :type="'password'" :pler="'Пароль'" :id="2">
                            </MyInput>
                            <div style="transform-origin: top;" :class="showLogin ? 'hide-inputs' : 'show-inputs'">
                            <MyInput :updValidate="updValidate" :required="!showLogin" :style="showLogin ? 'margin: 0' : ''" v-model:inputValue="returnPassword" :type="'password'" :pler="'Повторите пароль'":id="3">
                            </MyInput>
                            <MyInput :updValidate="updValidate" :required="!showLogin" v-model:inputValue="name" :type="'text'" :pler="'Имя'" :id="4">
                            </MyInput>
                            <MyInput v-model:inputValue="lastname" :type="'text'" :pler="'Фамилия'" :id="5">
                            </MyInput>
                            </div>

                        </div>
                        <input class="form-submit" type="submit" :value="showLogin ? 'Войти в аккаунт' : 'Зарегистрироваться'">
                    </form>
                </main>
                <footer>
                    <div style="display: flex; align-items: center; margin-top: 15px; width: 100%;">
                        <div style="width: 50%; display: flex; justify-content: center; position: relative; z-index: 2; background-color: white;"
                            :class="showLogin ? 'left-block-footer-auth-show' : 'left-block-footer-auth-hide'">
                            <MyLink :class="showLogin ? 'slide-right-lt' : 'slide-left-lt'"
                                @click="showLogin = !showLogin" style="font-size: 14px; position: relative;"
                                :gotham="'book'" :color="'purple'"> {{ showLogin ? 'Нет аккаунта?' : 'Есть аккаунт?' }}
                            </MyLink>
                        </div>
                        <div style="width: 50%; display: flex; justify-content: center; position: relative;">
                            <MyLink :class="showLogin ? 'slide-right-rt' : 'slide-left-rt'"
                                style="font-size: 14px; position: relative; z-index: 1;" :gotham="'book'"
                                :color="'purple'">Забыли пароль?</MyLink>
                        </div>
                    </div>
                </footer>
            </div>
        </div>
    </section>
</template>

<script>
import store from '@/store';
import { mapActions } from 'vuex';
import MyLink from './MyLink.vue';

export default {
    name: "ModalWindow",
    props: {
        show: {
            type: Boolean,
            default: false
        },
        optionRender: {
            type: String,
            default: "none"
        }
    },
    data() {
        return {
            screen: window.innerWidth,
            showLogin: true,
            email: {value: '', isValidate: false},
            password:  {value: '', isValidate: false},
            returnPassword:  {value: '', isValidate: false},
            name:  {value: '', isValidate: false},
            lastname:  {value: '', isValidate: true},
            updValidate: 0
        }
    },
    methods: {
        ...mapActions({
            loginUser: 'loginUser'
        }),
        hideDialog() {
            store.commit('toggleDialog')
        },
        autoGrow(id) {
            let el = document.getElementById(id)
            el.style.height = '5px';
            el.style.height = el.scrollHeight + 'px';
        },
        manipulateTask(manipulate) {
            const title = document.getElementById('task_textarea_title').value
            const description = document.getElementById('task_textarea_description').value
            const responsible = document.getElementById('task_textarea_responsible').value
            const statusId = parseInt(document.getElementById('task_select').value)
            let id = 0
            if (manipulate === 'editTask') { id = store.state.currentDisplayTask.id }
            if (manipulate === 'addTask') { id = Date.now() }
            const newTask = { id: id, statusId: statusId, title: title, responsible: responsible, description: description }
            store.commit(manipulate, newTask)
            store.commit('toggleDialog')
        },
        validationBeforeLoginUser(){
            if(this.email.isValidate && this.password.isValidate && this.returnPassword.isValidate && this.name.isValidate){
                this.loginUser()
            }else{
                this.updValidate += 1
            }
        }
    },
    mounted() {
        if (this.optionRender === 'viewTask' || this.optionRender === 'addTask') {
            let el = document.getElementById(`task_textarea_title`)
            el.style.height = '5px';
            el.style.height = el.scrollHeight + 'px';
            let el2 = document.getElementById(`task_textarea_description`)
            el2.style.height = '5px';
            el2.style.height = el2.scrollHeight + 'px';
            let el3 = document.getElementById(`task_textarea_responsible`)
            el3.style.height = '5px';
            el3.style.height = el3.scrollHeight + 'px';
        }
    }
}
</script>

<style scoped>
h2 {
    font-family: gothambold;
    margin-bottom: 10px;
}

.show-inputs{
    transform: rotateX(0deg);
    max-height: 200px;
    transition: all 0.4s ease-in
}
.hide-inputs{
    transform: rotateX(90deg);
    max-height: 0;
    transition: all 0.4s ease-out
}

.show-login {
    transform: rotateX(0deg);
    transition: all 0.4s ease-in
}
.hide-login {
    transform: rotateX(90deg);
    transition: all 0.4s ease-out
}

.show-reg {
    transform: rotateX(0deg);
    transition: all 0.4s ease-in
}

.hide-reg {
    transform: rotateX(90deg);
    transition: all 0.4s ease-out
}

.left-block-footer-auth-show {
    border-right: 1px solid #906fcd;
    transition: all 1s cubic-bezier(1, 0, 0, 0.06)
}

.left-block-footer-auth-hide {
    border-right: 1px solid #58369700;
    transition: all 0.1s ease-in-out;
}

.slide-left-rt {
    left: -100%;
    color: #58369700;
    transition: all 0.4s ease-in-out;
}

.slide-right-rt {
    left: 0%;
    transition: all 0.4s ease-in-out;
}

.slide-left-lt {
    left: 50%;
    transition: left .4s ease-in-out!important;
}

.slide-right-lt {
    left: 0%;
    transition: left .4s ease-in-out!important;
}

.footer-task {
    background: #E9DFFC;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    width: 100%;
    margin-top: 15px;
    border-radius: 10px;
}

.form-login {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.form-submit {
    width: 100%;
    font-family: gothambold;
    color: white;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #764ac9;
    border-radius: 150px;
    outline: none;
    border: none;
    padding: 10px;
    margin-top: 20px;
    position: relative;
    top: -3px;
    box-shadow: 0 3px 0 0 #583697;
    transition: all 0.2s ease-in-out;
}

.form-submit:hover {
    background: #9061e7;
    transition: all 0.2s ease-in-out;
}

.form-submit:active {
    top: 0;
    box-shadow: 0 0px 0 0 #583697;
    transition: all 0.1s ease-in-out;
}

@media (max-width: 536px) {
    .select-div {
        margin-bottom: 10px;
    }
}

@media (max-width: 964px) and (min-width: 716px) {
    .select-div {
        margin-bottom: 10px;
    }
}

select {
    cursor: pointer;
    border: none;
    background: none;
    appearance: none;
    outline: none;
    color: #764ac9;
}

select:focus {
    outline: none;
    border: none;
}

.modal-bg {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 5;
    padding: 5%;
    animation-name: blured;
    animation-duration: .2s;
    animation-iteration-count: 1;
}

@keyframes blured {
    from {
        backdrop-filter: blur(0px);
        background: rgba(0, 0, 0, 0);
    }

    to {
        backdrop-filter: blur(5px);
        background: rgba(0, 0, 0, 0.5);
    }
}

@media (max-width: 715px) {
    .modal-window {
        max-width: 100% !important;
        width: 100% !important;
    }
}

.modal-window {
    min-height: 30vh;
    min-width: 30vw;
    max-width: 50vw;
    background: white;
    border-radius: 8px;
    box-shadow: 0 0 20px -5px rgba(255, 255, 255, 0.7);
    padding: 25px;
    position: relative;
    top: 0;
    opacity: 1;
    animation-name: blop;
    animation-duration: .2s;
    animation-iteration-count: 1;
    transition: all 0.2s ease-in-out;
}

@keyframes blop {
    from {
        top: 25px;
        opacity: 0;
    }

    to {
        top: 0;
        opacity: 1;
    }
}

label {
    font-family: gothamlight;
    font-size: 13px;
}

.input-task {
    margin-bottom: 10px;
    background: rgb(255, 255, 255);
    border-radius: 4px;
    width: 100%;
    border: none;
    resize: none;
    padding: 0;
    padding: 8px;
    outline: none;
    position: relative;
    left: -8px;
    cursor: pointer;
}

.input-task:focus,
.input-task-active {
    background: rgb(235, 230, 244);
    left: 0;
    cursor: text;
}

.title {
    font-family: gothambold;
    font-size: 19px;
}

.description {
    font-family: gothambook;
    font-size: 17px;
}

.responsible {
    font-family: gothambook;
    font-size: 17px;
}
</style>