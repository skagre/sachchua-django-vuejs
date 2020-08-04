<template lang="pug">
    .login-container
        .login
            router-link(:to="{ path: '/login' }") 
                img(src="@/assets/images/logo.png", alt="logo")
                h1 Sách chùa Admin Login
            .input-group
                label Email
                input(type="text", required, placeholder="email", v-model="email")
            .input-group
                label Password
                input(type="password", required, placeholder="password", v-model="password")
            button(v-on:click="login()") Đăng nhập
</template>

<script>
import axios from 'axios'
export default {
    name: 'Login',
    data() {
        return {
            base_url: `http://localhost:8000/`,
            email: '',
            password: '',
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
        login() {
            axios.post(this.base_url + `api/login/`, {"username": this.email, "password": this.password})
            .then((res) => {
                if(res.data != '') {
                    localStorage.setItem('Authorization', 'Token: ' + res.data.token)
                    this.$router.push({ name: 'Dashboard' });
                }
            })
        }
    }
}
</script>

<style>

</style>