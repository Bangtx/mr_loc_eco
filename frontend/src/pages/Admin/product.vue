<template lang="pug">
  div.pa-10
    v-text-field(v-model='products.name' label='Name')
    v-text-field(v-model='products.sales' label='Sales')
    v-text-field(v-model='products.cost' label='Cost')
    v-text-field(v-model='products.price' label='Price')
    v-text-field(v-model='products.star' label='Star')
    v-text-field(v-model='products.cmt' label='Cmt')
    v-text-field(v-model='products.shipCmt' label='Ship Cmt')
    v-file-input(
      v-model="products.image"
      show-size
      counter
      multiple
      label="File input"
    )
    v-btn.me-4(@click='submit')
      | submit

</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      products: {
        image: null,
        name: 'Tủ lạnh ô tô Kemin K20 - 20L Chính hãng',
        star: 5,
        sales: 1000,
        cost: 1200,
        price: 10000,
        cmt: 'Tặng tới 467 ASA (106k ₫)',
        shipCmt: 'Giao tất cả các ngày trong tuần',
        category: 1
      }
    }
  },
  methods: {
    async submit() {
      this.products.image = await this.readFile(this.products.image[0])
      axios.post('http://127.0.0.1:8000/product/', this.products).then((responce) => {
        console.log(responce)
      })
    },
    readFile(file) {
      return new Promise((r => {
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onloadend = () => r(reader.result)
      }))
    }
  }
}
</script>