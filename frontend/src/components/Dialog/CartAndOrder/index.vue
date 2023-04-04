<template lang="pug">
  dialog-container(
    label="Giỏ hàng"
    @on-close="$emit('on-close')"
    :value="show"
    :width="1000"
  )
    span.title Giỏ Hàng
    v-data-table(
      :headers="headers"
      :items="carts"
      class="elevation-1"
    )
      template(v-slot:item.name="{item}")
        span {{item.product.name}}
      template(v-slot:item.image="{item}")
        v-img(:src="item.product.images[0].url" max-width="80" )
      template(v-slot:item.price="{item}")
        span {{item.product.price}}
      template(v-slot:item.action="{item}")
        v-chip.pointer(color="green" dark)
          span Đăt hàng
        v-chip.pointer(color="red" dark)
          span Xóa

    span.title Đơn Mua
    v-data-table(
      :headers="headers"
      :items="orders"
      class="elevation-1"
    )
      template(v-slot:item.name="{item}")
        span {{item.product.name}}
      template(v-slot:item.image="{item}")
        v-img(:src="item.product.images[0].url" max-width="80" )
      template(v-slot:item.price="{item}")
        span {{item.product.price}}
      template(v-slot:item.action="{item}")
        v-chip.pointer(color="red" dark)
          span Xóa
    template(v-slot:actions)
      v-card-actions
</template>

<script>
import {defineComponent, computed} from 'vue'
import DialogContainer from '../../DialogContainer/index.vue'

const CartAndOrderDialog = defineComponent({
    components: {DialogContainer},
    props: {
        show: {default: false},
        carts: {default: () => []},
        orders: {default: () => []}
    },
    setup(props, {emit}) {
        const headers = [
            {text: 'Hình ảnh', value: 'image', align: 'start',},
            {text: 'Tên sản phẩm', value: 'name'},
            {text: 'Giá', value: 'price'},
            {text: 'Số Lượng', value: 'quantity'},
            {text: '', value: 'action'}
        ]
        return {
            headers
        }
    }
})

export default CartAndOrderDialog
</script>

<style lang="sass">
.pointer
  cursor: pointer
.title
  font-size: 17px
  color: green
  padding: 2px
</style>