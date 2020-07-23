<template lang="pug">
  //- <div id="app">
  //-   <div id="nav">
  //-     <router-link to="/">Home</router-link> |
  //-     <router-link to="/about">About</router-link>
  //-   </div>
  //-   <router-view/>
  //- </div>
  div#app
    <router-view />
</template>

<script>

export default {
  
}
</script>

<style lang="scss">
  @import "@/assets/css/style.scss";
</style>
