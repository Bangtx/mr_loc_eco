<template lang="pug">
  dialog-container(
    label="Tài Khoản"
    @on-close="$emit('on-close')"
    :value="show"
    :width="400"
  )
    v-text-field(
      label="Code (Tên đăng nhập)"
      v-model="masterData.code"
    )
    v-text-field(
      label="Mật Khẩu"
      type="password"
      v-model="masterData.password"
    )
    div(v-if="!isLogin")
      v-text-field(
        label="Tên"
        v-model="masterData.name"
      )
      v-text-field(
        label="Điện Thoại"
        v-model="masterData.tel"
      )
      v-text-field(
        label="Email"
        v-model="masterData.email"
      )
      v-text-field(
        label="Địa chỉ"
        v-model="masterData.address"
      )
    template(v-slot:actions)
      v-card-actions
        v-col(:cols="isLogin ? 6 : 12")
          v-btn.relative-btn.white--text(
            :large="!$vuetify.breakpoint.xsOnly"
            block
            color="#f57e2e"
            @click="isLogin ? isLogin = false : onRegister"
          )
            | Đăng kí
        v-col(cols="6" v-if="isLogin")
          v-btn.relative-btn.white--text(
            :large="!$vuetify.breakpoint.xsOnly"
            block
            color="#f57e2e"
            @click="onLogin"
          )
            | Đăng Nhập
</template>

<script>
import {defineComponent, ref, watch} from "vue";
import DialogContainer from "../../DialogContainer/index.vue";
import {createData} from "@/utils";

const AccountDialog = defineComponent({
    components: {DialogContainer},
    props: {
        show: {default: false}
    },
    setup(props, {emit}) {
        const masterData = ref({})
        const isLogin = ref(true)

        const onRegister = async () => {
            await createData('/user/', masterData.value)
            alert('create successful')
            emit('on-close')
        }

        const onLogin = async () => {
            const data = await createData(
                '/user/login', {code: masterData.value.code, password: masterData.value.password}
            )
            if (data.status === 400) alert('Login failed')
            if (data.status === 200) {
                alert('Login successful')
                localStorage.setItem('user', JSON.stringify(data.data))
                emit('on-close')
            }
        }

        watch(
            () => props.show,
            () => {
                if (props.show) {
                    isLogin.value = true
                    masterData.value = {
                        code: null,
                        password: null,
                        name: null,
                        tel: null,
                        email: null,
                        address: null
                    }
                }
            }
        )

        return {
            masterData,
            isLogin,
            onRegister,
            onLogin
        }
    }
})

export default AccountDialog
</script>