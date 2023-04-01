export const categories = {
    state () {
        return {
            categories: []
        }
    },
    mutations: {
        updateCategories(state, value) {
            state.categories = value
        }
    }
}