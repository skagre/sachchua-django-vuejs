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
            axios({
                method: 'post',
                url: this.base_url + `api/checklogin/`,
                headers: {
                    'Authorization': localStorage.getItem('Authorization')
                }
            })
            .then((res) => {
                if(res.data.id != null) {
                    localStorage.setItem('id', res.data.id);
                    localStorage.setItem('email', res.data.email);
                    localStorage.setItem('name', res.data.name);
                    localStorage.setItem('created_on', res.data.created_on);
                    this.$router.push({ path: 'dashboard/profile' }).catch(()=>{});
                }
            })
            .catch(() => {
                this.$router.push({ name: 'Login' }).catch(()=>{});
            })
        },
        login() {
            if (this.email == '')
                return alert("Email không được trống!");
            else if (this.password == '')
                return alert("Password không được trống!");
            
            axios.post(this.base_url + `api/login/`, {"username": this.email, "password": this.password})
            .then((res) => {
                if(res.data != '') {
                    localStorage.setItem('Authorization', 'Token ' + res.data.token);
                    this.checklogin();
                    //this.$router.push({ path: 'dashboard/profile' }).catch(()=>{});
                }
            })
            .catch((err) => {
                alert(JSON.stringify(err.response.data, null, 4));
            });
        }
    }
}
</script>

<style>

</style>