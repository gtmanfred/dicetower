<template>
  <div class="dice">
    <input id="formula" v-model="formula" placeholder="roll: 1d20">
    <b-button id="roll" pill variant="success" v-on:click="result = roll()">Roll!</b-button>
  </div>
</template>

<script>
import SwaggerClient from 'swagger-client';
import * as THREE from 'three';

export default {
  name: 'Dice',
  data: function() {

    let scene = new THREE.Scene();

    let camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerWidth, 0.1, 100);
    camera.position.set(10, 4, 4);
    camera.lookAt(new THREE.Vector3(0, 0, 0));

    let light = new THREE.PointLight(0xFFFFFF, 1, 500);
    light.position.set(10, 0, 25);
    scene.add(light)

    return {
      result: null,
      client: new SwaggerClient("/openapi.json"),
      scene: scene,
      camera: camera,
      renderer: null,
      formula: null,
      dice: [],
    };
  },
  beforeMount() {
    this.renderer = new THREE.WebGLRenderer({alpha: true, antialias: true});
    this.renderer.setClearColor("#e5e5e5");
    document.body.appendChild(this.renderer.domElement);
    window.addEventListener('resize', () =>{
      this.renderer.setSize(window.innerWidth, window.innerHeight);
      this.camera.aspect = window.innerWidth / window.innerHeight;
      this.camera.updateProjectionMatrix();
    })
    requestAnimationFrame(this.render);
  },
  mounted() {
    this.renderer.setSize(window.innerWidth, window.innerHeight);
  },
  methods: {
    render: function() {
      this.renderer.render(this.scene, this.camera);
      requestAnimationFrame(this.render);
    },
    roll: function() {
      this.client.then(
        client => client.apis.dice.roll_api_v2_dice_get({roll: this.formula})
      ).then(
        (result) => {
          this.result = result.body.result;
          this.dice = result.body.dice;
        }
      ).then(() => {
        let geometry = new THREE.BoxGeometry(1, 1, 1);
        let material = new THREE.MeshLambertMaterial({color: 0xFFCC00});
        let mesh = new THREE.Mesh(geometry, material);
        this.scene.add(mesh);
        this.render();
      });
    }
  }
}
</script>
