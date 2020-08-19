<template lang="pug">
    .addbook-container
        .addbook-heading
            h2 Thêm mới sách
        .addbook-content
            .left
                .input-group
                    label Tên sách
                    input(type="text", v-model="title")
                .input-group
                    label Tác giả
                    input(type="text", v-model="author")
                .input-group
                    label Thể loại
                    select(v-model="category")
                        <option disabled value="">Chọn thể loại</option>
                        option(v-for="category in categories", :key="category.id", v-bind:value="category.id") 
                            | {{ category.name }}
                .input-group
                    label Thumbnail
                    input(type="file", accept="image/gif, image/jpeg", ref="thumbnail", v-on:change="handleThumbnailUpload")
                .input-group
                    label File PDF
                    input(type="file", accept="application/pdf,application/vnd.ms-excel", ref="file", v-on:change="handleFileUpload()")
                button(v-on:click="addBook()") Lưu
                router-link(:to="{ path: '/dashboard/books' }", id="cancel") Hủy
            .right
                .input-group
                    label Nội dung
                    textarea(v-model="content")
</template>

<script>
import axios from 'axios'
export default {
    name: 'AddBook',
    data() {
        return {
            base_url: `http://localhost:8000/`,
            title: '',
            author: '',
            content: '',
            thumbnail: '',
            file: '',
            category: '',
            categories: null,
        }
    },
    created() {
        this.loadCategories();
    },
    methods: {
        loadCategories() {
            axios({
                method: 'get',
                url: this.base_url + `api/category/?limit=100`,
            })
            .then((res) => {
                this.categories = res.data.results;
            })
            .catch((err) => {
                alert(JSON.stringify(err.response.data, null, 4));
            });
        },
        handleThumbnailUpload() {
            this.thumbnail = this.$refs.thumbnail.files[0];
        },
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
        },
        addBook() {
            let f = new FormData();

            f.append('thumbnail', this.thumbnail);
            f.append('title', this.title);
            f.append('author', this.author);
            f.append('content', this.content);
            f.append('file', this.file);
            f.append('category', this.category);
            f.append('user', localStorage.getItem('id'));

            axios({
                method: 'post',
                url: this.base_url + `api/book/`,
                data: f, 
                headers: {
                    'Authorization': localStorage.getItem('Authorization'),
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(() => {
                alert("Thêm mới thành công!");
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