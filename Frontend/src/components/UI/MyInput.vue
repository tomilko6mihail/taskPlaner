<template>
    <div class="margin-passive" :id="'div'+id" style="position: relative;" :style="isValidate ? 'margin-bottom: 10px' : 'margin-bottom: 35px'">
        <label :id="'label' + id" :for="id">{{ pler }}{{ required ? ' *' : ''}}</label>
        <input :id="'input' + id" @blur="setClassBottom" @focus="setClassTop" @input="updateInput" :type="type">
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
            active: {
                type: Boolean,
                default: true
            },
            required: {
                type: Boolean,
                default: false
            },
            updValidate: {
                type: Number,
                default: 0
            }

        },
        data(){
            return{
                value: '',
                message: '',
                isValidate: true
            }
        },
        methods: {
            updateInput(event){
                this.value = document.getElementById('input'+this.id).value
                this.$emit('update:inputValue', {value: event.target.value, isValidate: this.isValidate})
            },
            setClassTop(){
                this.isValidate = true
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
            },
            validation(){
                if(this.required){
                    if(this.type === 'text'){
                        this.message = 'Обязательно к заполнению'
                        if(this.value === '') this.isValidate = false
                        else this.isValidate = true
                    }
                }
            }
        },
        watch: {
            updValidate(){
                this.validation()
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
p{
    position: absolute;
    font-family: gothammedium;
    font-size: 11px;
    color: #ef4c4c;
}
.hide-alert{
    top: 0;
    transition: 0.2s ease-in-out;
}
.show-alert{
    top: 100%;
    transition: 0.2s ease-in-out;
}
.margin-active{
    margin: 31px 0 10px 0;
    transition: all 0.2s ease-in-out;
}
.margin-passive{
    margin: 10px 0 10px 0;
    transition: all 0.2s ease-in-out;
}
.margin-active-alert{
    margin: 31px 0 20px 0;
    transition: all 0.2s ease-in-out;
}
.margin-passive-alert{
    margin: 10px 0 20px 0;
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