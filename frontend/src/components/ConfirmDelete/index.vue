<template lang="pug">
  confirm-dialog(
    :showDialog="showDialog"
    :messages="setMessage()"
    :color-confirm="'red'"
    @on-cancel="closeDialog('cancel')"
    @on-ok="closeDialog('delete')"
  )
</template>

<script>
import {defineComponent, getCurrentInstance} from 'vue'
import ConfirmDialog from '../ConfirmDialog/index'

const JConfirmDelete = defineComponent({
  components: {
    ConfirmDialog
  },
  props: {
    showDialog: {
      type: Boolean,
      required: true
    },
    itemLabel: {
      type: String,
      required: false
    }
  },
  setup(props, {emit}) {
    const {$root} = getCurrentInstance().proxy
    const closeDialog = (param) => {
      emit('on-close', param)
    }

    const setMessage = () => {
      return ['Bạn muốn xóa mục này?']
    }

    return {
      closeDialog,
      setMessage
    }
  }
})
export default JConfirmDelete
</script>