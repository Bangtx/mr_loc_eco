<template lang="pug">
  dialog-container(
    label="Thông báo"
    @on-close="$emit('on-close')"
    :value="show"
    :width="400"
  )
    .pa-4
      p {{label}}
    template(v-slot:actions)
      v-card-actions
        v-col(cols="12")
          v-btn.relative-btn.white--text(
            :large="!$vuetify.breakpoint.xsOnly"
            block
            color="#f57e2e"
            @click="openRegisterDialog(true)"
          ) Đăng nhập
</template>

<script>
import {defineComponent, inject, ref} from 'vue'
import DialogContainer from '../../DialogContainer/index.vue'

const ConfirmDialog = defineComponent({
    components: {DialogContainer},
    props: {
        show: {default: false},
        label: {default: ''}
    },
    setup(props, {emit}) {
        const detailPage = inject('detailPage')

        const openRegisterDialog = () => {
            detailPage.$refs.headerBar.openAccountDialog()
            emit('on-close')
        }

        return {
            openRegisterDialog
        }
    }
})

export default ConfirmDialog
</script>