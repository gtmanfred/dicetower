<template>
  <div id="app">
    <Dice/>
  </div>
</template>

<script>
import Dice from './components/Dice.vue'

export default {
  name: 'App',
  components: {
    Dice,
  },
  methods: {
    roll: function() {
      console.log('APP');
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
