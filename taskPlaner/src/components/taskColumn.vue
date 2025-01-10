<template>
    <div class="section_task">
        <header>
            <div class="inner-header">
                <div style="display: flex; align-items: center;">
                    <img :src="urlImage" width="20" alt="icon">
                    <h3>{{ nameColumn }}</h3>
                </div>
                <a href="">+ задача</a>
            </div>

        </header>
        <main style="height: 100%; padding-block: 20px; overflow-y: auto; overflow-x: hidden;">
            <TaskListRender :tasks="tasks"></TaskListRender>
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
        urlImage: {
            type: String,
            required: true
        },
        tasks: {
            type: Array,
            default: () => []
        }
    },
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
    display: grid;

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
}
header .inner-header {
    border-bottom: 1px solid black;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 13px 0;
}
</style>