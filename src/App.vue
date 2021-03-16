<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Homework Manager</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <v-container>
        <v-btn
          v-if="inputState < 2"
          class="ma-1"
          v-on:click="showParseTxtF()"
          color="primary"
          >Add Homework by Parsing Text</v-btn
        >
        <v-btn
          v-if="inputState < 2"
          class="ma-1"
          v-on:click="manualInput()"
          color="primary"
          >Add Homework by Manual Input</v-btn
        >
        <v-btn
          v-if="inputState == 3"
          class="ma-1"
          v-on:click="inputState = 1"
          color="red darken-4"
          dark
          >Cancel</v-btn
        >
        <v-btn
          v-if="inputState == 2"
          class="ma-1"
          v-on:click="inputState = 0"
          color="red darken-4"
          dark
          >Cancel</v-btn
        >
        <v-btn
          right
          v-if="inputState == 3 || inputState == 2"
          class="ma-1"
          v-on:click="submit()"
          color="primary"
          >Add</v-btn
        >
        <br />
        <v-container v-show="inputState == 1">
          <v-textarea v-model="txtToParse" outlined></v-textarea>
          <v-btn v-on:click="parse()" color="primary">Parse</v-btn>
        </v-container>
        <v-card class="ma-3" v-if="inputState == 3">
          <v-list outlined>
            <template v-for="(item, index) in parsedHW">
              <v-list-item :key="index">
                <v-list-item-content>
                  <v-list-item-title>Class Name:</v-list-item-title>
                </v-list-item-content>
                <v-list-item-content>
                  <v-text-field
                    v-model="parsedHW[index]['className']"
                  ></v-text-field>
                </v-list-item-content>
              </v-list-item>
              <v-list-item :key="index+'2'">
                <v-list-item-content>
                  <v-list-item-title>Homework Name:</v-list-item-title>
                </v-list-item-content>
                <v-list-item-content>
                  <v-text-field
                    v-model="parsedHW[index]['homeworkName']"
                  ></v-text-field>
                </v-list-item-content>
              </v-list-item>

              <v-list-item :key="index + '3'">
                <v-list-item-content>
                  <v-list-item-title>Due Date:</v-list-item-title>
                </v-list-item-content>
                <v-list-item-content>
                  <br />

                  <v-container>
                    <v-row>
                      <v-col class="pa-0">
                        <v-text-field
                          class="mr-3"
                          v-model="parsedHW[index]['dueM']"
                          suffix="/"
                        ></v-text-field>
                      </v-col>
                      <v-col class="pa-0">
                        <v-text-field
                          class="mr-3"
                          v-model="parsedHW[index]['dueD']"
                        ></v-text-field>
                      </v-col>
                      <v-col class="pa-0">
                        <v-text-field
                          class="mr-3"
                          v-model="parsedHW[index]['dueh']"
                          suffix=":"
                        ></v-text-field>
                      </v-col>
                      <v-col class="pa-0">
                        <v-text-field
                          class=""
                          v-model="parsedHW[index]['duem']"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-list-item-content>
              </v-list-item>
              <v-list-item :key="index + '4'">
                <v-btn
                  dark
                  class="ma-1"
                  v-on:click="parsedHW.splice(index, 1)"
                  color="red darken-4"
                  >Delete</v-btn
                >
              </v-list-item>
              <v-divider
                v-if="index + 1 < parsedHW.length"
                :key="item.homeworkName + 'divider'"
              ></v-divider>
            </template>
          </v-list>
        </v-card>

        <v-card class="ma-3" v-if="inputState == 2">
          <v-list outlined>
            <template v-for="(item, index) in parsedHW">
              <v-list-item :key="index+'1'">
                <v-list-item-content>
                  <v-list-item-title>Class Name:</v-list-item-title>
                </v-list-item-content>
                <v-list-item-content>
                  <v-text-field
                    v-model="parsedHW[index]['className']"
                  ></v-text-field>
                </v-list-item-content>
              </v-list-item>
              <v-list-item :key="index+'2'">
                <v-list-item-content>
                  <v-list-item-title>Homework Name:</v-list-item-title>
                </v-list-item-content>
                <v-list-item-content>
                  <v-text-field
                    v-model="parsedHW[index]['homeworkName']"
                  ></v-text-field>
                </v-list-item-content>
              </v-list-item>

              <v-list-item :key="index + '3'">
                <v-list-item-content>
                  <v-list-item-title>Due Date:</v-list-item-title>
                </v-list-item-content>
                <v-list-item-content>
                  <br />
                  <v-container>
                    <v-row>
                      <v-col class="pa-0">
                        <v-text-field
                          class="mr-3"
                          v-model="parsedHW[index]['dueM']"
                          suffix="/"
                        ></v-text-field>
                      </v-col>
                      <v-col class="pa-0">
                        <v-text-field
                          class="mr-3"
                          v-model="parsedHW[index]['dueD']"
                        ></v-text-field>
                      </v-col>
                      <v-col class="pa-0">
                        <v-text-field
                          class="mr-3"
                          v-model="parsedHW[index]['dueh']"
                          suffix=":"
                        ></v-text-field>
                      </v-col>
                      <v-col class="pa-0">
                        <v-text-field
                          class=""
                          v-model="parsedHW[index]['duem']"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-list-item-content>
              </v-list-item>
              <v-list-item :key="index + '4'">
                <v-btn
                  dark
                  class="ma-1"
                  v-on:click="parsedHW.splice(index, 1)"
                  color="red darken-4"
                  >Delete</v-btn
                >
              </v-list-item>
              <v-divider
                v-if="index + 1 < parsedHW.length"
                :key="item.homeworkName + 'divider'"
              ></v-divider>
            </template>
          </v-list>
        </v-card>

        <v-data-table :items="HWList" :headers="headers">
          <template v-slot:item.status="{ item }">
            <v-btn text small @click="markAsDone(item)">
              <v-icon class="mr-2" small>mdi-check</v-icon>Mark As Done
            </v-btn>
          </template>
          <template v-slot:item.dueDate="{ item }">
            <span
              >{{ item["dueM"] }}/{{ item["dueD"] }} {{ item["dueh"] }}:{{
                item["duem"]
              }}
              {{ getWeekday(item) }}</span
            >
          </template>
        </v-data-table>
        <v-btn
          v-if="inputState < 2"
          class="ma-1"
          v-on:click="doShowDoneHW()"
          color="primary"
          >{{
            showDoneHomeworks
              ? "Hide Completed Homeworks"
              : "Show Completed Homeworks"
          }}</v-btn
        >
        <v-data-table
          v-if="showDoneHomeworks"
          :items="HWCompletedList"
          :headers="cHeaders"
        >
          <template v-slot:item.status="{ item }">
            <v-icon small>mdi-check</v-icon>Completed
            <v-btn text small @click="deleteTask(item)">
              <v-icon class="mr-2" small>mdi-delete</v-icon>Delete
            </v-btn>
            <v-btn text small @click="markAsUndone(item)">
              <v-icon class="mr-2" small>mdi-delete</v-icon>Undone
            </v-btn>
          </template>
          <template v-slot:item.dueDate="{ item }">
            <span
              >{{ item["dueM"] }}/{{ item["dueD"] }} {{ item["dueh"] }}:{{
                item["duem"]
              }}</span
            >
          </template>
        </v-data-table>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
//import HelloWorld from "./components/HelloWorld";

export default {
  name: "App",

  components: {},

  data: function () {
    return {
      showDoneHomeworks: false,
      inputState: 0,
      parsedHW: {}, //null,
      txtToParse: "",
      HWList: [],
      HWCompletedList: [
        {
          className: "",
          dueD: "",
          dueM: "",
          dueh: "",
          duem: "",
          homeworkName: "",
        },
      ],
      headers: [
        { text: "Class Name", value: "className" },
        { text: "Homework Name", value: "homeworkName" },
        { text: "Due Date", value: "dueDate" },
        { text: "Change Status", value: "status" },
      ],
      cHeaders: [
        { text: "Class Name", value: "className" },
        { text: "Homework Name", value: "homeworkName" },
        { text: "Due Date", value: "dueDate" },
        { text: "Status", value: "status" },
      ],
    };
  },
  mounted: function () {
    this.loadHWList();
  },
  methods: {
    fullName(salut) {
      return `${salut}`;
    },
    getWeekday(item) {
      var d = new Date();
      var y = d.getFullYear();
      if (Number(item["dueM"]) < 3 && d.getMonth() > 10) {
        y++;
      }
      var dateToGetWeekday = new Date(
        y + "/" + item["dueM"] + "/" + item["dueD"]
      );
      var weekdays = new Array("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat");
      return (
        weekdays[dateToGetWeekday.getDay()] +
        " (" +
        Math.floor(
          (dateToGetWeekday.getTime() - new Date().getTime()) / 86400000 + 1
        ) +
        " Days Left)"
      );
    },
    doShowDoneHW: function () {
      this.showDoneHomeworks = !this.showDoneHomeworks;
      this.$axios
        .get("./api/hwDoneList")
        .then((response) => (this.HWCompletedList = response.data.hwl));
    },
    markAsDone: function (item) {
      this.$axios
        .get("./api/markAsDone", {
          params: {
            nameOfTask: item["homeworkName"],
          },
        })
        .then((response) => (this.HWList = response.data.hwl));
      this.$nextTick(function () {
        this.loadHWList();
        this.$axios
          .get("./api/hwDoneList")
          .then((response) => (this.HWCompletedList = response.data.hwl));
      });
    },
    markAsUndone: function (item) {
      this.$axios
        .get("./api/markAsUndone", {
          params: {
            nameOfTask: item["homeworkName"],
          },
        })
        .then((response) => (this.HWList = response.data.hwl));
      this.$nextTick(function () {
        this.loadHWList();
        this.$axios
          .get("./api/hwDoneList")
          .then((response) => (this.HWCompletedList = response.data.hwl));
      });
    },
    deleteTask: function (item) {
      this.$axios
        .get("./api/delete", {
          params: {
            nameOfTask: item["homeworkName"],
          },
        })
        .then((response) => (this.HWList = response.data.hwl));
      this.$nextTick(function () {
        this.loadHWList();
        this.$axios
          .get("./api/hwDoneList")
          .then((response) => (this.HWCompletedList = response.data.hwl));
      });
    },
    loadHWList: function () {
      this.$axios
        .get("./api/hwlist")
        .then(
          (this.headers = [
            { text: "Class Name", value: "className" },
            { text: "Homework Name", value: "homeworkName" },
            { text: "Due Date", value: "dueDate" },
            { text: "Change Status", value: "status" },
          ])
        )
        .then((response) => (this.HWList = response.data.hwl));
    },
    showParseTxtF: function () {
      this.inputState = this.inputState == 1 ? 0 : 1;
    },
    manualInput: function () {
      this.inputState = this.inputState == 2 ? 0 : 2;
      this.parsedHW = [
        {
          className: "",
          dueD: "",
          dueM: "",
          dueh: "",
          duem: "",
          homeworkName: "",
        },
      ];
    },
    parse: function () {
      this.$axios
        .get("./api/parse", {
          params: {
            parseTxt: this.txtToParse,
          },
        })
        .then((response) => (this.parsedHW = response.data.parsedHomeworks))
        .then((this.inputState = 3));
    },
    submit: function () {
      console.log("parsedHW" + JSON.stringify(this.parsedHW));
      this.$axios
        .get("./api/addnew", {
          params: {
            hws: JSON.stringify({ hwl: this.parsedHW }),
          },
        })
        .then((response) => (this.HWList = response.data.hwl));

      this.inputState = 0;

      this.$nextTick(function () {
        this.loadHWList();
      });
    },
  },
};
</script>