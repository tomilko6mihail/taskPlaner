<template>
    <div class="margin-passive" :id="'div'+id" style="position: relative;">
        <label :id="'label' + id" :for="id">{{ pler }}</label>
        <input :id="'input' + id" @blur="setClassBottom" @focus="setClassTop" @input="updateInput" :type="type">
    </div>
</template>

<script>
    export default {
        name: 'MyInput',
        props: {
            pler: {
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
            active: {
                type: Boolean,
                default: true
            }
        },
        data(){
            return{
                value: ''
            }
        },
        methods: {
            updateInput(event){
                this.value = document.getElementById('input'+this.id).value
                this.$emit('update:inputValue', event.target.value)
            },
            setClassTop(){
                let label = document.getElementById('label'+this.id)
                if(this.value == ''){
                    document.getElementById('div'+this.id).className = 'margin-active'
                    label.className = "show-top"
                }
            },
            setClassBottom(){
                let label = document.getElementById('label'+this.id)
                if(this.value == ''){
                    document.getElementById('div'+this.id).className = 'margin-passive'
                    label.className = "show-bottom"
                }
            }
        }
    }
</script>

<style scoped>
label{
    font-family: gothammedium;
    font-size: 16px;
    position: absolute;
    color: #9986a3;
    margin-bottom: 4px;
    top: 10px;
    left: 10px;
    z-index: 2;
    transition: all 0.2s ease-in-out;
    pointer-events: none;
}
.margin-active{
    margin: 31px 0 10px 0;
    transition: all 0.2s ease-in-out;
}
.margin-passive{
    margin: 10px 0 10px 0;
    transition: all 0.2s ease-in-out;
}
.show-top{
    top: -20px;
    font-size: 13px;
    color: rgb(129 110 135);
    left: 0px;
    transition: all 0.2s ease-in-out;
}
.show-bottom{
    color: #9986a3;
    top: 10px;
    left: 10px;
    transition: all 0.2s ease-in-out;
}
input{
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
    top: 0;
    box-shadow: 0 0 0 0 rgb(177, 173, 185);
    transition: all 0.2s ease-in-out;
}
input:focus{
    top: -2px;
    box-shadow: 0 2px 0 0 rgb(177, 173, 185);
    transition: all 0.2s ease-in-out;
}
</style>