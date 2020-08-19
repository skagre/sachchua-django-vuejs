<template lang="pug">
    .book-container
        .book-heading
            h2 Quản lý sách
            router-link(:to="{ path: '/dashboard/addbook' }") Thêm mới
        .book-content
            .list-book
                span.col1 ID
                span.col2 Ảnh
                span.col3 Tiêu đề sách
                span.col4 Tác giả
                span.col5 Thể loại
                span.col6 Hành động
            p(v-if="books.length == 0", style="margin-top: 30px; color: red; font-weight: bold;") Không có sách, hãy thêm mới !
            div(v-for="book in books", :key="book.id")
                .list-book 
                    span.col.col1 \#{{ book.id }}
                    span.col.col2
                        img(v-bind:src="book.thumbnail", alt="alt")
                    span.col.col3 {{ book.title }}
                    span.col.col4 {{ book.author }}
                    span.col.col5 {{ book.category_name }}
                    span.col.col6
                        a(v-on:click="editBook(book.id)") Sửa
                        a(v-on:click="deleteBook(book.id)") Xóa
                    span.col.col7 Đăng bởi: 
                        span {{ book.created_by }} 
                            | Ngày: {{ book.created_on }}
                    span.col.col8 Cập nhật bởi: 
                        span(v-if="book.user_updated == null") --- 
                            | Ngày: ---
                        span(v-else) {{ book.user_updated }} 
                            | Ngày: {{ book.updated_on }}
        
        .pagination
            ul
                li(v-for="i in Math.ceil(count / 5)")
                    button(v-on:click="loadBooks((i-1)*5)") {{ i }}
                

</template>

<script>
import axios from 'axios'
export default {
    name: 'DashboardBooks',
    data() {
        return {
            base_url: `http://localhost:8000/`,
            books: null,
            count: 0
        }
    },
    created() {
        this.loadBooks();
    },
    methods: {
        loadBooks(offset = null) {
            axios({
                method: 'get',
                url: this.base_url + `api/book/?limit=5&offset=` + offset,
            })
            .then((res) => {
                this.books = res.data.results;
                this.count = res.data.count;
            })
            .catch((err) => {
                alert(JSON.stringify(err.response.data, null, 4));
            });
        },
        deleteBook(id) {
            if (confirm("Bạn chắc chắn muốn xóa?"))
            {
                axios({
                    method: 'delete',
                    url: this.base_url + `api/book/` + id,
                    headers: {
                        'Authorization': localStorage.getItem('Authorization')
                    }   
                })
                .then(() => {
                    this.loadBooks();
                })
                .catch((err) => {
                    alert(JSON.stringify(err.response.data, null, 4));
                });
            }
        },
        editBook(id) {
            this.$router.push({ path: 'editbook/' + id }).catch(()=>{});
        }
    }
}
</script>

<style>

</style>