<template>
  <div>
    <div ref="chartRef" class="chart"></div>
    <div ref="chartRef2" class="chart"></div>
  </div>
</template>

<script setup lang="ts">
import {useDark, useECharts} from "@pureadmin/utils";
import {computed, ref} from "vue";
import * as echarts from "echarts";
import {dataSgpScore} from "@/api/data/dataSgpScore";
const chartRef = ref();
const chartRef2 = ref();
const { isDark } = useDark();
const theme = computed(() => (isDark.value ? "dark" : "light"));
const chart1 = useECharts(chartRef, {
  theme,
  renderer: "canvas"
});
const chart2 = useECharts(chartRef2, {
  theme,
  renderer: "canvas"
});
const dataInfo = ref([])
const dataList = ref({
  name: [],
  data: []
})
const chartRander = () => {
  chart1.setOptions({
    title: {
      text: '考试科目人数占比',
      left: 'center'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',
      left: 'left'
    },
    series: [
      {
        type: 'pie',
        radius: '50%',
        data: dataInfo.value,
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  })

  chart2.setOptions({
    title: {
      text: 'SGP平均分对比',
      left: 'center'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',
      left: 'left'
    },
    xAxis: {
      type: 'category',
      data: dataList.value.name
    },
    yAxis: {
      type: 'value',
      max: 50,
      min: 49.5
    },
    series: [
      {
        data: dataList.value.data,
        type: 'bar',
        barWidth: 20,
        type: 'bar',
        showBackground: true,
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: '#83bff6' },
            { offset: 0.5, color: '#188df0' },
            { offset: 1, color: '#188df0' }
          ])
        },
        emphasis: {
          itemStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              { offset: 0, color: '#2378f7' },
              { offset: 0.7, color: '#2378f7' },
              { offset: 1, color: '#83bff6' }
            ])
          }
        },
      }
    ]
  })
}

dataSgpScore.demoSgp().then(res => {
  console.log(res)
  dataInfo.value = res.data.map(item => {
    return {
      value: item.num,
      name: '考试科目编号：'+item.sgp考试科目,
    }
  });
  res.data.forEach(item => {
    dataList.value.name.push('考试科目编号：'+item.sgp考试科目);
    dataList.value.data.push(item.sgp);
  })
  chartRander()
})
</script>

<style scoped lang="scss">

.chart {
  width: 500px;
  height: 300px;
  margin: 30px auto;
}
</style>
