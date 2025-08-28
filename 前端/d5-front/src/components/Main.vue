<template>
  <div class="resume-upload" :class="{ mobile: isMobile }">
    <!-- 左侧文案 + 插图 -->
    <div class="left-section" :class="isMobile ? 'mobile' : 'pc-height'">
      <h2>Finish!</h2>
      <h2>Upload Your Resume</h2>
      <p>Upload your resume, the platform will help you parse and optimize, you can also skip this step</p>
      <img v-if="!isMobile" class=illustration src="@/assets/img.svg" alt="illustration"/>

    </div>

    <!-- 上传区域 -->
    <div class="upload-sec" :class="isMobile ? 'mobile' : 'pc-height'">
      <uploader/>
    </div>
  </div>
</template>

<script setup>
import {ref, onMounted, onUnmounted} from 'vue';
import Uploader from "@/components/uploader.vue";



const isMobile = ref(false);
const checkMobile = () => {
  isMobile.value = window.innerWidth < 768;
};

onMounted(() => {
  checkMobile();
  window.addEventListener('resize', checkMobile);
});
onUnmounted(() => window.removeEventListener('resize', checkMobile));

</script>

<style scoped>
.resume-upload {
  display: flex;
  padding: 0 40px 0 40px;
  gap: 20px;
  align-items: center;
  min-height: 100vh;
}

/* 桌面端左右布局 */
.resume-upload:not(.mobile) {
  flex-direction: row;
}

/* 移动端上下布局 */
.resume-upload.mobile {
  flex-direction: column;
}


.pc-height{
  min-height: calc(100vh - 10vh);
  padding-top: 10vh;

}
.upload-sec{
  flex:7;
  align-content: start;

}
.left-section{
  flex: 6;
  align-content: start;
  position: relative;
}
.left-section h2 {
  margin-top: 10px;
  font-size: 28px;
  margin-bottom: 10px;
}

.left-section p {
  color: #666;
  margin-bottom: 20px;
}


.illustration {
  position: absolute;
  left: 0;
  bottom: 0;
}

</style>
