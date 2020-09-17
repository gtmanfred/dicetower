<template>
  <div class="dice">
    <b-btn pill varient="outline-secondary" v-on:click="result = roll()">Button</b-btn>
    <h1>{{result}}</h1>
  </div>
</template>

<script>
import SwaggerClient from 'swagger-client';

export default {
  name: 'Dice',
  data: function() {
    return {
      result: null,
      client: new SwaggerClient('http://localhost:8000/openapi.json')
    };
  },
  methods: {
    roll: function() {
      this.client.then(
        client => client.apis.dice.roll_api_v1_dice_get()
      ).then(
        (result) => {
          this.result = result.body.result
        }
      )
    }
  }
}
</script>
