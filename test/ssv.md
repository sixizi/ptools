### 5.1.6 服务器状态变量

服务器维护很多提供自身运行信息的状态变量。你可以使用`SHOW [GLOBAL | SESSION ] STATUS`语句（参考[每13.7.5.36小节，SHOW STATUS语法][SHOW_STATUS]）来查看这些变量和它们的值。选项`GLOBAL`关键词汇总了所有连接的值，而`SESSION`显示当前连接的值。

    mysql> SHOW GLOBAL STATUS;
    +-----------------------------------+------------+
    | Variable_name                     | Value      |
    +-----------------------------------+------------+
    | Aborted_clients                   | 0          |
    | Aborted_connects                  | 0          |
    | Bytes_received                    | 155372598  |
    | Bytes_sent                        | 1176560426 |
    ...
    | Connections                       | 30023      |
    | Created_tmp_disk_tables           | 0          |
    | Created_tmp_files                 | 3          |
    | Created_tmp_tables                | 2          |
    ...
    | Threads_created                   | 217        |
    | Threads_running                   | 88         |
    | Uptime                            | 1389872    |
    +-----------------------------------+------------+

很多变量会被[FLUSH STATUS][FLUSH_STATUS]重置为0。

下表列出所有可用的服务器状态变量：

表5.5 系统变量概要

变量名 | 变量类型 | 变量范围
-------|-------|:-------:
[Aborted_clients](#statvar_Aborted_clients) | numeric | `GLOBAL`
[Aborted_connects](#statvar_Aborted_connects) | numeric | `GLOBAL`
[Binlog_cache_disk_use](#statvar_Binlog_cache_disk_use) | numeric | `GLOBAL`
[Binlog_cache_use](#statvar_Binlog_cache_use) | numeric | `GLOBAL`
[Binlog_stmt_cache_disk_use](#statvar_Binlog_stmt_cache_disk_use) | numeric | `GLOBAL`
[Binlog_stmt_cache_use](#statvar_Binlog_stmt_cache_use) | numeric | `GLOBAL`
[Bytes_received](#statvar_Bytes_received) | numeric | `GLOBAL ` | ` SESSION`
[Bytes_sent](#statvar_Bytes_sent) | numeric | `GLOBAL ` | ` SESSION`
[Com_admin_commands](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_alter_db](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_alter_db_upgrade](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_alter_event](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_alter_function](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_alter_procedure](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_alter_server](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_alter_table](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_alter_tablespace](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_alter_user](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_analyze](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_assign_to_keycache](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_begin](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_binlog](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_call_procedure](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_change_db](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_change_master](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_check](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_checksum](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_commit](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_db](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_event](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_function](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_index](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_procedure](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_server](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_table](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_trigger](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_udf](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_user](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_create_view](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_dealloc_sql](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_delete](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_delete_multi](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_do](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_drop_db](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_drop_event](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_drop_function](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_drop_index](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_drop_procedure](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_drop_server](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_drop_table](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_drop_trigger](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_drop_user](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_drop_view](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_empty_query](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_execute_sql](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_flush](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_get_diagnostics](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_grant](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_ha_close](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_ha_open](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_ha_read](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_help](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_insert](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_insert_select](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_install_plugin](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_kill](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_load](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_lock_tables](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_optimize](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_preload_keys](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_prepare_sql](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_purge](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_purge_before_date](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_release_savepoint](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_rename_table](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_rename_user](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_repair](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_replace](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_replace_select](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_reset](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_resignal](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_revoke](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_revoke_all](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_rollback](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_rollback_to_savepoint](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_savepoint](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_select](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_set_option](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_authors](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_binlog_events](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_binlogs](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_charsets](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_collations](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_contributors](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_create_db](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_create_event](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_create_func](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_create_proc](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_create_table](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_create_trigger](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_databases](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_engine_logs](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_engine_mutex](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_engine_status](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_errors](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_events](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_fields](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_function_code](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_function_status](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_grants](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_keys](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_master_status](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_ndb_status](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_new_master](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_open_tables](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_plugins](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_privileges](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_procedure_code](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_procedure_status](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_processlist](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_profile](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_profiles](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_relaylog_events](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_slave_hosts](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_slave_status](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_status](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_storage_engines](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_table_status](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_tables](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_triggers](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_variables](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_show_warnings](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_signal](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_slave_start](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_slave_stop](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_stmt_close](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_stmt_execute](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_stmt_fetch](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_stmt_prepare](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_stmt_reprepare](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_stmt_reset](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_stmt_send_long_data](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_truncate](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_uninstall_plugin](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_unlock_tables](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_update](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_update_multi](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_xa_commit](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_xa_end](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_xa_prepare](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_xa_recover](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_xa_rollback](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Com_xa_start](#statvar_Com_xxx) | numeric | `GLOBAL ` | ` SESSION`
[Compression](#statvar_Compression) | numeric | `SESSION`
[Connection_errors_accept](#statvar_Connection_errors_accept) | numeric | `GLOBAL`
[Connection_errors_internal](#statvar_Connection_errors_internal) | numeric | `GLOBAL`
[Connection_errors_max_connections](#statvar_Connection_errors_max_connections) | numeric | `GLOBAL`
[Connection_errors_peer_addr](#statvar_Connection_errors_peer_addr) | numeric | `GLOBAL`
[Connection_errors_select](#statvar_Connection_errors_select) | numeric | `GLOBAL`
[Connection_errors_tcpwrap](#statvar_Connection_errors_tcpwrap) | numeric | `GLOBAL`
[Connections](#statvar_Connections) | numeric | `GLOBAL`
[Created_tmp_disk_tables](#statvar_Created_tmp_disk_tables) | numeric | `GLOBAL ` | ` SESSION`
[Created_tmp_files](#statvar_Created_tmp_files) | numeric | `GLOBAL`
[Created_tmp_tables](#statvar_Created_tmp_tables) | numeric | `GLOBAL ` | ` SESSION`
[Delayed_errors](#statvar_Delayed_errors) | numeric | `GLOBAL`
[Delayed_insert_threads](#statvar_Delayed_insert_threads) | numeric | `GLOBAL`
[Delayed_writes](#statvar_Delayed_writes) | numeric | `GLOBAL`
[Flush_commands](#statvar_Flush_commands) | numeric | `GLOBAL`
[Handler_commit](#statvar_Handler_commit) | numeric | `GLOBAL ` | ` SESSION`
[Handler_delete](#statvar_Handler_delete) | numeric | `GLOBAL ` | ` SESSION`
[Handler_discover](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Handler_discover) | numeric | `GLOBAL ` | ` SESSION`
[Handler_external_lock](#statvar_Handler_external_lock) | numeric | `GLOBAL ` | ` SESSION`
[Handler_mrr_init](#statvar_Handler_mrr_init) | numeric | `GLOBAL ` | ` SESSION`
[Handler_prepare](#statvar_Handler_prepare) | numeric | `GLOBAL ` | ` SESSION`
[Handler_read_first](#statvar_Handler_read_first) | numeric | `GLOBAL ` | ` SESSION`
[Handler_read_key](#statvar_Handler_read_key) | numeric | `GLOBAL ` | ` SESSION`
[Handler_read_last](#statvar_Handler_read_last) | numeric | `GLOBAL ` | ` SESSION`
[Handler_read_next](#statvar_Handler_read_next) | numeric | `GLOBAL ` | ` SESSION`
[Handler_read_prev](#statvar_Handler_read_prev) | numeric | `GLOBAL ` | ` SESSION`
[Handler_read_rnd](#statvar_Handler_read_rnd) | numeric | `GLOBAL ` | ` SESSION`
[Handler_read_rnd_next](#statvar_Handler_read_rnd_next) | numeric | `GLOBAL ` | ` SESSION`
[Handler_rollback](#statvar_Handler_rollback) | numeric | `GLOBAL ` | ` SESSION`
[Handler_savepoint](#statvar_Handler_savepoint) | numeric | `GLOBAL ` | ` SESSION`
[Handler_savepoint_rollback](#statvar_Handler_savepoint_rollback) | numeric | `GLOBAL ` | ` SESSION`
[Handler_update](#statvar_Handler_update) | numeric | `GLOBAL ` | ` SESSION`
[Handler_write](#statvar_Handler_write) | numeric | `GLOBAL ` | ` SESSION`
[Innodb_available_undo_logs](#statvar_Innodb_available_undo_logs) | numeric | `GLOBAL`
[Innodb_buffer_pool_bytes_data](#statvar_Innodb_buffer_pool_bytes_data) | numeric | `GLOBAL`
[Innodb_buffer_pool_bytes_dirty](#statvar_Innodb_buffer_pool_bytes_dirty) | numeric | `GLOBAL`
[Innodb_buffer_pool_dump_status](#statvar_Innodb_buffer_pool_dump_status) | numeric | `GLOBAL`
[Innodb_buffer_pool_load_status](#statvar_Innodb_buffer_pool_load_status) | numeric | `GLOBAL`
[Innodb_buffer_pool_pages_data](#statvar_Innodb_buffer_pool_pages_data) | numeric | `GLOBAL`
[Innodb_buffer_pool_pages_dirty](#statvar_Innodb_buffer_pool_pages_dirty) | numeric | `GLOBAL`
[Innodb_buffer_pool_pages_flushed](#statvar_Innodb_buffer_pool_pages_flushed) | numeric | `GLOBAL`
[Innodb_buffer_pool_pages_free](#statvar_Innodb_buffer_pool_pages_free) | numeric | `GLOBAL`
[Innodb_buffer_pool_pages_latched](#statvar_Innodb_buffer_pool_pages_latched) | numeric | `GLOBAL`
[Innodb_buffer_pool_pages_misc](#statvar_Innodb_buffer_pool_pages_misc) | numeric | `GLOBAL`
[Innodb_buffer_pool_pages_total](#statvar_Innodb_buffer_pool_pages_total) | numeric | `GLOBAL`
[Innodb_buffer_pool_read_ahead](#statvar_Innodb_buffer_pool_read_ahead) | numeric | `GLOBAL`
[Innodb_buffer_pool_read_ahead_evicted](#statvar_Innodb_buffer_pool_read_ahead_evicted) | numeric | `GLOBAL`
[Innodb_buffer_pool_read_requests](#statvar_Innodb_buffer_pool_read_requests) | numeric | `GLOBAL`
[Innodb_buffer_pool_reads](#statvar_Innodb_buffer_pool_reads) | numeric | `GLOBAL`
[Innodb_buffer_pool_wait_free](#statvar_Innodb_buffer_pool_wait_free) | numeric | `GLOBAL`
[Innodb_buffer_pool_write_requests](#statvar_Innodb_buffer_pool_write_requests) | numeric | `GLOBAL`
[Innodb_data_fsyncs](#statvar_Innodb_data_fsyncs) | numeric | `GLOBAL`
[Innodb_data_pending_fsyncs](#statvar_Innodb_data_pending_fsyncs) | numeric | `GLOBAL`
[Innodb_data_pending_reads](#statvar_Innodb_data_pending_reads) | numeric | `GLOBAL`
[Innodb_data_pending_writes](#statvar_Innodb_data_pending_writes) | numeric | `GLOBAL`
[Innodb_data_read](#statvar_Innodb_data_read) | numeric | `GLOBAL`
[Innodb_data_reads](#statvar_Innodb_data_reads) | numeric | `GLOBAL`
[Innodb_data_writes](#statvar_Innodb_data_writes) | numeric | `GLOBAL`
[Innodb_data_written](#statvar_Innodb_data_written) | numeric | `GLOBAL`
[Innodb_dblwr_pages_written](#statvar_Innodb_dblwr_pages_written) | numeric | `GLOBAL`
[Innodb_dblwr_writes](#statvar_Innodb_dblwr_writes) | numeric | `GLOBAL`
[Innodb_have_atomic_builtins](#statvar_Innodb_have_atomic_builtins) | numeric | `GLOBAL`
[Innodb_log_waits](#statvar_Innodb_log_waits) | numeric | `GLOBAL`
[Innodb_log_write_requests](#statvar_Innodb_log_write_requests) | numeric | `GLOBAL`
[Innodb_log_writes](#statvar_Innodb_log_writes) | numeric | `GLOBAL`
[Innodb_num_open_files](#statvar_Innodb_num_open_files) | numeric | `GLOBAL`
[Innodb_os_log_fsyncs](#statvar_Innodb_os_log_fsyncs) | numeric | `GLOBAL`
[Innodb_os_log_pending_fsyncs](#statvar_Innodb_os_log_pending_fsyncs) | numeric | `GLOBAL`
[Innodb_os_log_pending_writes](#statvar_Innodb_os_log_pending_writes) | numeric | `GLOBAL`
[Innodb_os_log_written](#statvar_Innodb_os_log_written) | numeric | `GLOBAL`
[Innodb_page_size](#statvar_Innodb_page_size) | numeric | `GLOBAL`
[Innodb_pages_created](#statvar_Innodb_pages_created) | numeric | `GLOBAL`
[Innodb_pages_read](#statvar_Innodb_pages_read) | numeric | `GLOBAL`
[Innodb_pages_written](#statvar_Innodb_pages_written) | numeric | `GLOBAL`
[Innodb_row_lock_current_waits](#statvar_Innodb_row_lock_current_waits) | numeric | `GLOBAL`
[Innodb_row_lock_time](#statvar_Innodb_row_lock_time) | numeric | `GLOBAL`
[Innodb_row_lock_time_avg](#statvar_Innodb_row_lock_time_avg) | numeric | `GLOBAL`
[Innodb_row_lock_time_max](#statvar_Innodb_row_lock_time_max) | numeric | `GLOBAL`
[Innodb_row_lock_waits](#statvar_Innodb_row_lock_waits) | numeric | `GLOBAL`
[Innodb_rows_deleted](#statvar_Innodb_rows_deleted) | numeric | `GLOBAL`
[Innodb_rows_inserted](#statvar_Innodb_rows_inserted) | numeric | `GLOBAL`
[Innodb_rows_read](#statvar_Innodb_rows_read) | numeric | `GLOBAL`
[Innodb_rows_updated](#statvar_Innodb_rows_updated) | numeric | `GLOBAL`
[Innodb_truncated_status_writes](#statvar_Innodb_truncated_status_writes) | numeric | `GLOBAL`
[Key_blocks_not_flushed](#statvar_Key_blocks_not_flushed) | numeric | `GLOBAL`
[Key_blocks_unused](#statvar_Key_blocks_unused) | numeric | `GLOBAL`
[Key_blocks_used](#statvar_Key_blocks_used) | numeric | `GLOBAL`
[Key_read_requests](#statvar_Key_read_requests) | numeric | `GLOBAL`
[Key_reads](#statvar_Key_reads) | numeric | `GLOBAL`
[Key_write_requests](#statvar_Key_write_requests) | numeric | `GLOBAL`
[Key_writes](#statvar_Key_writes) | numeric | `GLOBAL`
[Last_query_cost](#statvar_Last_query_cost) | numeric | `SESSION`
[Last_query_partial_plans](#statvar_Last_query_partial_plans) | numeric | `SESSION`
[Max_used_connections](#statvar_Max_used_connections) | numeric | `GLOBAL`
[Ndb_api_bytes_received_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_bytes_received_count) | numeric | `GLOBAL`
[Ndb_api_bytes_received_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_bytes_received_count_session) | numeric | `SESSION`
[Ndb_api_bytes_received_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_bytes_received_count_slave) | numeric | `GLOBAL`
[Ndb_api_bytes_sent_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_bytes_sent_count) | numeric | `GLOBAL`
[Ndb_api_bytes_sent_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_bytes_sent_count_session) | numeric | `SESSION`
[Ndb_api_bytes_sent_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_bytes_sent_count_slave) | numeric | `GLOBAL`
[Ndb_api_event_bytes_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_event_bytes_count) | numeric | `GLOBAL`
[Ndb_api_event_bytes_count_injector](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_event_bytes_count_injector) | numeric | `GLOBAL`
[Ndb_api_event_data_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_event_data_count) | numeric | `GLOBAL`
[Ndb_api_event_data_count_injector](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_event_data_count_injector) | numeric | `GLOBAL`
[Ndb_api_event_nondata_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_event_nondata_count) | numeric | `GLOBAL`
[Ndb_api_event_nondata_count_injector](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_event_nondata_count_injector) | numeric | `GLOBAL`
[Ndb_api_pk_op_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_pk_op_count) | numeric | `GLOBAL`
[Ndb_api_pk_op_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_pk_op_count_session) | numeric | `SESSION`
[Ndb_api_pk_op_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_pk_op_count_slave) | numeric | `GLOBAL`
[Ndb_api_pruned_scan_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_pruned_scan_count) | numeric | `GLOBAL`
[Ndb_api_pruned_scan_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_pruned_scan_count_session) | numeric | `SESSION`
[Ndb_api_pruned_scan_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_pruned_scan_count_slave) | numeric | `GLOBAL`
[Ndb_api_range_scan_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_range_scan_count) | numeric | `GLOBAL`
[Ndb_api_range_scan_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_range_scan_count_session) | numeric | `SESSION`
[Ndb_api_range_scan_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_range_scan_count_slave) | numeric | `GLOBAL`
[Ndb_api_read_row_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_read_row_count) | numeric | `GLOBAL`
[Ndb_api_read_row_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_read_row_count_session) | numeric | `SESSION`
[Ndb_api_read_row_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_read_row_count_slave) | numeric | `GLOBAL`
[Ndb_api_scan_batch_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_scan_batch_count) | numeric | `GLOBAL`
[Ndb_api_scan_batch_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_scan_batch_count_session) | numeric | `SESSION`
[Ndb_api_scan_batch_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_scan_batch_count_slave) | numeric | `GLOBAL`
[Ndb_api_table_scan_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_table_scan_count) | numeric | `GLOBAL`
[Ndb_api_table_scan_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_table_scan_count_session) | numeric | `SESSION`
[Ndb_api_table_scan_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_table_scan_count_slave) | numeric | `GLOBAL`
[Ndb_api_trans_abort_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_abort_count) | numeric | `GLOBAL`
[Ndb_api_trans_abort_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_abort_count_session) | numeric | `SESSION`
[Ndb_api_trans_abort_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_abort_count_slave) | numeric | `GLOBAL`
[Ndb_api_trans_close_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_close_count) | numeric | `GLOBAL`
[Ndb_api_trans_close_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_close_count_session) | numeric | `SESSION`
[Ndb_api_trans_close_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_close_count_slave) | numeric | `GLOBAL`
[Ndb_api_trans_commit_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_commit_count) | numeric | `GLOBAL`
[Ndb_api_trans_commit_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_commit_count_session) | numeric | `SESSION`
[Ndb_api_trans_commit_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_commit_count_slave) | numeric | `GLOBAL`
[Ndb_api_trans_local_read_row_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_local_read_row_count) | numeric | `GLOBAL`
[Ndb_api_trans_local_read_row_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_local_read_row_count_session) | numeric | `SESSION`
[Ndb_api_trans_local_read_row_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_local_read_row_count_slave) | numeric | `GLOBAL`
[Ndb_api_trans_start_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_start_count) | numeric | `GLOBAL`
[Ndb_api_trans_start_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_start_count_session) | numeric | `SESSION`
[Ndb_api_trans_start_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_trans_start_count_slave) | numeric | `GLOBAL`
[Ndb_api_uk_op_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_uk_op_count) | numeric | `GLOBAL`
[Ndb_api_uk_op_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_uk_op_count_session) | numeric | `SESSION`
[Ndb_api_uk_op_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_uk_op_count_slave) | numeric | `GLOBAL`
[Ndb_api_wait_exec_complete_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_exec_complete_count) | numeric | `GLOBAL`
[Ndb_api_wait_exec_complete_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_exec_complete_count_session) | numeric | `SESSION`
[Ndb_api_wait_exec_complete_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_exec_complete_count_slave) | numeric | `GLOBAL`
[Ndb_api_wait_meta_request_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_meta_request_count) | numeric | `GLOBAL`
[Ndb_api_wait_meta_request_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_meta_request_count_session) | numeric | `SESSION`
[Ndb_api_wait_meta_request_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_meta_request_count_slave) | numeric | `GLOBAL`
[Ndb_api_wait_nanos_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_nanos_count) | numeric | `GLOBAL`
[Ndb_api_wait_nanos_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_nanos_count_session) | numeric | `SESSION`
[Ndb_api_wait_nanos_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_nanos_count_slave) | numeric | `GLOBAL`
[Ndb_api_wait_scan_result_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_scan_result_count) | numeric | `GLOBAL`
[Ndb_api_wait_scan_result_count_session](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_scan_result_count_session) | numeric | `SESSION`
[Ndb_api_wait_scan_result_count_slave](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_api_wait_scan_result_count_slave) | numeric | `GLOBAL`
[ndb_cluster_connection_pool](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#option_mysqld_ndb-cluster-connection-pool) | numeric | `GLOBAL`
[Ndb_cluster_node_id](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_cluster_node_id) | numeric | `GLOBAL ` | ` SESSION`
[Ndb_config_from_host](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_config_from_host) | numeric | `GLOBAL ` | ` SESSION`
[Ndb_config_from_port](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_config_from_port) | numeric | `GLOBAL ` | ` SESSION`
[Ndb_conflict_fn_epoch](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_conflict_fn_epoch) | numeric | `GLOBAL`
[Ndb_conflict_fn_epoch_trans](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_conflict_fn_epoch_trans) | numeric | `GLOBAL`
[Ndb_conflict_fn_max](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_conflict_fn_max) | numeric | `GLOBAL`
[Ndb_conflict_fn_old](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_conflict_fn_old) | numeric | `GLOBAL`
[Ndb_conflict_trans_conflict_commit_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_conflict_trans_conflict_commit_count) | numeric | `GLOBAL`
[Ndb_conflict_trans_detect_iter_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_conflict_trans_detect_iter_count) | numeric | `GLOBAL`
[Ndb_conflict_trans_reject_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_conflict_trans_reject_count) | numeric | `GLOBAL`
[Ndb_conflict_trans_row_conflict_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_conflict_trans_row_conflict_count) | numeric | `GLOBAL`
[Ndb_conflict_trans_row_reject_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_conflict_trans_row_reject_count) | numeric | `GLOBAL`
[ndb_execute_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_execute_count) | numeric | `GLOBAL`
[ndb-nodeid](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#option_mysqld_ndb-nodeid) | numeric | `GLOBAL`
[Ndb_number_of_data_nodes](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_number_of_data_nodes) | numeric | `GLOBAL`
[ndb_pruned_scan_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_pruned_scan_count) | numeric | `GLOBAL`
[Ndb_pushed_queries_defined](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_pushed_queries_defined) | numeric | `GLOBAL`
[Ndb_pushed_queries_dropped](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_pushed_queries_dropped) | numeric | `GLOBAL`
[Ndb_pushed_queries_executed](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_pushed_queries_executed) | numeric | `GLOBAL`
[ndb_pushed_reads](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_pushed_reads) | numeric | `GLOBAL`
[ndb_scan_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#statvar_Ndb_scan_count) | numeric | `GLOBAL`
[Not_flushed_delayed_rows](#statvar_Not_flushed_delayed_rows) | numeric | `GLOBAL`
[Open_files](#statvar_Open_files) | numeric | `GLOBAL`
[Open_streams](#statvar_Open_streams) | numeric | `GLOBAL`
[Open_table_definitions](#statvar_Open_table_definitions) | numeric | `GLOBAL`
[Open_tables](#statvar_Open_tables) | numeric | `GLOBAL ` | ` SESSION`
[Opened_files](#statvar_Opened_files) | numeric | `GLOBAL`
[Opened_table_definitions](#statvar_Opened_table_definitions) | numeric | `GLOBAL ` | ` SESSION`
[Opened_tables](#statvar_Opened_tables) | numeric | `GLOBAL ` | ` SESSION`
[Performance_schema_accounts_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_accounts_lost) | numeric | `GLOBAL`
[Performance_schema_cond_classes_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_cond_classes_lost) | numeric | `GLOBAL`
[Performance_schema_cond_instances_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_cond_instances_lost) | numeric | `GLOBAL`
[Performance_schema_file_classes_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_file_classes_lost) | numeric | `GLOBAL`
[Performance_schema_file_handles_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_file_handles_lost) | numeric | `GLOBAL`
[Performance_schema_file_instances_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_file_instances_lost) | numeric | `GLOBAL`
[Performance_schema_hosts_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_hosts_lost) | numeric | `GLOBAL`
[Performance_schema_locker_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_locker_lost) | numeric | `GLOBAL`
[Performance_schema_mutex_classes_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_mutex_classes_lost) | numeric | `GLOBAL`
[Performance_schema_mutex_instances_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_mutex_instances_lost) | numeric | `GLOBAL`
[Performance_schema_rwlock_classes_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_rwlock_classes_lost) | numeric | `GLOBAL`
[Performance_schema_rwlock_instances_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_rwlock_instances_lost) | numeric | `GLOBAL`
[Performance_schema_session_connect_attrs_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_session_connect_attrs_lost) | numeric | `GLOBAL`
[Performance_schema_socket_classes_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_socket_classes_lost) | numeric | `GLOBAL`
[Performance_schema_socket_instances_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_socket_instances_lost) | numeric | `GLOBAL`
[Performance_schema_stage_classes_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_stage_classes_lost) | numeric | `GLOBAL`
[Performance_schema_statement_classes_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_statement_classes_lost) | numeric | `GLOBAL`
[Performance_schema_table_handles_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_table_handles_lost) | numeric | `GLOBAL`
[Performance_schema_table_instances_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_table_instances_lost) | numeric | `GLOBAL`
[Performance_schema_thread_classes_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_thread_classes_lost) | numeric | `GLOBAL`
[Performance_schema_thread_instances_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_thread_instances_lost) | numeric | `GLOBAL`
[Performance_schema_users_lost](../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md#statvar_Performance_schema_users_lost) | numeric | `GLOBAL`
[Prepared_stmt_count](#statvar_Prepared_stmt_count) | numeric | `GLOBAL`
[Qcache_free_blocks](#statvar_Qcache_free_blocks) | numeric | `GLOBAL`
[Qcache_free_memory](#statvar_Qcache_free_memory) | numeric | `GLOBAL`
[Qcache_hits](#statvar_Qcache_hits) | numeric | `GLOBAL`
[Qcache_inserts](#statvar_Qcache_inserts) | numeric | `GLOBAL`
[Qcache_lowmem_prunes](#statvar_Qcache_lowmem_prunes) | numeric | `GLOBAL`
[Qcache_not_cached](#statvar_Qcache_not_cached) | numeric | `GLOBAL`
[Qcache_queries_in_cache](#statvar_Qcache_queries_in_cache) | numeric | `GLOBAL`
[Qcache_total_blocks](#statvar_Qcache_total_blocks) | numeric | `GLOBAL`
[Queries](#statvar_Queries) | numeric | `GLOBAL ` | ` SESSION`
[Questions](#statvar_Questions) | numeric | `GLOBAL ` | ` SESSION`
[Rpl_semi_sync_master_clients](#statvar_Rpl_semi_sync_master_clients) | numeric | `GLOBAL`
[Rpl_semi_sync_master_net_avg_wait_time](#statvar_Rpl_semi_sync_master_net_avg_wait_time) | numeric | `GLOBAL`
[Rpl_semi_sync_master_net_wait_time](#statvar_Rpl_semi_sync_master_net_wait_time) | numeric | `GLOBAL`
[Rpl_semi_sync_master_net_waits](#statvar_Rpl_semi_sync_master_net_waits) | numeric | `GLOBAL`
[Rpl_semi_sync_master_no_times](#statvar_Rpl_semi_sync_master_no_times) | numeric | `GLOBAL`
[Rpl_semi_sync_master_no_tx](#statvar_Rpl_semi_sync_master_no_tx) | numeric | `GLOBAL`
[Rpl_semi_sync_master_status](#statvar_Rpl_semi_sync_master_status) | boolean | `GLOBAL`
[Rpl_semi_sync_master_timefunc_failures](#statvar_Rpl_semi_sync_master_timefunc_failures) | numeric | `GLOBAL`
[Rpl_semi_sync_master_tx_avg_wait_time](#statvar_Rpl_semi_sync_master_tx_avg_wait_time) | numeric | `GLOBAL`
[Rpl_semi_sync_master_tx_wait_time](#statvar_Rpl_semi_sync_master_tx_wait_time) | numeric | `GLOBAL`
[Rpl_semi_sync_master_tx_waits](#statvar_Rpl_semi_sync_master_tx_waits) | numeric | `GLOBAL`
[Rpl_semi_sync_master_wait_pos_backtraverse](#statvar_Rpl_semi_sync_master_wait_pos_backtraverse) | numeric | `GLOBAL`
[Rpl_semi_sync_master_wait_sessions](#statvar_Rpl_semi_sync_master_wait_sessions) | numeric | `GLOBAL`
[Rpl_semi_sync_master_yes_tx](#statvar_Rpl_semi_sync_master_yes_tx) | numeric | `GLOBAL`
[Rpl_semi_sync_slave_status](#statvar_Rpl_semi_sync_slave_status) | boolean | `GLOBAL`
[Rsa_public_key](#statvar_Rsa_public_key) | string | `GLOBAL`
[Select_full_join](#statvar_Select_full_join) | numeric | `GLOBAL ` | ` SESSION`
[Select_full_range_join](#statvar_Select_full_range_join) | numeric | `GLOBAL ` | ` SESSION`
[Select_range](#statvar_Select_range) | numeric | `GLOBAL ` | ` SESSION`
[Select_range_check](#statvar_Select_range_check) | numeric | `GLOBAL ` | ` SESSION`
[Select_scan](#statvar_Select_scan) | numeric | `GLOBAL ` | ` SESSION`
[Slave_heartbeat_period](#statvar_Slave_heartbeat_period) |   | `GLOBAL`
[Slave_last_heartbeat](#statvar_Slave_last_heartbeat) |   | `GLOBAL`
[Slave_open_temp_tables](#statvar_Slave_open_temp_tables) | numeric | `GLOBAL`
[Slave_received_heartbeats](#statvar_Slave_received_heartbeats) |   | `GLOBAL`
[Slave_retried_transactions](#statvar_Slave_retried_transactions) | numeric | `GLOBAL`
[Slave_running](#statvar_Slave_running) | boolean | `GLOBAL`
[Slow_launch_threads](#statvar_Slow_launch_threads) | numeric | `GLOBAL ` | ` SESSION`
[Slow_queries](#statvar_Slow_queries) | numeric | `GLOBAL ` | ` SESSION`
[Sort_merge_passes](#statvar_Sort_merge_passes) | numeric | `GLOBAL ` | ` SESSION`
[Sort_range](#statvar_Sort_range) | numeric | `GLOBAL ` | ` SESSION`
[Sort_rows](#statvar_Sort_rows) | numeric | `GLOBAL ` | ` SESSION`
[Sort_scan](#statvar_Sort_scan) | numeric | `GLOBAL ` | ` SESSION`
[Ssl_accept_renegotiates](#statvar_Ssl_accept_renegotiates) | numeric | `GLOBAL`
[Ssl_accepts](#statvar_Ssl_accepts) | numeric | `GLOBAL`
[Ssl_callback_cache_hits](#statvar_Ssl_callback_cache_hits) | numeric | `GLOBAL`
[Ssl_cipher](#statvar_Ssl_cipher) | string | `GLOBAL ` | ` SESSION`
[Ssl_cipher_list](#statvar_Ssl_cipher_list) | string | `GLOBAL ` | ` SESSION`
[Ssl_client_connects](#statvar_Ssl_client_connects) | numeric | `GLOBAL`
[Ssl_connect_renegotiates](#statvar_Ssl_connect_renegotiates) | numeric | `GLOBAL`
[Ssl_ctx_verify_depth](#statvar_Ssl_ctx_verify_depth) | numeric | `GLOBAL`
[Ssl_ctx_verify_mode](#statvar_Ssl_ctx_verify_mode) | numeric | `GLOBAL`
[Ssl_default_timeout](#statvar_Ssl_default_timeout) | numeric | `GLOBAL ` | ` SESSION`
[Ssl_finished_accepts](#statvar_Ssl_finished_accepts) | numeric | `GLOBAL`
[Ssl_finished_connects](#statvar_Ssl_finished_connects) | numeric | `GLOBAL`
[Ssl_server_not_after](#statvar_Ssl_server_not_after) | numeric | `GLOBAL ` | ` SESSION`
[Ssl_server_not_before](#statvar_Ssl_server_not_before) | numeric | `GLOBAL ` | ` SESSION`
[Ssl_session_cache_hits](#statvar_Ssl_session_cache_hits) | numeric | `GLOBAL`
[Ssl_session_cache_misses](#statvar_Ssl_session_cache_misses) | numeric | `GLOBAL`
[Ssl_session_cache_mode](#statvar_Ssl_session_cache_mode) | string | `GLOBAL`
[Ssl_session_cache_overflows](#statvar_Ssl_session_cache_overflows) | numeric | `GLOBAL`
[Ssl_session_cache_size](#statvar_Ssl_session_cache_size) | numeric | `GLOBAL`
[Ssl_session_cache_timeouts](#statvar_Ssl_session_cache_timeouts) | numeric | `GLOBAL`
[Ssl_sessions_reused](#statvar_Ssl_sessions_reused) | numeric | `GLOBAL ` | ` SESSION`
[Ssl_used_session_cache_entries](#statvar_Ssl_used_session_cache_entries) | numeric | `GLOBAL`
[Ssl_verify_depth](#statvar_Ssl_verify_depth) | numeric | `GLOBAL ` | ` SESSION`
[Ssl_verify_mode](#statvar_Ssl_verify_mode) | numeric | `GLOBAL ` | ` SESSION`
[Ssl_version](#statvar_Ssl_version) | string | `GLOBAL ` | ` SESSION`
[Table_locks_immediate](#statvar_Table_locks_immediate) | numeric | `GLOBAL`
[Table_locks_waited](#statvar_Table_locks_waited) | numeric | `GLOBAL`
[Table_open_cache_hits](#statvar_Table_open_cache_hits) | numeric | `GLOBAL ` | ` SESSION`
[Table_open_cache_misses](#statvar_Table_open_cache_misses) | numeric | `GLOBAL ` | ` SESSION`
[Table_open_cache_overflows](#statvar_Table_open_cache_overflows) | numeric | `GLOBAL ` | ` SESSION`
[Tc_log_max_pages_used](#statvar_Tc_log_max_pages_used) | numeric | `GLOBAL`
[Tc_log_page_size](#statvar_Tc_log_page_size) | numeric | `GLOBAL`
[Tc_log_page_waits](#statvar_Tc_log_page_waits) | numeric | `GLOBAL`
[Threads_cached](#statvar_Threads_cached) | numeric | `GLOBAL`
[Threads_connected](#statvar_Threads_connected) | numeric | `GLOBAL`
[Threads_created](#statvar_Threads_created) | numeric | `GLOBAL`
[Threads_running](#statvar_Threads_running) | numeric | `GLOBAL`
[Uptime](#statvar_Uptime) | numeric | `GLOBAL`
[Uptime_since_flush_status](#statvar_Uptime_since_flush_status) | numeric | `GLOBAL`


系统变量有如下含义。有关MySQL Cluster的状态变量含义，参考[第17.3.4.4小节，MySQL Cluster系统变量](mysql_cluster)。

* <a name='statvar_Aborted_clients' href='#statvar_Aborted_clients'>Aborted_clients</a>  
因客户端没有正常关闭的而中止的死连接的数目。见[第5.2.11节，](5.2.11，通信错误与中止连接)。
[5.2.11]: http://dev.mysql.com/doc/refman/5.6/en/communication-errors.html

* <a name='statvar_Aborted_connects' href='#statvar_Aborted_connects'>Aborted_connects</a>  
尝试连结MySQL服务器的失败的次数。见[第5.2.11节，](5.2.11，通信错误与中止连接)。
如需连接相关信息，检查[Connection_errors__xxx_](Connection_errors__xxx_)状态变量和[host_cache](host_cache)表。

* <a name='statvar_Binlog_cache_disk_use' href='#statvar_Binlog_cache_disk_use'>Binlog_cache_disk_use</a>  
使用临时二进制日志缓存（temprorary binary log cache）但超过了[biglog_cache_size](binlog_cache_size)所以使用了临时文件存储语句的事务数。
引起二进制日志缓存写入到硬盘的非事务语句数量在状态变量[Binlog_stmt_cache_disk_use](Binlog_stmt_cache_disk_use)中单独跟踪。

* <a name='statvar_Binlog_cache_use' href='#statvar_Binlog_cache_use'>Binlog_cache_use</a>  
使用二进制日志缓存的事务数目。

* <a name='statvar_Binlog_stmt_cache_disk_use' href='#statvar_Binlog_stmt_cache_disk_use'>Binlog_stmt_cache_disk_use</a>  
使用二进制日志语句缓存（binary log statement cache）但超过了[binlog_stmt_cache_size](binlog_stmt_cache_size)所以使用了临时文件存储语句的非事务数语句数目。
[binlog_stmt_cache_size]: http://dev.mysql.com/doc/refman/5.6/en/replication-options-binary-log.html#sysvar_binlog_stmt_cache_size

* <a name='statvar_Binlog_stmt_cache_use' href='#statvar_Binlog_stmt_cache_use'>Binlog_stmt_cache_use</a>  
使用了二进制日志语句缓存的非事务语句数目。

* <a name='statvar_Bytes_received' href='#statvar_Bytes_received'>Bytes_received</a>  
从所有客户端接收的字节数。

* <a name='statvar_Bytes_sent' href='#statvar_Bytes_sent'>Bytes_sent</a>  
发送给所有客户端的字节数。

* <a name='statvar_Com_xxx' href='#statvar_Com_xxx'>Com_xxx</a>  
`Com_xxx`语句计数器表示___xxx___语句被执行的次数。每一种语句类型都有一个对应的状态变量。例如，`Com_delete`和`Com_update`统计[DELETE](delete)和[UPDATE](update)语句，相应的，`Com_delete_multi`和`Com_update_multi`是类似的，但是统计使用了多表的[DELETE](delete)和[UPDATE](update)的语句。
如果一个查询的结果是从查询缓存中返回的，服务器会增加[Qcache_hits](statvar_Qcache_hits)的状态变量，而不会加`Com_select`。参考[8.9.3.4节，查询缓存的状态与维护](query-cache-status-and-maintenance)。
即使在预编译参数未知或执行过程中有错误发生，所有`Com_stmt__xxx_`的变量都会增加。也就是说，这些值对应的是发出的请求的数目，而不是请求成功完成的数目。
`Com_stmt_xxx`状态变量如下：
    * Com_stmt_prepare
    * Com_stmt_execute
    * Com_stmt_fetch
    * Com_stmt_send_long_data
    * Com_stmt_reset
    * Com_stmt_close

  这些变量表示预编译语句命令。他们的名字指的是在网络层使用的`Com_xxx`的命令集。也就是说，他们的值在调用以及执行诸如**mysql_stmt_prepared**, **mysql_stmt_execute()**的预编译语句API时增加。然而，`Com_stmt_prepared`、`Com_stmt_execute`和`Com_stmt_close`也会分别因[PREPARE]、[EXECUTE]和[DEALLOCATE PREPARE]而增加。另外，老版本的语句计数器变量`Com_prepare_sql`、`Com_execute_sql`和`Com_dealloc_sql`的值也会因[PREPARE]、[EXECUTE]和[DEALLOCATE PREPARE]而增加。`Com_stmt_fetch`代表从游标中获取数据时的网络往返总数。
  `Com_stat_reprepare`指的是表或视图的元数据发生变化后服务器对使用了它们的语句自动重新预编译的次数。一个重新预编译操作会增加`Com_stmt_reprepare`和`Com_stmt_prepard`。

* <a name='statvar_Compression' href='#statvar_Compression'>Compression</a>  
是否在客户端/服务器协议中使用了压缩。

* <a name='statvar_Connection_error_xxx' href='#statvar_Connection_error_xxx'>Connection_error_xxx</a>  
这些变量提供了在客户端连接过程中发生错误的信息。它们是仅全局所有且代表所有主机连接错误的总和。这些变量跟踪错误并不占用主机缓存（参考第8.11.5.2，DNS查询优化和主机缓存），比如不相关联的TCP连接，在很早期的连结中发生（甚至早到连IP都不确认），或没有指定任何具体IP地址（如内存不足的情况）。这些变量是在MySQL 5.6.5中加入的。
    * Connection_error_accept
    在侦听端口上调用`accept()`时发生的错误数。
    * Connection_error_internal
    因服务器内部错误引起的拒绝连接数，比如启动一个新线程失败或内存不足的情况。
    * Connection_error_max_connections
    因服务器[max_connections]上限到达而引起的拒绝连接数。
    * Connection_error_peer_addr
    在搜索正在连结的客户端的IP地址时发生错误的数目。
    * Connection_errors_select
    在侦听端口上调用`select()`或`poll()`时发生错误的数目。（这个操作的失败并不一定意味客户端连接被拒绝。）
    * Connection_errors_tcpwrap
    被`libwrap`包拒绝的连接的数目。

* <a name='statvar_Connections' href='#statvar_Connections'>Connections</a>  
尝试连接（成功或失败）MySQL服务器的连接数。

* <a name='statvar_Created_tmp_disk_tables' href='#statvar_Created_tmp_disk_tables'>Created_tmp_disk_tables</a>  
在执行语句时由服务器创建的内部硬盘临时表的数目。
如果一个内部临时表在刚开始时是以内存表创建的，但后来变得太大了，MySQL会自动转为硬盘表。内存临时表大小的上限是[tmp_table_size]和[max_heap_table_size]两者中的小者。如果[Created_tmp_disk_table]值很大，你可以增大[tmp_table_size]或[max_heap_table_size]的值来减少内存中的内部临时表被转化为硬盘表的可能性。
你可以通过比较[Created_tmp_disk_tables]和[Create_tmp_tables]变量的值来比较创建的内部硬盘临时表的数目和创建临时表的总数。
也可以参考[第8.4.3.3节，MySQL如何使用内部临时表]。

* <a name='statvar_Created_tmp_files' href='#statvar_Created_tmp_files'>Created_tmp_files</a>  
[mysqld]创建的临时文件数。

* <a name='statvar_Created_tmp_tables' href='#statvar_Created_tmp_tables'>Created_tmp_tables</a>  
在执行语句时由服务器创建的内部临时表的数目。
你可以通过比较[Created_tmp_disk_tables]和[Create_tmp_tables]变量的值来比较创建的内部硬盘临时表的数目和创建临时表的总数。
也可以参考[第8.4.3.3节，MySQL如何使用内部临时表]。
每次执行[SHOW STATUS]都会使用一个内部临时表，并增加全局的[Created_tmp_tables]的变量值。

* <a name='statvar_Delayed_errors' href='#statvar_Delayed_errors'>Delayed_errors</a>  
在使用[INSERT DELAYED]写入时因某些错误发生造成而写入的行数（可能是`duplicate key`）。
在MySQL 5.6.7中，这个状态变量是过期的（因为DELAYED插入已废弃），并且在将来的版本中会被移除。

* <a name='statvar_Delayed_insert_threads' href='#statvar_Delayed_insert_threads'>Delayed_insert_threads</a>  
非事务表使用的[INSERT DELAYED]处理线程数。
在MySQL 5.6.7中，这个状态变量是过期的（因为DELAYED插入已废弃），并且在将来的版本中会被移除。

* <a name='statvar_Delayed_writes' href='#statvar_Delayed_writes'>Delayed_writes</a>  
使用[INSERT DELAYED]写入到非事务表中的数据行数。
在MySQL 5.6.7中，这个状态变量是过期的（因为DELAYED插入已废弃），并且在将来的版本中会被移除。

* <a name='statvar_Flush_commands' href='#statvar_Flush_commands'>Flush_commands</a>  
服务器刷表的次数，不管是因为用户执行了[FLUSH TABLES]语句还是因为服务器内部裙定期操作。在收到`COM_REFRESH`包时这个值也会增加。这与[Com_flush]有区别，[Com_flush]指的是多少个`FLUSH`语句被执行了，无论是[FLUSH TABLES]、[FLUSH LOGS]还是其它等等。

* <a name='statvar_Handler_commit' href='#statvar_Handler_commit'>Handler_commit</a>  
内部[COMMIT]语句数目。

* <a name='statvar_Handler_delete' href='#statvar_Handler_delete'>Handler_delete</a>  
从表里删除行的次数。

* <a name='statvar_Handler_external_lock' href='#statvar_Handler_external_lock'>Handler_external_lock</a>  
服务器什会每次调用exteral_lock()时增加这个变量，常发生在访问一个表实例的开始和结束。这可能在不同的存储引擎之间有一些不同。例如，这个变量可以用在提示一个语句访问一张分区表时，在锁发生时有多少个分区被剪掉：检查计数器因这个语句增加了多少，减去2（表本身两次调用），然后再除以2就得到被锁住的分区数。这个变量在MySQL 5.6.2中加入。

* <a name='statvar_Handler_mrr_init' href='#statvar_Handler_mrr_init'>Handler_mrr_init</a>  
服务器使用存储引擎自己实现的访问表的多路读（Multi-Range Read）的次数。

* <a name='statvar_Handler_prepare' href='#statvar_Handler_prepare'>Handler_prepare</a>  
两段式提交操作中预编译段的计数器。

* <a name='statvar_Handler_read_first' href='#statvar_Handler_read_first'>Handler_read_first</a>  
索引中第一个条目被读取的数目。如果这个值很高，表明服务器做了很多全索引扫描；如`SELECT col1 FROM foo`，假设`col1`是有索引的。

* <a name='statvar_Handler_read_key' href='#statvar_Handler_read_key'>Handler_read_key</a>  
基于一个有索引的列来读取行的请求数。如果这个值很高，这是一个很好的迹象，你的表针对查询的索引非常好。

* <a name='statvar_Handler_read_last' href='#statvar_Handler_read_last'>Handler_read_last</a>  
读一个索引最后一个键值的请求数。在有`ORDER BY`的情况下，服务器会先发出一个首个键值（first-key）的请求，这个请求后紧跟着一些下一个键值（next-key）请求，面在有`ORDER BY DESC`的情况下，服务器会先发出一个最末键值（last-key）的请求，这个请求后紧跟着一些前一个键值（previous-key）的请求。这个变量在MySQL 5.6.1中被加入。

* <a name='statvar_Handler_read_next' href='#statvar_Handler_read_next'>Handler_read_next</a>  
在键序列中读下一行的请求数。如果你在一个有索引的万上做范围查找或做一个索引扫描，这个值会增大。

* <a name='statvar_Handler_read_prev' href='#statvar_Handler_read_prev'>Handler_read_prev</a>  
在键序列中读前一行的请求数。这个读方法主要是用来优化`ORDER BY ... DESC`的。

* <a name='statvar_Handler_read_rnd' href='#statvar_Handler_read_rnd'>Handler_read_rnd</a>  
在一个固定位置读一行的请求数。如果你做了大量对结果排序的查询，这个值会很高。很可能你有大量需要MySQL扫描整表或是没有用键值的关联操作的查询。

* <a name='statvar_Handler_read_rnd_next' href='#statvar_Handler_read_rnd_next'>Handler_read_rnd_next</a>  
在数据文件中读取下一行的请求数。如果你做了很多扫表操作，这个值会很大。一般来说这表明你的表没有被正确索引或你的查询没有写得能够利用到索引。

* <a name='statvar_Handler_rollback' href='#statvar_Handler_rollback'>Handler_rollback</a>  
向存储引擎发送的执行rollback操作的请求数。

* <a name='statvar_Hanlder_savepoint' href='#statvar_Hanlder_savepoint'>Hanlder_savepoint</a>  
向存储引擎发送的放置一个保存点（savepoint）的请求数。

* <a name='statvar_Handler_savepoint_rollback' href='#statvar_Handler_savepoint_rollback'>Handler_savepoint_rollback</a>  
向存储引擎发送的执行rollback保存点操作的请求数。

* <a name='statvar_Handler_update' href='#statvar_Handler_update'>Handler_update</a>  
更新表中一行的请求数。

* <a name='statvar_Handler_write' href='#statvar_Handler_write'>Handler_write</a>  
向表中插入一行的请求数。

* <a name='statvar_Innodb_available_undo_logs' href='#statvar_Innodb_available_undo_logs'>Innodb_available_undo_logs</a>  
可用的`InnoDB` [undo logs]的总数。是对[innodb_undo_logs]系统变量的补充，[innodb_undo_logs]表示有使用的undo logs的总数。

* <a name='statvar_Innodb_buffer_pool_dump_status' href='#statvar_Innodb_buffer_pool_dump_status'>Innodb_buffer_pool_dump_status</a>  
记录在`InnoDB` [buffer pool][buffer_pool]中所持有的[pages][pages]的操作进度，由`innodb_buffer_pool_dump_at_shutdown`或`innodb_buffer_pool_dump_now`设置触发。

* <a name='statvar_Innodb_buffer_pool_load_status' href='#statvar_Innodb_buffer_pool_load_status'>Innodb_buffer_pool_load_status</a>  
通过读取较早时间点对应的[pages][pages]集来预热`InnoDB` [buffer pool][buffer_pool]的操作进度，由[innodb_buffer_pool_load_at_startup]或[innodb_buffer_pool_load_now]设置触发。如果这个操作会造成负载过重，你可以用[innodb_buffer_pool_load_abort]来取消它。

* <a name='statvar_Innodb_buffer_pool_bytes_data' href='#statvar_Innodb_buffer_pool_bytes_data'>Innodb_buffer_pool_bytes_data</a>  
`InnoDB` [buffer pool][buffer_pool]当前容纳数据的总字节数。这个数字包括脏（[dirty]）页和干净的页。当压缩（[compressed]）表引起buffer pool持有不同大小的页时，可以用它来计算比[Innodb_buffer_pool_pages_data]更精确的内存使用量。

* <a name='statvar_Innodb_buffer_pool_pages_data' href='#statvar_Innodb_buffer_pool_pages_data'>Innodb_buffer_pool_pages_data</a>  
`InnoDB` [buffer pool][buffer_pool]当前容纳的数据的页数。这个数字包括脏（[dirty]）页和干净的页。

* <a name='statvar_Innodb_buffer_pool_bytes_dirty' href='#statvar_Innodb_buffer_pool_bytes_dirty'>Innodb_buffer_pool_bytes_dirty</a>  
`InnoDB` [buffer pool][buffer_pool]当前所持有的脏页（[dirty_pages]）的字节数。当压缩（[compressed]）表引起buffer pool持有不同大小的页时，可以用它来计算比[Innodb_buffer_pool_pages_dirty]更精确的内存使用量。

* <a name='statvar_Innodb_buffer_pool_pages_dirty' href='#statvar_Innodb_buffer_pool_pages_dirty'>Innodb_buffer_pool_pages_dirty</a>  
`InnoDB` [buffer pool][buffer_pool]当前所持有的脏页（[dirty_pages]）的总数。

* <a name='statvar_Innodb_buffer_pool_pages_flushed' href='#statvar_Innodb_buffer_pool_pages_flushed'>Innodb_buffer_pool_pages_flushed</a>  
`InnoDB` [buffer pool][buffer_pool]刷新页面（[flush][pages][pages]）的请求数。

* <a name='statvar_Innodb_buffer_pool_pages_free' href='#statvar_Innodb_buffer_pool_pages_free'>Innodb_buffer_pool_pages_free</a>  
`InnoDB` [buffer pool][buffer_pool]中空闲的页（[pages][pages][pages][pages]）数。

* <a name='statvar_Innodb_buffer_pool_pages_latched' href='#statvar_Innodb_buffer_pool_pages_latched'>Innodb_buffer_pool_pages_latched</a>  
`InnoDB` [buffer pool][buffer_pool]中被锁住的页面（[pages][pages]）。它们是正在被读或写的页面，或是因为其它原因不能被刷新（[flushed]）或删除的页面。

* <a name='statvar_Innodb_buffer_pool_pages_misc' href='#statvar_Innodb_buffer_pool_pages_misc'>Innodb_buffer_pool_pages_misc</a>  
`InnoDB` [buffer pool][buffer_pool]中因为被分配给管理开销而处于忙碌状态的页（[pages][pages]）数，如行锁（[row locks]）或自适应哈希索引([adaptive hash index])。这个值也可以用[Innodb_buffer_pool_pages_total] - [Innodb_buffer_pool_pages_free] - [Innodb_buffer_pool_pages_data]计算出来。

* <a name='statvar_Innodb_buffer_pool_pages_total' href='#statvar_Innodb_buffer_pool_pages_total'>Innodb_buffer_pool_pages_total</a>  
`InnoDB` [buffer pool][buffer_pool]总大小，页（[pages][pages]）数。

* <a name='statvar_Innodb_buffer_pool_read_ahead' href='#statvar_Innodb_buffer_pool_read_ahead'>Innodb_buffer_pool_read_ahead</a>  
通过后台预读进程读入`InnoDB` [buffer pool][buffer_pool]的页（[pages][pages]）数。

* <a name='statvar_Innodb_buffer_pool_read_ahead_evicted' href='#statvar_Innodb_buffer_pool_read_ahead_evicted'>Innodb_buffer_pool_read_ahead_evicted</a>  
通过后台预读进程读入`InnoDB` [buffer pool][buffer_pool]的页因未被查询访问而踢出内存的页（[pages][pages]）数。

* <a name='statvar_Innodb_buffer_pool_read_requests' href='#statvar_Innodb_buffer_pool_read_requests'>Innodb_buffer_pool_read_requests</a>  
`InnoDB` [buffer pool][buffer_pool]逻辑读请求数。这些请求可能通直接返回已经在内存中的数据来响应，或通读取首次从硬盘读取数据到内存的数据来响应。

* <a name='statvar_Innodb_buffer_pool_reads' href='#statvar_Innodb_buffer_pool_reads'>Innodb_buffer_pool_reads</a>  
`InnoDB`可能不能满足从[buffer pool][buffer_pool]读取，而必须从直接从硬盘读取数据的逻辑读数。

* <a name='statvar_Innodb_buffer_pool_wait_free' href='#statvar_Innodb_buffer_pool_wait_free'>Innodb_buffer_pool_wait_free</a>  
正常情况下，写入`InnoDB` [buffer pool][buffer_pool]是在后台发生的。当`InnoDB`需要读或创建一个页（[page][pages]）且没有干净的页可用时，`InnoDB`首先会刷新一些脏页（[dirty pages]）并等待操作结束这个计数器统计了这些等待的实例数。如果[innodb_buffer_pool_size]的值设置合理，这个值会非常小。

* <a name='statvar_Innodb_buffer_pool_write_requests' href='#statvar_Innodb_buffer_pool_write_requests'>Innodb_buffer_pool_write_requests</a>  
`InnoDB` [buffer pool][buffer_pool]完成的写入次数。

* <a name='statvar_Innodb_data_fsyncs' href='#statvar_Innodb_data_fsyncs'>Innodb_data_fsyncs</a>  
到目前为止`fsync()`的操作数。配置选项[innodb_flush_method]的设置影响`fsync()`的调用频率。

* <a name='statvar_Innodb_data_pending_fsyncs' href='#statvar_Innodb_data_pending_fsyncs'>Innodb_data_pending_fsyncs</a>  
当前等待执行的`fsync()`操作的数目。配置选项[innodb_flush_method]的设置影响`fsync()`的调用频率。

* <a name='statvar_Innodb_data_pending_reads' href='#statvar_Innodb_data_pending_reads'>Innodb_data_pending_reads</a>  
当前挂起的读取数。

* <a name='statvar_Innodb_data_pending_writes' href='#statvar_Innodb_data_pending_writes'>Innodb_data_pending_writes</a>  
当前挂起的写数。


* <a name='statvar_Innodb_data_read' href='#statvar_Innodb_data_read'>Innodb_data_read</a>  
从服务器起启后写入数据的总数。

* <a name='statvar_Innodb_data_reads' href='#statvar_Innodb_data_reads'>Innodb_data_reads</a>  
读数据的总数。

* <a name='statvar_Innodb_data_writes' href='#statvar_Innodb_data_writes'>Innodb_data_writes</a>  
写数据的总数。

* <a name='statvar_Innodb_data_written' href='#statvar_Innodb_data_written'>Innodb_data_written</a>  
到目前为止写入数据的总字节数。

* <a name='statvar_Innodb_dblwr_pages_writes' href='#statvar_Innodb_dblwr_pages_writes'>Innodb_dblwr_pages_writes</a>  
已经被写入到[doublewrite buffer]里的页（[pages][pages]）数。参考[5.3.1节，InnoDB 磁盘I/O]。

* <a name='statvar_Innodb_dblwr_writes' href='#statvar_Innodb_dblwr_writes'>Innodb_dblwr_writes</a>  
双写（doublewrite）操作被执行的次数。参考[5.3.1节，InnoDB 磁盘I/O]。

* <a name='statvar_Innodb_have_atomic_builtins' href='#statvar_Innodb_have_atomic_builtins'>Innodb_have_atomic_builtins</a>  
表示服务器是否使用[atomic instrucations]编译。

* <a name='statvar_Innodb_log_writes' href='#statvar_Innodb_log_writes'>Innodb_log_writes</a>  
因[log buffer]太小需要等待（[wait]）刷新（[flushed]）后才能继续的次数。

* <a name='statvar_Innodb_log_write_requests' href='#statvar_Innodb_log_write_requests'>Innodb_log_write_requests</a>  
对`InnoDB` [redo log]的写请求次数。

* <a name='statvar_Innodb_log_writes' href='#statvar_Innodb_log_writes'>Innodb_log_writes</a>  
对`InnoDB` [redo log]文件物理写的次数。

* <a name='statvar_Innodb_num_open_files' href='#statvar_Innodb_num_open_files'>Innodb_num_open_files</a>  
`InnoDB`当前所持有打开的文件数。

* <a name='statvar_Innodb_os_log_fsyncs' href='#statvar_Innodb_os_log_fsyncs'>Innodb_os_log_fsyncs</a>  
`fsync()`已经写入`InnoDB` [redo log]文件的数目。

* <a name='statvar_Innodb_os_log_pending_fsyncs' href='#statvar_Innodb_os_log_pending_fsyncs'>Innodb_os_log_pending_fsyncs</a>  
等待执行的对`InnoDB` [redo log]文件写操作的数目。

* <a name='statvar_Innodb_os_log_written' href='#statvar_Innodb_os_log_written'>Innodb_os_log_written</a>  
已经写入`InnoDB` [redo log]文件的字节数。

* <a name='statvar_Innodb_page_size' href='#statvar_Innodb_page_size'>Innodb_page_size</a>  
编译的`InnoDB`页面大小（默认16K）。好多值在页面里就被计数；页面大小使得它们更容易被转为字节。

* <a name='statvar_Innodb_page_created' href='#statvar_Innodb_page_created'>Innodb_page_created</a>  
`InnoDB`表操作创建的页数。

* <a name='statvar_Innodb_pages_read' href='#statvar_Innodb_pages_read'>Innodb_pages_read</a>  
`InnoDB`表操作读取的页数。

* <a name='statvar_Innodb_pages_written' href='#statvar_Innodb_pages_written'>Innodb_pages_written</a>  
`InnoDB`表操作写入的页数。

* <a name='statvar_Innodb_row_lock_current_waits' href='#statvar_Innodb_row_lock_current_waits'>Innodb_row_lock_current_waits</a>  
`InnoDB`表操作正在等待行锁（[row lock][row_lock]）的数量。

* <a name='statvar_Innodb_row_lock_time' href='#statvar_Innodb_row_lock_time'>Innodb_row_lock_time</a>  
获取`InnoDB`表行锁所花费的总时长，单位是微秒。

* <a name='statvar_Innodb_row_lock_time_avg' href='#statvar_Innodb_row_lock_time_avg'>Innodb_row_lock_time_avg</a>  
获取`InnoDB`表行锁所花费的平均时长，单位是微秒。

* <a name='statvar_Innodb_row_lock_time_max' href='#statvar_Innodb_row_lock_time_max'>Innodb_row_lock_time_max</a>  
获取`InnoDB`表行锁所花费的最大时长，单位是微秒。

* <a name='statvar_Innodb_row_lock_waits' href='#statvar_Innodb_row_lock_waits'>Innodb_row_lock_waits</a>  
`InnoDB`表操作必须等待行锁（[row lock][row_lock]）的次数。

* <a name='statvar_Innodb_rows_deleted' href='#statvar_Innodb_rows_deleted'>Innodb_rows_deleted</a>  
从`InnoDB`表中删除的行数。

* <a name='statvar_Innodb_rows_inserted' href='#statvar_Innodb_rows_inserted'>Innodb_rows_inserted</a>  
向`InnoDB`表中插入的行数。

* <a name='statvar_Innodb_rows_read' href='#statvar_Innodb_rows_read'>Innodb_rows_read</a>  
从`InnoDB`表中读取的行数。

* <a name='statvar_Innodb_rows_updated' href='#statvar_Innodb_rows_updated'>Innodb_rows_updated</a>  
`InnoDB`表中更新的行数。

* <a name='statvar_Innodb_truncated_status_writes' href='#statvar_Innodb_truncated_status_writes'>Innodb_truncated_status_writes</a>  
`SHOW ENGINE INNODB STATUS`语句输入被截断的次数。

* <a name='statvar_Key_blocks_not_flushed' href='#statvar_Key_blocks_not_flushed'>Key_blocks_not_flushed</a>  
`MyISAM` key cache中已经发生改变但尚未刷到硬盘的主键块（key blocks）数。

* <a name='statvar_Key_blocks_unused' href='#statvar_Key_blocks_unused'>Key_blocks_unused</a>  
`MyISAM` key cache中未被使用的块数。你可以用这个值来确定多少key cache在使用中；见[第5.1.4章，服务器系统变量]中[key_buffer_size]的讨论。

* <a name='statvar_Key_blocks_used' href='#statvar_Key_blocks_used'>Key_blocks_used</a>  
`MyISAM` key cache中使用的块数。这个值是一个高水位标记表示曾经某个时刻使用块数的最大值。

* <a name='statvar_Key_read_requests' href='#statvar_Key_read_requests'>Key_read_requests</a>  
从`MyISAM` key cache读取主键块（key blocks）的请求数。

* <a name='statvar_Key_reads' href='#statvar_Key_reads'>Key_reads</a>  
从硬盘往`MyISAM` key cache中物理读取一个主键块（key block）的次数数。如果[Key_reads]值很大，你的[key_buffer_size]可能太小了。缓存未命中率可以用[Key_reads]/[Key_reads_requests]来计算。

* <a name='statvar_Key_write_requests' href='#statvar_Key_write_requests'>Key_write_requests</a>  
向`MyISAM` key cache写入主键块的请求数。

* <a name='statvar_Key_writes' href='#statvar_Key_writes'>Key_writes</a>  
从`MyISAM` key cache往硬盘物理写入一个块的次数。

* <a name='statvar_Last_query_cost' href='#statvar_Last_query_cost'>Last_query_cost</a>  
查询优化器计算的上个编译的查询的总开销。这对比较同一查询的不同执行计划非常有用。默认值0意味着目前还没有查询被编译。默认值为0。[Last_query_cost]是会话范围的。
[Last_query_cost]的值能精确计算的是简单的查询，而不是那些有子查询或UNION的复杂查询。对于后者，它的值被设为0。

* <a name='statvar_Last_query_partial_plans' href='#statvar_Last_query_partial_plans'>Last_query_partial_plans</a>  
查询优化器在为前一个查询创建执行计划构造器时的所迭代的次数。[Last_query_partial_plans]是会话范围的。这个变量是在MySQL 5.6.5中加入的。

* <a name='statvar_Max_used_connections' href='#statvar_Max_used_connections'>Max_used_connections</a>  
自服务器启动以来同时使用的连接数的最大值。

* <a name='statvar_Not_flushed_delayed_rows' href='#statvar_Not_flushed_delayed_rows'>Not_flushed_delayed_rows</a>  
等待使用`INSERT DELAYED`写入到非事务表中的行数。
在MySQL 5.6.7中，这个状态变量是过期的（因为DELAYED插入已废弃），并且在将来的版本中会被移除。

* <a name='statvar_Open_files' href='#statvar_Open_files'>Open_files</a>  
打开的表数。这个数包括服务器打开的常规文件。它不包括其它如套接字或管道等文件。这个数也不包括那些存储引擎使用自己内部方法打开而不是服务器层打开的文件。

* <a name='statvar_Open_streams' href='#statvar_Open_streams'>Open_streams</a>  
打开的流数（主要用来记日志）。

* <a name='statvar_Open_table_definitions' href='#statvar_Open_table_definitions'>Open_table_definitions</a>  
缓存的`.frm`文件数。

* <a name='statvar_Open_tables' href='#statvar_Open_tables'>Open_tables</a>  
已经被打开的表数。如果[Open_tables]值很大，你的[table_open_cache]值可能设得太小了

* <a name='statvar_Performace_schema_xxx' href='#statvar_Performace_schema_xxx'>Performace_schema_xxx</a>  
性能库（Performace Schema）状态变量列在[第21.13节，性能库状态变量]中。这些变量提供因为内存限制而无法加载或创建的监测信息。

* <a name='statvar_Prepared_stmt_count' href='#statvar_Prepared_stmt_count'>Prepared_stmt_count</a>  
当前预编译语句的数量 。（预编译语句的最大数量由系统变量[max_prepared_stmt_count]提供。）

* <a name='statvar_Qcache_free_blocks' href='#statvar_Qcache_free_blocks'>Qcache_free_blocks</a>  
查询缓存中空闲的内存块数。

* <a name='statvar_Qcache_free_memory' href='#statvar_Qcache_free_memory'>Qcache_free_memory</a>  
查询缓存中空间内存的总大小。

* <a name='statvar_Qcache_hits' href='#statvar_Qcache_hits'>Qcache_hits</a>  
命中查询缓存的数量。

* <a name='statvar_Qcache_inserts' href='#statvar_Qcache_inserts'>Qcache_inserts</a>  
加入到查询缓存中的查询数量。

* <a name='statvar_Qcache_lowmem_prunes' href='#statvar_Qcache_lowmem_prunes'>Qcache_lowmem_prunes</a>  
因为内存不够而从查询缓存中删掉的查询数。

* <a name='statvar_Qcache_not_cached' href='#statvar_Qcache_not_cached'>Qcache_not_cached</a>  
没有被缓存的查询数（没法缓存或因为[query_cache_type]设置而没有缓存）。

* <a name='statvar_Qcache_queries_in_cache' href='#statvar_Qcache_queries_in_cache'>Qcache_queries_in_cache</a>  
在查询缓存中注册了的查询数量。

* <a name='statvar_Qcache_total_blocks' href='#statvar_Qcache_total_blocks'>Qcache_total_blocks</a>  
查询缓存中总的块数。

* <a name='statvar_Queries' href='#statvar_Queries'>Queries</a>  
服务器执行了的语句的数量。不像变量[Questions]，这个变量包括了在存储程序中执行的语句。它不统计`COM_PING`或`COM_STATISTICS`命令。

* <a name='statvar_Questions' href='#statvar_Questions'>Questions</a>  
服务器执行了的语句的数量。不像变量[Queries]，它只包括由客户端发给服务器的语句，而不包括在存储程序中执行的语句。这个变量不统计`COM_PING`、`COM_STATISTICS`、`COM_STMT_PREPARE`、`COM_STMT_CLOSE`或`COM_STMT_RESET`命令。

* <a name='statvar_Rpl_semi_sync_master_clients' href='#statvar_Rpl_semi_sync_master_clients'>Rpl_semi_sync_master_clients</a>  
半同步的从库数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_net_avg_wait_time' href='#statvar_Rpl_semi_sync_master_net_avg_wait_time'>Rpl_semi_sync_master_net_avg_wait_time</a>  
主库等待从库回应的平均微秒数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_net_wait_time' href='#statvar_Rpl_semi_sync_master_net_wait_time'>Rpl_semi_sync_master_net_wait_time</a>  
主库等待从库回应的总微秒数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_net_waits' href='#statvar_Rpl_semi_sync_master_net_waits'>Rpl_semi_sync_master_net_waits</a>  
主库等待从库回应的总次数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_no_times' href='#statvar_Rpl_semi_sync_master_no_times'>Rpl_semi_sync_master_no_times</a>  
主库关闭半同步复制的次数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_no_tx' href='#statvar_Rpl_semi_sync_master_no_tx'>Rpl_semi_sync_master_no_tx</a>  
从库没有应答成功的提交数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_status' href='#statvar_Rpl_semi_sync_master_status'>Rpl_semi_sync_master_status</a>  
半同步复制当时是否在主库上运行。如果这个插件已被启用，并且提交确认已经发生，这个值为`ON`。如果这个插件未被启用，或由于提交确认超时主库回到异步同步的状态，这个值为`OFF`。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_timefunc_failures' href='#statvar_Rpl_semi_sync_master_timefunc_failures'>Rpl_semi_sync_master_timefunc_failures</a>  
主库在调用诸如`gettimeofday()`的时间函数时失败的次数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_tx_avg_wait_time' href='#statvar_Rpl_semi_sync_master_tx_avg_wait_time'>Rpl_semi_sync_master_tx_avg_wait_time</a>  
主库等待每个事务的平均微秒数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_tx_wait_times' href='#statvar_Rpl_semi_sync_master_tx_wait_times'>Rpl_semi_sync_master_tx_wait_times</a>  
主库等待事务的总微秒数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_masrer_tx_waits' href='#statvar_Rpl_semi_sync_masrer_tx_waits'>Rpl_semi_sync_masrer_tx_waits</a>  
主库等待事务的总次数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_wait_pos_backtraverse' href='#statvar_Rpl_semi_sync_master_wait_pos_backtraverse'>Rpl_semi_sync_master_wait_pos_backtraverse</a>  
主库等待一个二进制日志位置比之前等待的还要靠前的事件的次数。这种情况见于事务等待回应的时序与它们写入二进制日志时序不同时。[^Rpl_semi_sync_master_wait_pos_backtraverse]
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。
[^Rpl_semi_sync_master_wait_pos_backtraverse]: lark翻译：主库等待“回溯”事件（其二进制日志位置比之前等待的事件还要靠前的事件）的次数。“回溯”事件发生在事务等待回应的顺序与它们的事件写入日志的顺序不同时。

* <a name='statvar_Rpl_semi_master_wait_sessions' href='#statvar_Rpl_semi_master_wait_sessions'>Rpl_semi_master_wait_sessions</a>  
当前等待从库应答的会话数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_master_yes_tx' href='#statvar_Rpl_semi_sync_master_yes_tx'>Rpl_semi_sync_master_yes_tx</a>  
从库应答成功的提交数。
这个变量只在主库端半同步复制插件（master-side semisynchronous replication plugin）安装了的情况下可用。

* <a name='statvar_Rpl_semi_sync_slave_status' href='#statvar_Rpl_semi_sync_slave_status'>Rpl_semi_sync_slave_status</a>  
半同步复制当时是否在从库上运行。如果这个插件启用并且从库的I/O线程在运行，这个值为`ON`，否则为`OFF`。

* <a name='statvar_Rsa_public_key' href='#statvar_Rsa_public_key'>Rsa_public_key</a>  
`sha256_password`验证插件所使用的RSA的公钥。这个值只有在服务器成功初始化了以系统变量[sha256_password_private_key_path]和[sha256_password_public_key_path]命名的文件时才不为空。[Rsa_public_key]的值来自后者文件。
如需更多关于`sha256_password`信息，参考[每6.3.7.4节，SHA-256验证插件]。
这个变量只在有MySQL使用了OpenSSL编译时有效。它是在MySQL 5.6.6中加入的。

* <a name='statvar_Select_full_join' href='#statvar_Select_full_join'>Select_full_join</a>  
因为有用到索引而做全表扫描的join数。如果这个值不为0，你应该仔细检查表的索引。

* <a name='statvar_Select_full_range_join' href='#statvar_Select_full_range_join'>Select_full_range_join</a>  
在引用表上做范围查找的join数。

* <a name='statvar_Select_range' href='#statvar_Select_range'>Select_range</a>  
在第一张表上做范围查找的join数。即使这个值很大也不是什么大问题。

* <a name='statvar_Select_range_check' href='#statvar_Select_range_check'>Select_range_check</a>  
在每一行数据后对键进行检查的不带键值的join数。如果这个值不为0，你应该仔细检查表的索引。

* <a name='statvar_Select_scan' href='#statvar_Select_scan'>Select_scan</a>  
在第一张表上做了全表扫描的join数。

* <a name='statvar_Slave_heartbeat_period' href='#statvar_Slave_heartbeat_period'>Slave_heartbeat_period</a>  
在一台复制从库上显示复制心跳间隔（单位为秒）。

* <a name='statvar_Slave_last_heartbeat' href='#statvar_Slave_last_heartbeat'>Slave_last_heartbeat</a>  
以时间戳（[TIMESTAMP]）显示一台复制从库接收到最新的心跳信号的时间。

* <a name='statvar_Slave_open_temp_tables' href='#statvar_Slave_open_temp_tables'>Slave_open_temp_tables</a>  
从库SQL线程当前打开的临时表个数。如果这个值大于0，关闭这台从库是不安全的。参考[第16.4.1.22，复制与临时表]。

* <a name='statvar_Slave_received_heartbeat' href='#statvar_Slave_received_heartbeat'>Slave_received_heartbeat</a>  
自从库重启或重置（也就是[CHANGE MASTER TO]语句被执行）后，这个计数器在每次接收到复制从库心跳时递增。

* <a name='statvar_Slave_retried_transactions' href='#statvar_Slave_retried_transactions'>Slave_retried_transactions</a>  
自从库起动以来复制从库SQL线程已经重试事务的次数。

* <a name='statvar_Slave_running' href='#statvar_Slave_running'>Slave_running</a>  
如果服务器是一台连上了主库的从库，且I/O和SQL线程都在运行，这个值为`ON`，否则为`OFF`。

* <a name='statvar_Slow_launch_threads' href='#statvar_Slow_launch_threads'>Slow_launch_threads</a>  
创建时间超过[slow_launch_time]秒的线程的数量。

* <a name='statvar_Slow_queries' href='#statvar_Slow_queries'>Slow_queries</a>  
执行时间超过[ong_query_time]秒的查询数。该计数器不管慢查询日志是否启用都会递增。 如需更多关于这个日志的信息，参考[第5.2.5节，慢查询日志]。

* <a name='statvar_Sort_merge_passes' href='#statvar_Sort_merge_passes'>Sort_merge_passes</a>  
排序算法已经执行的合并的数量，如果这个值较大，你可以考虑增加[sort_buffer_size]系统变量的大小一。

* <a name='statvar_Sort_range' href='#statvar_Sort_range'>Sort_range</a>  
使用范围排序的数量。

* <a name='statvar_Sort_rows' href='#statvar_Sort_rows'>Sort_rows</a>  
排完序的行数。

* <a name='statvar_Sort_scan' href='#statvar_Sort_scan'>Sort_scan</a>  
通过扫描表完成的排序的数量。

* <a name='statvar_Ssl_accept_renegotiates' href='#statvar_Ssl_accept_renegotiates'>Ssl_accept_renegotiates</a>  
建立连接时需要的协商的次数。

* <a name='statvar_Ssl_accepts' href='#statvar_Ssl_accepts'>Ssl_accepts</a>  
接受了的SSL连接数。

* <a name='statvar_Ssl_callback_cache_hits' href='#statvar_Ssl_callback_cache_hits'>Ssl_callback_cache_hits</a>  
SSL回调缓存命中的数量。

* <a name='statvar_Ssl_cipher' href='#statvar_Ssl_cipher'>Ssl_cipher</a>  
当前的SSL密文（非SSL连接为空）。

* <a name='statvar_Ssl_cipher_list' href='#statvar_Ssl_cipher_list'>Ssl_cipher_list</a>  
可能的SSL密码列表。

* <a name='statvar_Ssl_client_connects' href='#statvar_Ssl_client_connects'>Ssl_client_connects</a>  
尝试连接一个启用SSL主库的连接数。

* <a name='statvar_Ssl_connect_renegotiates' href='#statvar_Ssl_connect_renegotiates'>Ssl_connect_renegotiates</a>  
建立一个启用SSL主库连接所需要的协商的次数。

* <a name='statvar_Ssl_ctx_verify_depth' href='#statvar_Ssl_ctx_verify_depth'>Ssl_ctx_verify_depth</a>  
SSL上下文验证深度（即多少个链上的证书被测试）。

* <a name='statvar_Ssl_ctx_verify_mode' href='#statvar_Ssl_ctx_verify_mode'>Ssl_ctx_verify_mode</a>  
SSL上下文验证模式

* <a name='statvar_Ssl_default_timeout' href='#statvar_Ssl_default_timeout'>Ssl_default_timeout</a>  
默认的SSL超时时间。

* <a name='statvar_Ssl_finished_accepts' href='#statvar_Ssl_finished_accepts'>Ssl_finished_accepts</a>  
成功连接到服务器的SSL连接数。

* <a name='statvar_Ssl_finished_connects' href='#statvar_Ssl_finished_connects'>Ssl_finished_connects</a>  
成功连到启用SSL主库的从库连接数。

* <a name='statvar_Ssl_server_not_after' href='#statvar_Ssl_server_not_after'>Ssl_server_not_after</a>  
SSL证书过期时间。这个变量在MySQL 5.6.3中被加入。

* <a name='statvar_Ssl_server_not_before' href='#statvar_Ssl_server_not_before'>Ssl_server_not_before</a>  
SSL证书有效的起始时间。这个变量在MySQL 5.6.3中被加入。

* <a name='statvar_Ssl_session_cache_hits' href='#statvar_Ssl_session_cache_hits'>Ssl_session_cache_hits</a>  
SSL会话缓存命中次数。

* <a name='statvar_Ssl_session_cache_misses' href='#statvar_Ssl_session_cache_misses'>Ssl_session_cache_misses</a>  
SSL会话缓存未命中次数。

* <a name='statvar_Ssl_session_cache_mode' href='#statvar_Ssl_session_cache_mode'>Ssl_session_cache_mode</a>  
SSL会话缓存模式。

* <a name='statvar_Ssl_session_cache_overflows' href='#statvar_Ssl_session_cache_overflows'>Ssl_session_cache_overflows</a>  
SSL会话缓存溢出次数。

* <a name='statvar_Ssl_session_cache_size' href='#statvar_Ssl_session_cache_size'>Ssl_session_cache_size</a>  
SSL会话缓存大小。

* <a name='statvar_Ssl_session_cache_timeouts' href='#statvar_Ssl_session_cache_timeouts'>Ssl_session_cache_timeouts</a>  
SSL会话缓存超时次数。

* <a name='statvar_Ssl_session_reused' href='#statvar_Ssl_session_reused'>Ssl_session_reused</a>  
缓存中有多少个SSL连接被复用。

* <a name='statvar_Ssl_used_session_cache_entries' href='#statvar_Ssl_used_session_cache_entries'>Ssl_used_session_cache_entries</a>  
多少个SSL会话缓存实体被使用。

* <a name='statvar_Ssl_verify_depth' href='#statvar_Ssl_verify_depth'>Ssl_verify_depth</a>  
复制SSL连接的验深度。

* <a name='statvar_Ssl_verify_mode' href='#statvar_Ssl_verify_mode'>Ssl_verify_mode</a>  
复制SSL连接验证模式。

* <a name='statvar_Ssl_version' href='#statvar_Ssl_version'>Ssl_version</a>  
连接的SSL协议版本。

* <a name='statvar_Table_locks_immediate' href='#statvar_Table_locks_immediate'>Table_locks_immediate</a>  
立即获得表锁的请求的次数。

* <a name='statvar_Table_locks_waited' href='#statvar_Table_locks_waited'>Table_locks_waited</a>  
不能立即获得表锁且需要等待的请求的次数。如果这个值较高，你可能遇上了性能问题，你应该首先优化你的查询，然后拆分你的表或使用复制。

* <a name='statvar_Table_open_cache_hits' href='#statvar_Table_open_cache_hits'>Table_open_cache_hits</a>  
在打开表缓存中查询的命中次数。这个变量在MySQL 5.6.6中被加入。

* <a name='statvar_Table_open_cache_misses' href='#statvar_Table_open_cache_misses'>Table_open_cache_misses</a>  
在打开表缓存中查询的未命中次数。这个变量在MySQL 5.6.6中被加入。

* <a name='statvar_Table_open_cache_overflows' href='#statvar_Table_open_cache_overflows'>Table_open_cache_overflows</a>  
打开表缓存溢数。这是当一个表打开或关闭后，缓存实例中有一个未使用的实体，它的大小比[table_open_cache]/[table_open_cache_instances]大的次数。这个变量在MySQL 5.6.6中加入。

* <a name='statvar_Tc_log_max_pages_used' href='#statvar_Tc_log_max_pages_used'>Tc_log_max_pages_used</a>  
对于mysqld所使用的内存映射实现的日志，当它被当成一个内部分布式事务恢复的事务协调器时，这个变量表示服务器启动以来的该日志所用的最大的页数。如果[Tc_log_max_page_used]和[Tc_log_page_size]的乘积总是小于该日志大小，那这个值就是大于所需，可以考虑降低它。（这个值用[--log-tc-size]选项来设置。）目前这个值是没啥用的：基于二进制日志的恢复用不上它，内存映射恢复的日志方法用不上，除非实现了两段式提交的存储引擎数大于1。（`InnoDB`是唯一支持的引擎。）

* <a name='statvar_Tc_log_page_size' href='#statvar_Tc_log_page_size'>Tc_log_page_size</a>  
内存映射实现分布式恢复日志所使用的页大小。默认值可以用`getpagesize()`来确定。目前，因为和上面介绍的[Tc_log_max_page_used]一样的原因，这个值没啥毛用。

* <a name='statvar_Tc_log_page_waits' href='#statvar_Tc_log_page_waits'>Tc_log_page_waits</a>  
对于内存映射实现分布式恢复日志，每次服务器不能提交一个事务不得不等待日志中一个空闲的页是，这个值会增加。如果这个值较大，你可能要增加日志大小（用[--log-tc-size]选项）。对于基于二进制日志的恢复，当二进制日志因程序中有两段式提交而不能提交时，这个值会增加。（关闭操作要一直等到像这样的事务全部关闭为止。）

* <a name='statvar_Threads_cached' href='#statvar_Threads_cached'>Threads_cached</a>  
线程缓存中的线程数。

* <a name='statvar_Threads_connected' href='#statvar_Threads_connected'>Threads_connected</a>  
当然打开的线程数。

* <a name='statvar_Threads_created' href='#statvar_Threads_created'>Threads_created</a>  
创建了的用来处理连接的线程数。如果[Threads_created]值较大，你可能要增大[thread_cache_size]值，缓存命中率可以用[Threads_created]/[Connections]来计算。

* <a name='statvar_Threads_running' href='#statvar_Threads_running'>Threads_running</a>  
非睡眠状态的线程数。

* <a name='statvar_Uptime' href='#statvar_Uptime'>Uptime</a>  
服务器运行的总秒数。

* <a name='statvar_Uptime_since_flush_status' href='#statvar_Uptime_since_flush_status'>Uptime_since_flush_status</a>  
从上次执行`FLUSH STATUS`到现在的总秒数。

[SHOW_STATUS]: ../Chapter_13/13.07.05_SHOW_Syntax.md#13.07.05.36
[FLUSH_STATUS]: ../Chapter_13.07.06_Other_Administrative_Statements.md#13.07.06.03

[mysql_cluster]: ../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#17.03.04.04
[Connection_errors_xxx]: http://dev.mysql.com/doc/refman/5.6/en/server-status-variables×.html#statvar_Connection_errors_xxx
[host_cache]: http://dev.mysql.com/doc/refman/5.6/en/host-cache-table.html
[binlog_cache_size]: http://dev.mysql.com/doc/refman/5.6/en/replication-options-binary-log.html#sysvar_binlog_cache_size
[Binlog_stmt_cache_disk_use]: http://dev.mysql.com/doc/refman/5.6/en/server-status-variables.html#statvar_Binlog_stmt_cache_disk_use
[delete]: http://dev.mysql.com/doc/refman/5.6/en/delete.html
[update]: http://dev.mysql.com/doc/refman/5.6/en/update.html
[statvar_Qcache_hits]: http://dev.mysql.com/doc/refman/5.6/en/server-status-variables.html#statvar_Qcache_hits
[query-cache-status-and-maintenance]: http://dev.mysql.com/doc/refman/5.6/en/query-cache-status-and-maintenance.html
[buffer_pool]: ../glossary.md#glos_buffer_pool
[pages]: ../glossary.md#glos_pages
[row_lock]: .