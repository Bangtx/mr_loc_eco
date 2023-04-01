<template lang="pug">
  //v-card.mx-auto(max-width='300' tile='')
  v-row.justify-center
    .border.width-card.pa-8
      div.cat-item(v-for='(item, i) in items' :key='i')
        v-img.img(:src='item.icon' width="40" )
        span.text-small.text-center {{ item.text }}

</template>

<script>
const MobileCategories = {
  props: {
    title: {default: ''},
    selectedItem: {default: 0},
    items: {default: () => []}
  },
  data() {
    return {}
  }
}

export default MobileCategories
</script>

<style scoped lang="sass">
.border
  //width: fit-content
  display: flex
  overflow-x: auto
.cat-item
  display: block
  width: 80px
.text-small
  font-size: 10px
.img
  margin: auto
  justify-content: center
</style>