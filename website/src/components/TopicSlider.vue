<template>
  <n-carousel show-arrow :show-dots="false" :loop="false" id="carousel">
    <template #arrow="{ prev, next, currentIndex }">
      <n-grid :cols="2" x-gap="12" class="mt mb">
        <n-gi>
          <n-button round secondary @click="prev" v-if="currentIndex > 0">
            <n-icon color="white" size="30"><ArrowBackFilled /></n-icon>
          </n-button>
        </n-gi>
        <n-gi>
          <n-button
            round
            secondary
            @click="next"
            v-if="currentIndex < topics.length - 1"
          >
            <n-icon color="white" size="30"><ArrowForwardFilled /></n-icon>
          </n-button>
          <n-button
            round
            type="info"
            @click="this.$emit('calculateScore')"
            v-else
          >
            Ergebnisse
          </n-button>
        </n-gi>
      </n-grid>
    </template>
    <rate-topic
      v-for="topic in topics"
      :key="topic"
      :info="topic"
      @updatePoints="updateScores"
      :showParty="showParty"
    />
  </n-carousel>
</template>
<script>
import RateTopic from "./RateTopic.vue";
import { NCarousel, NGrid, NIcon, NGi, NButton } from "naive-ui";
import { ArrowBackFilled, ArrowForwardFilled } from "@vicons/material";

export default {
  name: "TopicSlider",
  props: {
    topics: Object,
    showParty: Boolean,
  },
  components: {
    RateTopic,
    NCarousel,
    NGrid,
    NIcon,
    ArrowForwardFilled,
    ArrowBackFilled,
    NGi,
    NButton,
  },
  emits: ["calculateScore", "updatePoints"],
  methods: {
    updateScores(infoID, points) {
      this.$emit("updatePoints", infoID, points);
    },
  },
};
</script>
