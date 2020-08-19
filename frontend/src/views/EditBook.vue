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
                    input(type="text", id="copyThumbnailUrl", v-model="thumbnailUrl", readonly)
                    .group
                        span(v-on:click="copyThumbnailUrl()") Copy
                        a(v-bind:href="thumbnailUrl", target="_blank") Xem
                        input(type="file", accept="image/gif, image/jpeg", ref="thumbnail", v-on:change="handleThumbnailUpload")
                .input-group
                    label File PDF
                    input(type="text", id="copyFileUrl", v-model="fileUrl", readonly)
                    .group
                        span(v-on:click="copyFileUrl()") Copy
                        a(v-bind:href="fileUrl", target="_blank") Xem
                        input(type="file", accept="application/pdf,application/vnd.ms-excel", ref="file", v-on:change="handleFileUpload()")
                button(v-on:click="editBook()") Lưu
                router-link(:to="{ path: '/dashboard/books' }", id="cancel") Hủy
            .right
                .input-group
                    label Nội dung
                    textarea(v-model="content")
</template>

<script>
import axios from 'axios'
export default {
    name: 'EditBook',
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
            book: null,

            fileUrl: '',
            thumbnailUrl: '',
        }
    },
    created() {
        this.loadCategories();
        this.loadBook();
    },
    methods: {
        copyFileUrl() {
            var c = document.getElementById('copyFileUrl');
            c.select();
            document.execCommand("copy");
            alert('Copy thành công !')
        },
        copyThumbnailUrl() {
            var c = document.getElementById('copyThumbnailUrl');
            c.select();
            document.execCommand("copy");
            alert('Copy thành công !')
        },
        loadBook() {
            axios({
                method: 'get',
                url: this.base_url + `api/book/` + this.$route.params.id,
            })
            .then((res) => {
                this.title = res.data.title;
                this.author = res.data.author;
                this.content = res.data.content;
                this.category = res.data.category;
                this.fileUrl = res.data.file;
                this.thumbnailUrl = res.data.thumbnail;
            })
            .catch((err) => {
                alert(err);
            });
        },
        loadCategories() {
            axios({
                method: 'get',
                url: this.base_url + `api/category/`,
            })
            .then((res) => {
                this.categories = res.data.results;
            })
            .catch((err) => {
                alert(err);
            });
        },
        handleThumbnailUpload() {
            this.thumbnail = this.$refs.thumbnail.files[0];
            this.thumbnailUrl = 'uploading...';
        },
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
            this.fileUrl = 'uploading...';
        },
        editBook() {
            let f = new FormData();

            if (this.thumbnailUrl == 'uploading...') {
                f.append('thumbnail', this.thumbnail);
            }
            if (this.fileUrl == 'uploading...') {
                f.append('file', this.file);
            }
            
            f.append('title', this.title);
            f.append('author', this.author);
            f.append('content', this.content);
            f.append('category', this.category);
            f.append('user', localStorage.getItem('id'));

            axios({
                method: 'patch',
                url: this.base_url + `api/book/` + this.$route.params.id + '/',
                data: f, 
                headers: {
                    'Authorization': localStorage.getItem('Authorization'),
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(() => {
                alert("Cập nhật thành công!");
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