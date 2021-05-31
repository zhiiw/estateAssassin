<template>
  <div>
    {{id}}
  </div>
</template>

<script>
export default {
  name: "Info",
  data () {
    return {
      id: 5209
    }
  },
  created() {
    if(this.$route.params.id !== undefined)
      this.id = this.$route.params.id
  }
}
</script>

<style scoped>

</style>
