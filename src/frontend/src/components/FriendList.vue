<template>
    <div>
        <div class="row">
            <div class="col">
                <base-alert type="success" v-show="success">
          <span class="alert-inner--icon" margin-right="10px">
            <i class="ni ni-bell-55"></i>
          </span>
                    <span class="alert-inner--text">
            <strong>已成功邀请!</strong> 请等待好友同意!
          </span>
                    <button
                            @click="success=false"
                            aria-label="Close"
                            class="close"
                            data-dismiss="alert"
                            type="button"
                    >
                        <span aria-hidden="true">&times;</span>
                    </button>
                </base-alert>
            </div>
        </div>
        <div class="friend-list">
            <div class="row align-items-center">
                <div class="col-10">
                    <div class="avatar-group">
                        <a
                                :data-original-title="friend.user_name"
                                :key="index"
                                class="avatar avatar-sm rounded-circle"
                                data-toggle="tooltip"
                                href="#"
                                v-for="(friend, index) in travel.company_list"
                        >
                            <img :src="friend.avatar_url" alt="Image placeholder">
                        </a>
                        <small>{{hasCompany()?"":"还没有同伴哦，快快邀请吧！"}}</small>
                    </div>
                </div>
                <div class="col-2 text-right">
                    <base-button
                            @click="showList = !showList"
                            size="sm"
                            type="primary"
                            v-show="hasFriend()"
                    >{{showList?"完成": "管理同行"}}
                    </base-button>
                </div>
            </div>

            <div
                    :key="index"
                    class="row align-items-center"
                    v-for="(friend,index) in friend_info_list"
                    v-show="showList"
            >
                <div class="col-1">
                    <a
                            :data-original-title="friend.user_name"
                            class="avatar avatar-sm rounded-circle"
                            data-toggle="tooltip"
                            href="#"
                    >
                        <img :src="friend.avatar_url" alt="Image placeholder">
                    </a>
                </div>
                <div class="col-9 text-left">{{friend.user_name}}</div>
                <div class="col-2 text-right">
                    <base-button
                            @click="isCompany(friend)?del(friend):invite(friend)"
                            size="sm"
                            type="primary"
                    >{{isCompany(friend)?"移除":"邀请"}}
                    </base-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "friend-list",
        props: {
            travel: Object,
            friend_info_list: Array
        },
        data() {
            return {
                showList: false,
                success: false
            };
        },

        methods: {
            isCompany: function (friend) {
                var start = false;
                this.travel.company_list.forEach(company => {
                    if (company.user_id == friend.user_id) {
                        start = true;
                    }
                });
                return start;
            },
            hasCompany: function () {
                return this.travel.company_list.length != 0;
            },
            hasFriend: function () {
                return this.friend_info_list.length != 0;
            },
            del(friend) {
                var vue = this;
                this.$backend_conn(
                    "remove_travel_company",
                    {
                        travel_id: vue.travel.travel_id,
                        friend_user_id: friend.user_id
                    },
                    vue,
                    function (response) {
                        for (var i = 0; i < vue.travel.company_list.length; ++i) {
                            if (vue.travel.company_list[i].user_id == friend.user_id) {
                                vue.travel.company_list.splice(i, 1);
                            }
                        }
                        console.log(response);
                    },
                    function (response) {
                        alert(response.data.error_message);
                    }
                );
            },

            invite(friend) {
                var vue = this;

                this.$backend_conn(
                    "invite_travel_company",
                    {
                        travel_id: vue.travel.travel_id,
                        friend_user_id: friend.user_id
                    },
                    vue,
                    function (response) {
                        vue.success = true;
                        setTimeout(function () {
                            vue.success = false;
                        }, 2000);
                        console.log(response);
                    },
                    function (response) {
                        alert(response.data.error_message);
                    }
                );
            }
        }
    };
</script>
<style scoped>
    .friend-list {
        max-height: 200px;
        overflow-y: auto;
        overflow-x: hidden;
    }
</style>

