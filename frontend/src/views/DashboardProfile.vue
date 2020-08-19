<template lang="pug">
    .user-box
        .user-info
            p.user-heading Thông tin người dùng
            .input-group
                label Họ tên
                input(type="text", v-model="name", v-bind:disabled="isDisabledName")
                span(v-on:click="isDisabledName = !isDisabledName") Sửa
            .input-group
                label Email
                input(type="text", v-model="email", v-bind:disabled="isDisabledEmail")
                span(v-on:click="isDisabledEmail = !isDisabledEmail") Sửa
            p(style="text-align: left; margin-left: 10px;") Ngày tạo: {{ created_on }}
        .change-password
            p.user-heading Đổi mật khẩu
            .input-group
                label Mật khẩu cũ
                input(type="text")
            .input-group
                label Mật khẩu mới
                input(type="text")
            .input-group
                label Nhập lại mật khẩu mới
                input(type="text")
        button(v-on:click="Save()") Lưu        
</template>

<script>
import axios from 'axios'
export default {
    name: 'DashboardProfile',
    data() {
        return {
            base_url: `http://localhost:8000/`,
            isDisabledEmail: true,
            isDisabledName: true,
            name: localStorage.getItem('name'),
            email: localStorage.getItem('email'),
            created_on: localStorage.getItem('created_on')
        }
    },
    methods: {
        Save() {
            if (confirm("Bạn có muốn lưu thay đổi ?")) {
                axios({
                    method: 'patch',
                    url: this.base_url + `api/profile/` + localStorage.getItem('id') + `/`,
                    data: {
                        "email": this.email,
                        "name": this.name  
                    },
                    headers: {
                        'Authorization': localStorage.getItem('Authorization'),
                        'Content-Type': 'application/json'
                    }   
                })
                .then(() => {
                    localStorage.setItem('name', this.name);
                    this.isDisabledName = true;
                    localStorage.setItem('email', this.email);
                    this.isDisabledEmail = true;
                    alert("Cập nhật thông tin thành công!")
                })
                .catch((err) => {
                    alert(JSON.stringify(err.response.data, null, 4));
                });
            }
        }
    }
}
</script>

<style>

</style>