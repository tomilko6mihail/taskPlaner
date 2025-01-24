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
                    <div style="display: flex; align-items: center;">
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
                    <div style="display: flex;">
                        <a role="button" @click="manipulateTask('editTask')">Сохранить изменения</a>
                        <p style="margin-inline: 10px; color: #764ac9;"><b>/</b></p>
                        <a role="button" @click="$store.commit('deleteTask', $store.state.currentDisplayTask.id), $store.commit('toggleDialog')">Удалить задачу</a>
                    </div>
                </footer>
            </div>
            <div v-if="optionRender === 'addTask'">
                <main>
                    <label>Название:</label>
                    <textarea rows="1" @focus="autoGrow('task_textarea_title')" id="task_textarea_title"
                        @input="autoGrow('task_textarea_title')" maxlength="100" class="input-task-active input-task title"
                        placeholder="Название задачи"></textarea>
                    <label>Описание:</label>
                    <textarea rows="1" @focus="autoGrow('task_textarea_description')" id="task_textarea_description"
                        @input="autoGrow('task_textarea_description')" maxlength="300"
                        class="input-task-active input-task description" placeholder="Описание задачи"></textarea>
                    <label>Ответственный:</label>
                    <textarea rows="1" @focus="autoGrow('task_textarea_responsible')" id="task_textarea_responsible"
                        @input="autoGrow('task_textarea_responsible')" maxlength="50"
                        class="input-task-active input-task responsible" placeholder="Ответственный за выполнение"></textarea>
                    <label>Текущий статус:</label>
                    <div style="display: flex; align-items: center; width: fit-content; height: auto; background: rgb(235, 230, 244); border-radius: 4px; padding: 8px;">
                        <img src="../../assets/img/menu.svg" height="13px" style="margin-right: 7px;" alt="">
                        <select id="task_select" name="selectStatus">
                            <option :selected="$store.state.currentDisplayTask.statusId === 0 ? true : false" selected value="0">Бэклог</option>
                            <option :selected="$store.state.currentDisplayTask.statusId === 1 ? true : false" value="1">В процессе</option>
                            <option :selected="$store.state.currentDisplayTask.statusId === 2 ? true : false" value="2">Выполнено</option>
                        </select>
                    </div>
                </main>
                <footer style="margin-top: 25px; cursor: pointer;">
                    <a role="button" @click="manipulateTask('addTask')">Добавить задачу</a>
                </footer>
            </div>
        </div>
    </section>
</template>

<script>
import store from '@/store';

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
    methods: {
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
        }
    },
    mounted() {
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
</script>

<style scoped>
@font-face {
    font-family: gothamlight;
    src: url(../../assets/fonts/gotham_light.otf);
}

@font-face {
    font-family: gothambold;
    src: url(../../assets/fonts/gotham_bold.otf);
}

@font-face {
    font-family: gothambook;
    src: url(../../assets/fonts/gotham_book.otf);
}

@font-face {
    font-family: gothammedium;
    src: url(../../assets/fonts/gotham_medium.otf);
}

.footer-task {
    background: #E9DFFC;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    width: 100%;
    margin-top: 15px;
    border-radius: 10px;
}

a {
    font-family: gothambook;
    font-size: 15px;
    color: #764ac9;
    text-decoration: underline 1px solid #764ac900;
    text-underline-offset: 15px;
    transition: all 0.15s ease-in-out;
}

a:hover {
    text-decoration: underline 1px solid #764ac9;
    text-underline-offset: 3px;
    transition: all 0.15s ease-in-out;
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
    padding: 50px;
}

.modal-window {
    min-height: 30vh;
    min-width: 30vw;
    max-width: 50vw;
    background: white;
    border-radius: 8px;
    box-shadow: 0 0 20px -5px rgba(255, 255, 255, 0.7);
    padding: 25px;
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