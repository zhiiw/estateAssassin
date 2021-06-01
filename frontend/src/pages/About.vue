<template>
  <q-card class="q-mx-auto q-mt-xl" style="width: 50%">
    <q-img
      src="https://cdn.quasar.dev/img/parallax1.jpg"
      basic
      style="height: 400px"
    />
    <p class="text-h1 text-weight-bold q-my-lg q-mx-md text-center">About US</p>
    <br>
    <q-card-section class="text-center">
      <q-list>
        <q-item clickable>
          <q-item-section avatar>
            <q-icon color="primary" name="face" style="font-size: 60px"/>
          </q-item-section>

          <q-item-section>
            <q-item-label class="text-h4 text-weight-bold"> 杨一凡 Ivan </q-item-label>
            <q-item-label class="text-h5" primary> 1930026147 </q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable>
          <q-item-section avatar>
            <q-icon color="orange" name="face" style="font-size: 60px"/>
          </q-item-section>

          <q-item-section>
            <q-item-label class="text-h4 text-weight-bold"> 刘语轩 McKellen </q-item-label>
            <q-item-label class="text-h5" primary> 1930026091 </q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable>
          <q-item-section avatar>
            <q-icon color="green" name="face" style="font-size: 60px"/>
          </q-item-section>

          <q-item-section>
            <q-item-label class="text-h4 text-weight-bold"> 吕浩洋 Noah </q-item-label>
            <q-item-label class="text-h5" primary> 1930026094 </q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable>
          <q-item-section avatar>
            <q-icon color="pink" name="face" style="font-size: 60px"/>
          </q-item-section>

          <q-item-section>
            <q-item-label class="text-h4 text-weight-bold"> 陈扬 Will </q-item-label>
            <q-item-label class="text-h5" primary> 1930026015 </q-item-label>
          </q-item-section>
        </q-item>

        <br>
      </q-list>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: "About"
}
</script>

<style scoped>

</style>
