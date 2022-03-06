<template>
  <n-space vertical>
    <h1>{{ info.value }}</h1>
    <n-grid x-gap="12" y-gap="12" cols="1 s:2 m:3 xl:6" responsive="screen">
      <n-gi
        v-for="(party, index) in party_mixed"
        :key="party.value"
        :value="party.value"
      >
        <n-card
          :title="this.showParty ? party.name : 'Partei #' + (index + 1)"
          style="height: 100%"
        >
          <div
            @click="openModal(index + 1, party.text, party.name)"
            style="word-wrap: break-word"
          >
            <n-ellipsis :line-clamp="15" :tooltip="false">
              {{ party.text }}
            </n-ellipsis>
          </div>
          <n-button
            text
            color="blue"
            @click="openModal(index + 1, party.text, party.name)"
          >
            Weiterlesen
          </n-button>

          <template #action>
            <n-rate
              :on-update:value="(value) => updateRating(value, party.id)"
            />
          </template>
        </n-card>
      </n-gi>
    </n-grid>
    <n-modal
      v-model:show="showModal"
      preset="card"
      :title="info.value"
      :bordered="false"
      id="textModal"
    >
      <template #header-extra>{{ modalTitle }} </template>
      {{ modalText }}
    </n-modal>
  </n-space>
</template>

<script>
import { defineComponent, ref } from "vue";

import {
  NSpace,
  NCard,
  NGrid,
  NGi,
  NEllipsis,
  NRate,
  NModal,
  NButton,
} from "naive-ui";

export default defineComponent({
  name: "RateTopic",
  props: {
    info: Object,
    showParty: Boolean,
  },
  components: {
    NSpace,
    NCard,
    NGrid,
    NGi,
    NRate,
    NEllipsis,
    NModal,
    NButton,
  },
  emits: ["updatePoints"],
  data() {
    return {
      points: [],
      modalTitle: "",
      modalText: "",
    };
  },
  setup(props) {
    const party_mixed = props.info.parties
      .map((value) => ({ value, sort: Math.random() }))
      .sort((a, b) => a.sort - b.sort)
      .map(({ value }) => value);
    return {
      party_mixed,
      showModal: ref(false),
    };
  },
  methods: {
    updateRating(value, partyID) {
      this.points[partyID] = value;
      this.$emit("updatePoints", this.info.id, this.points);
    },
    openModal(index, text, name) {
      this.modalTitle = this.showParty ? name : "Partei #" + index;
      this.modalText = text;
      this.showModal = true;
    },
  },
});
</script>

<style scoped>
span.n-ellipsis {
  word-wrap: break-word;
  max-width: 100%;
}
</style>

<style>
#textModal {
  width: 100%;
}

@media only screen and (min-width: 800px) {
  #textModal {
    width: 80%;
  }
}

@media only screen and (min-width: 1000px) {
  #textModal {
    width: 60%;
  }
}
</style>
