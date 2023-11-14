<template>
    <div class="bookmark-card">

        <div class="bookmark-content">

            <p class="bookmark-name">{{ bookmark && bookmark.name ? bookmark.name.toUpperCase() : '' }}</p>
            <a :href="bookmark && bookmark.link" target="_blank">{{ bookmark && bookmark.name }}</a>


            <button @click="removeBookmark">🗑️</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'BookmarkCard',
    props: {
        bookmark: Object
    },

    methods: {
        removeBookmark() {

            this.$emit('remove', this.bookmark);
        }
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Abel&display=swap');

.bookmark-card {
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 10px;
    background-color: #1C1A1C;
    border-radius: 19px;
    text-align: center;
}

a {
    color: #fa82ae;
}

.bookmark-content {
    text-align: center;
    font-family: 'Abel', sans-serif;

}

.bookmark-name {
    color: wheat;
    font-family: 'Abel', sans-serif;
    font-size: 18px;
    font-weight: bold;
}

.bookmark-link {
    font-size: 14px;
}
</style>