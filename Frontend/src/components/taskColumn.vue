<template>
    <div class="section_task">
        <header>
            <div :style="toggleShowContent || isDesktop ? 'border-bottom: 1px solid black;' : 'border-bottom: none'" class="inner-header">
                <div style="display: flex; align-items: center;">
                    <img v-if="nameColumn === 'Бэклог'" src="../assets/img/task-square.svg" width="20" alt="icon">
                    <img v-if="nameColumn === 'В процессе'" src="../assets/img/clock.svg" width="20" alt="icon">
                    <img v-if="nameColumn === 'Выполнено'" src="../assets/img/tick-circle.svg" width="20" alt="icon">
                    <div @click="toggleShowContent = !toggleShowContent" style="display: flex; align-items: center;">
                        <h3>{{ nameColumn }}</h3>
                        <img v-if="!isDesktop" style="margin-left: 5px;" :class="toggleShowContent ? 'arrow-down' : 'arrow-up'" src="../assets/img/arrow-down.svg" alt="arrow">
                    </div>
                </div>
                <a role="button" style="cursor: pointer;" @click="$store.commit('setOptionRenderModal', 'addTask'), $store.commit('toggleDialog'), $store.commit('setCurrentDisplayTask', {statusId: statusId})">+ задача</a>
            </div>

        </header>
        <main v-if="toggleShowContent || isDesktop" style="height: 100%; overflow-y: auto; overflow-x: hidden;">
            <TaskListRender :selectedSort="selectedSort" :tasks="tasks" :statusId="statusId"></TaskListRender>
        </main>
    </div>
</template>

<script>
import TaskListRender from './taskListRender.vue';

export default {
    components: {
        TaskListRender
    },
    //:src="urlImage"
    props: {
        nameColumn: {
            type: String,
            required: true
        },
        statusId: {
            type: Number,
            required: true
        },
        tasks: {
            type: Array,
            default: () => []
        },
        selectedSort: {
            type: String,
            default: "title"
        }
    },
    data(){
        return{
            toggleShowContent: true
        }
    },
    computed: {
        isDesktop(){
            if(window.innerWidth > 976) return true
            else return false
        }
    }
}
</script>

<style scoped>
@font-face {
    font-family: gothambold;
    src: url('../assets/fonts/gotham_bold.otf');
}
@font-face {
    font-family: gothammed;
    src: url('../assets/fonts/gotham_medium.otf');
}

.section_task {
    background-color: #F1F1F1;
    width: 100%;
    border-radius: 15px;
    height: 100%;
    display: flex;
    flex-direction: column;
}
@media (max-width: 975px){
    .section_task{
        margin-bottom: 30px
    }

}
.arrow-down{
    transform: rotateZ(0deg);
    transition: all 0.15s ease-in-out;
}
.arrow-up{
    transform: rotateZ(180deg);
    transition: all 0.15s ease-in-out;
}
header{
    padding: 0 30px;
    width: 100%;
    height: auto;
}
header h3{
    font-family: gothambold;
    margin-left: 5px;
}
header a{
    color: black;
    font-family: gothammed;
    text-decoration: underline solid #764ac900;
    text-underline-offset: 15px;
    transition: all 0.15s ease-in-out;
}
header a:hover{
    color: #764ac9;
    text-decoration: underline solid #764ac9;
    text-underline-offset: 3px;
    transition: all 0.15s ease-in-out;
}
header .inner-header {
    border-bottom: 1px solid black;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 17px 0;
}
</style>