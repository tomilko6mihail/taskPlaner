<template>
    <section :id="statusId">
        <div v-show="($store.state.tasks.filter(x => x.statusId === statusId).length === 0) || (thisSector === 1)">
            <h3 style="margin-bottom: 4px;">Здесь ничего нет.</h3>
            <p>Перетащите задачу в эту область, или создайте новую.</p>
        </div>
        <TaskCard v-for="task in $store.state.tasks.filter(x => x.statusId === statusId)" :key="task.id" :task="task">
        </TaskCard>
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
        const thisSector = document.getElementById(this.statusId).childElementCount
        console.log(thisSector)
    }
}
</script>

<style scoped>
@font-face {
    font-family: gothambold;
    src: url(../assets/fonts/gotham_bold.otf);
}

@font-face {
    font-family: gothamlight;
    src: url(../assets/fonts/gotham_light.otf);
}

h3 {
    font-family: gothambold;
    font-size: 16px;
}

p {
    font-family: gothamlight;
    font-size: 14px;
}

div {
    width: 100%;
    height: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    background: none;
    border-radius: 15px;
    border: 2px dashed #000000;
    flex-direction: column;
    text-align: center;
    padding: 15px;
    stroke-dasharray: 5px;
}

section {
    width: 100%;
    padding-inline: 30px;
    height: fit-content;
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>