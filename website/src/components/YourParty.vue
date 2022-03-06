<template>
  <n-card title="DEINE PARTEI" size="huge">
    <h3>
      Entsprechend deiner Punktevergabe, hast du am meisten Übereinstimmung mit:
      {{ this.result[0].name }}
    </h3>
    <n-table :bordered="false" :single-line="false">
      <thead>
        <tr>
          <th>Partei</th>
          <th>Punkte</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="party in result" :key="party">
          <td>{{ party.name }}</td>
          <td>{{ party.score }}</td>
        </tr>
      </tbody>
    </n-table>
    <n-grid cols="1 m:2" responsive="screen">
      <n-gi>
        <n-button
          round
          secondary
          type="primary"
          @click="this.$emit('reset', false)"
          class="mt"
        >
          Nochmal?
        </n-button>
      </n-gi>
      <n-gi>
        <n-button
          round
          secondary
          type="primary"
          @click="this.$emit('reset', true)"
          class="mt"
        >
          Nochmal mit Parteinamen?
        </n-button>
      </n-gi>
    </n-grid>
  </n-card>
</template>

<script>
import { NButton, NCard, NTable, NGrid, NGi } from "naive-ui";

export default {
  name: "YourParty",
  props: {
    result: Object,
  },
  components: {
    NButton,
    NCard,
    NTable,
    NGrid,
    NGi,
  },
  emits: ["reset"],
};
</script>
