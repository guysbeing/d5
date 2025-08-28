<template>
  <el-card class="upload-card" >
    <h2 >Upload file</h2>

    <div
        class="upload-area"
        @click="triggerUpload"
        @dragover.prevent
        @drop.prevent="handleDrop"
    >
      <el-upload
          ref="uploadRef"
          :before-upload="beforeUpload"
          :auto-upload="false"
          :show-file-list="false"

      >
        <p v-if="!fileName" class="up-t" >
          <el-icon class="el-icon--upload"><upload-filled /></el-icon>
          Drag your resume file to this area, or click on the area to select the appropriate file to upload</p>
        <p v-else>Uploaded file: {{ fileName }}</p>
      </el-upload>
    </div>

    <div class="button-group">
      <el-button :disabled="!fileName" @click="$emit('last-step')" type="primary" plain color="#1B5AFF">Last step</el-button>
      <el-button :disabled="!fileName" @click="$emit('finish', fileName)" type="primary" color="#1B5AFF">Finish</el-button>
    </div>
    <div >
      <el-steps class="step" :active="2" finish-status="success" align-center>
        <el-step/>
        <el-step/>
        <el-step />
      </el-steps>
    </div>

  </el-card>
</template>

<script setup>
import { ref } from 'vue';
import {UploadFilled} from "@element-plus/icons-vue";

const uploadRef = ref(null);
const fileName = ref('');

const triggerUpload = () => {
  uploadRef.value.$el.querySelector('input[type="file"]').click();
};

const beforeUpload = (file) => {
  fileName.value = file.name;
  return false;
};

const handleDrop = (e) => {
  const file = e.dataTransfer.files[0];
  if (file) fileName.value = file.name;
};
</script>

<style scoped>
.upload-card {
  border-radius: 10px;
  padding: 40px;
  text-align: center;
}

.upload-card h2 {

  text-align: left;
  margin: 0 0 30px 0;
}
.upload-area {
  border: 2px dashed #409EFF;
  padding: 40px 20px;
  cursor: pointer;
  transition: background 0.3s;
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 30vh;

}
.up-t{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.upload-area:hover {
  background-color: #ecf5ff;
}
.el-icon--upload {
  font-size: 48px;
  color: #409EFF;
  margin-bottom: 16px;
  cursor: pointer;
}

.el-icon--upload:hover {
  color: #66b1ff;
}

.button-group {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-bottom: 20px;
}
.step{
  width: 60%;
  display: flex;
  justify-items: center;
  align-content: center;
  margin: 0 auto;
}
.step ::v-deep(.el-step__head.is-success){
  color: #1B5AFF !important;
}

.step ::v-deep(.el-step__line) {
  background-color: #1B5AFF !important;

}
</style>
