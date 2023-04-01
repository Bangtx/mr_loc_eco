<template lang="pug">
  div
    v-file-input(
      accept="image/*"
      label="File input"
      v-model="image"
    )
    v-img(:src="url" width="300" )
    span {{ url }}
    v-btn(@click="upload()") 3444
</template>

<script>
import axios from 'axios'
const Input = {
  data() {
    return {
      image: null
    }
  },
  methods: {
    async upload() {
      // let formData = new FormData();
      // formData.append('file', this.image);
      // console.log(formData.file)
      const formData = {
        file: await this.readFile(this.image)
      }
      axios.post(
        "http://127.0.0.1:8000/image/"
        ,formData
      )
      .then(response => {
        //...
      })
      .catch(e => {
         //...
      })
    },
    readFile(file) {
      return new Promise((r => {
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onloadend = () => r(reader.result)
      }))
    }
  },
  computed: {
    url() {
      if (!this.image) return;
      return URL.createObjectURL(this.image);
    }
  }
}

export default Input
</script>