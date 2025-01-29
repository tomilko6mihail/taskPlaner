<template>
    <section :id="statusId">
        <div v-show="this.length_of_element_in_column === 1">
            <h3 style="margin-bottom: 4px;">Здесь ничего нет.</h3>
            <p>Перетащите задачу в эту область, или создайте новую.</p>
        </div>
        <transition-group name="listTask">
            <TaskCard class="listTask-item" v-for="task in sortedPosts" :key="task.id" :task="task">
            </TaskCard>
        </transition-group>
    </section>
</template>

<script>
import store from '@/store';
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
        tasks: {
            type: Array,
            required: true
        },
        selectedSort: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            length_of_element_in_column: 2,
            thisTasks: this.tasks.filter(x => x.statusId === this.statusId),
            screen: window.innerWidth
        }
    },
    mounted() {
        const observer = new MutationObserver(mutations => {
            mutations.forEach(mutation => {
                if (mutation.addedNodes.length) this.length_of_element_in_column = document.getElementById(this.statusId).childElementCount//, console.log(document.getElementById(this.statusId).childElementCount, this.statusId, "зашел");
                else if (mutation.removedNodes.length) this.length_of_element_in_column = document.getElementById(this.statusId).childElementCount//, console.log(document.getElementById(this.statusId).childElementCount, this.statusId, "вышел");
            });
        });
        const config = { childList: true };
        observer.observe(document.getElementById(this.statusId), config);
        //.filter(x => x.statusId === this.statusId)
    },
    computed:{
        sortedPosts(){      
            //console.log(this.taskThis);
            this.thisTasks = this.tasks.filter(x => x.statusId === this.statusId)
            return [...this.thisTasks].sort((post1, post2) => {
                return post1[this.selectedSort]?.localeCompare(post2[this.selectedSort]) //сравниваем x двух постов
            })
        }
    }
}
</script>

<style scoped>

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
    margin-bottom: 30px;
}

section {
    width: 100%;
    padding-inline: 30px;
    padding-block: 20px;
    height: fit-content;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
}



.listTask-item {
  transition: all 0.5s ease;
  display: inline-block;
}

.listTask-enter-from,
.listTask-leave-to {
  opacity: 0;
  transform: translateY(30px);
}

.listTask-leave-active {
    position: absolute;
}
</style>