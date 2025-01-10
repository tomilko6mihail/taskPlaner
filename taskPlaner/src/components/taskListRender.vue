<template>
    <section>
        <TaskCard v-for="task in tasks" :key="task.id" :task="task"></TaskCard>
    </section>
</template>

<script>
import TaskCard from './taskCard.vue';

    export default {
        components: {
            TaskCard
        },
        props:{
            typeList: {
                type: String,
                required: true
            },
            tasks:{
                type: Array,
                required: true
            }
        }
    }
</script>

<style scoped>
section{
    width: 100%;
    padding-inline: 30px;
    height: fit-content;
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>