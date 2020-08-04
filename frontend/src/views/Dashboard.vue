<template lang="pug">
    p asdsa
</template>

<script>
import axios from 'axios'
export default {
    name: 'Dashboard',
    data() {
        return {
            base_url: `http://localhost:8000/`,
        }
    },
    created() {
        this.checklogin();
    },
    methods: {
        checklogin() {
            axios.post(this.base_url + `api/checklogin/`, {"token": localStorage.getItem('Authorization')})
            .then((res) => {
                if(res.data == 'logged') {
                    this.$router.push({ name: 'Dashboard' });
                }
            })
            .catch(() => {
                this.$router.push({ name: 'Login' });
            })
        },
    },
}
</script>

<style>

</style>