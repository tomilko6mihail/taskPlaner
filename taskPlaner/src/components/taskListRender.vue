<template>
    <section>
        <TaskCard v-for="task in $store.state.tasks.filter(x => x.statusId === statusId)" :key="task.id" :task="task"></TaskCard>
    </section>
</template>

<script>
import TaskCard from './taskCard.vue';

export default {
    components: {
        TaskCard
    },
    props: {
        statusId: {
            type: Number,
            required: true
        },
    },
    mounted(){
    }
}
</script>

<style scoped>
section {
    width: 100%;
    padding-inline: 30px;
    height: fit-content;
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>