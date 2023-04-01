<template lang="pug">
  v-carousel(:height="height")
    v-carousel-item(v-for='(image, i) in images' :key='i' :src='image' reverse-transition='fade-transition' transition='fade-transition')

</template>

<script>
const Carousel = {
  props: ['isMobile'],
  data() {
    return {
      images: [
        'https://phukienpeugeot.com/wp-content/uploads/2019/02/banner-ngoai-that-phu-kien-peugeot-02-1400x373.jpg'
      ],
      height: 250
    }
  },
  mounted() {
    const width = screen.width
    if (width <= 600) this.height = 150
    else if (width <= 900 && width > 600) this.height = 200
    else this.height = 250
  }
}

export default Carousel
</script>