变量名 | 变量类型 | 变量范围
-------|-------|:-------:
[audit_log_flush](../Chapter_06/06.03.11_MySQL_Enterprise_Audit_Log_Plugin.md#sysvar_audit_log_flush) | boolean | `GLOBAL`
[audit_log_policy](../Chapter_06/06.03.11_MySQL_Enterprise_Audit_Log_Plugin.md#sysvar_audit_log_policy) | enumeration | `GLOBAL`
[audit_log_rotate_on_size](../Chapter_06/06.03.11_MySQL_Enterprise_Audit_Log_Plugin.md#sysvar_audit_log_rotate_on_size) | numeric | `GLOBAL`
[auto_increment_increment](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_auto_increment_increment) | numeric | `GLOBAL` ¦ `SESSION`
[auto_increment_offset](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_auto_increment_offset) | numeric | `GLOBAL` ¦ `SESSION`
[autocommit](#sysvar_autocommit) | boolean | `GLOBAL` ¦ `SESSION`
[automatic_sp_privileges](#sysvar_automatic_sp_privileges) | boolean | `GLOBAL`
[big_tables](./05.01.03_Server_Command_Options.md#option_mysqld_big-tables) | boolean | `GLOBAL` ¦ `SESSION`
[binlog_cache_size](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_binlog_cache_size) | numeric | `GLOBAL`
[binlog_checksum](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_binlog_checksum) | string | `GLOBAL`
[binlog_direct_non_transactional_updates](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_binlog_direct_non_transactional_updates) | boolean | `GLOBAL` ¦ `SESSION`
[binlog_format](./05.01.03_Server_Command_Options.md#option_mysqld_binlog-format) | enumeration | `GLOBAL` ¦ `SESSION`
[binlog_max_flush_queue_time](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_binlog_max_flush_queue_time) | numeric | `GLOBAL`
[binlog_order_commits](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_binlog_order_commits) | boolean | `GLOBAL`
[binlog_row_image=image_type](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_binlog_row_image) | enumeration | `GLOBAL` ¦ `SESSION`
[binlog_rows_query_log_events](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_binlog_rows_query_log_events) | boolean | `GLOBAL` ¦ `SESSION`
[binlog_stmt_cache_size](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_binlog_stmt_cache_size) | numeric | `GLOBAL`
[bulk_insert_buffer_size](#sysvar_bulk_insert_buffer_size) | numeric | `GLOBAL` ¦ `SESSION`
[character_set_client](#sysvar_character_set_client) | string | `GLOBAL` ¦ `SESSION`
[character_set_connection](#sysvar_character_set_connection) | string | `GLOBAL` ¦ `SESSION`
[character_set_database](#sysvar_character_set_database) | string | `GLOBAL` ¦ `SESSION`
[character_set_filesystem](./05.01.03_Server_Command_Options.md#option_mysqld_character-set-filesystem) | string | `GLOBAL` ¦ `SESSION`
[character_set_results](#sysvar_character_set_results) | string | `GLOBAL` ¦ `SESSION`
[character_set_server](./05.01.03_Server_Command_Options.md#option_mysqld_character-set-server) | string | `GLOBAL` ¦ `SESSION`
[collation_connection](#sysvar_collation_connection) | string | `GLOBAL` ¦ `SESSION`
[collation_database](#sysvar_collation_database) | string | `GLOBAL` ¦ `SESSION`
[collation_server](./05.01.03_Server_Command_Options.md#option_mysqld_collation-server) | string | `GLOBAL` ¦ `SESSION`
[completion_type](#sysvar_completion_type) | numeric | `GLOBAL` ¦ `SESSION`
[concurrent_insert](#sysvar_concurrent_insert) | boolean | `GLOBAL`
[connect_timeout](#sysvar_connect_timeout) | numeric | `GLOBAL`
[debug](./05.01.03_Server_Command_Options.md#option_mysqld_debug) | string | `GLOBAL` ¦ `SESSION`
[debug_sync](#sysvar_debug_sync) | string | `SESSION`
[default_storage_engine](./05.01.03_Server_Command_Options.md#option_mysqld_default-storage-engine) | enumeration | `GLOBAL` ¦ `SESSION`
[default_tmp_storage_engine](#sysvar_default_tmp_storage_engine) | enumeration | `GLOBAL` ¦ `SESSION`
[default_week_format](#sysvar_default_week_format) | numeric | `GLOBAL` ¦ `SESSION`
[delay_key_write](./05.01.03_Server_Command_Options.md#option_mysqld_delay-key-write) | enumeration | `GLOBAL`
[delayed_insert_limit](#sysvar_delayed_insert_limit) | numeric | `GLOBAL`
[delayed_insert_timeout](#sysvar_delayed_insert_timeout) | numeric | `GLOBAL`
[delayed_queue_size](#sysvar_delayed_queue_size) | numeric | `GLOBAL`
[div_precision_increment](#sysvar_div_precision_increment) | numeric | `GLOBAL` ¦ `SESSION`
[end_markers_in_json](#sysvar_end_markers_in_json) | boolean | `GLOBAL` ¦ `SESSION`
[engine_condition_pushdown](./05.01.03_Server_Command_Options.md#option_mysqld_engine-condition-pushdown) | boolean | `GLOBAL` ¦ `SESSION`
[eq_range_index_dive_limit](#sysvar_eq_range_index_dive_limit) | numeric | `GLOBAL` ¦ `SESSION`
[event_scheduler](./05.01.03_Server_Command_Options.md#option_mysqld_event-scheduler) | enumeration | `GLOBAL`
[expire_logs_days](#sysvar_expire_logs_days) | numeric | `GLOBAL`
[flush](#sysvar_flush) | boolean | `GLOBAL`
[flush_time](#sysvar_flush_time) | numeric | `GLOBAL`
[foreign_key_checks](#sysvar_foreign_key_checks) | boolean | `GLOBAL` ¦ `SESSION`
[ft_boolean_syntax](#sysvar_ft_boolean_syntax) | string | `GLOBAL`
[general_log](./05.01.03_Server_Command_Options.md#option_mysqld_general-log) | boolean | `GLOBAL`
[general_log_file](#sysvar_general_log_file) | filename | `GLOBAL`
[group_concat_max_len](#sysvar_group_concat_max_len) | numeric | `GLOBAL` ¦ `SESSION`
[gtid_next](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_gtid_next) | enumeration | `SESSION`
[gtid_purged](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_gtid_purged) | string | `GLOBAL`
[host_cache_size](#sysvar_host_cache_size) | numeric | `GLOBAL`
[identity](#sysvar_identity) | numeric | `SESSION`
[init_connect](#sysvar_init_connect) | string | `GLOBAL`
[init_slave](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_init_slave) | string | `GLOBAL`
[innodb_adaptive_flushing](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_adaptive_flushing) | boolean | `GLOBAL`
[innodb_adaptive_flushing_lwm](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_adaptive_flushing_lwm) | numeric | `GLOBAL`
[innodb_adaptive_hash_index](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_adaptive_hash_index) | boolean | `GLOBAL`
[innodb_adaptive_max_sleep_delay](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_adaptive_max_sleep_delay) | numeric | `GLOBAL`
[innodb_api_bk_commit_interval](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_api_bk_commit_interval) | numeric | `GLOBAL`
[innodb_api_trx_level](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_api_trx_level) | numeric | `GLOBAL`
[innodb_autoextend_increment](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_autoextend_increment) | numeric | `GLOBAL`
[innodb_buffer_pool_dump_at_shutdown](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_buffer_pool_dump_at_shutdown) | boolean | `GLOBAL`
[innodb_buffer_pool_dump_now](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_buffer_pool_dump_now) | boolean | `GLOBAL`
[innodb_buffer_pool_filename](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_buffer_pool_filename) | string | `GLOBAL`
[innodb_buffer_pool_load_abort](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_buffer_pool_load_abort) | boolean | `GLOBAL`
[innodb_buffer_pool_load_now](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_buffer_pool_load_now) | boolean | `GLOBAL`
[innodb_change_buffer_max_size](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_change_buffer_max_size) | numeric | `GLOBAL`
[innodb_change_buffering](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_change_buffering) | enumeration | `GLOBAL`
[innodb_checksum_algorithm](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_checksum_algorithm) | enumeration | `GLOBAL`
[innodb_cmp_per_index_enabled](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_cmp_per_index_enabled) | boolean | `GLOBAL`
[innodb_commit_concurrency](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_commit_concurrency) | numeric | `GLOBAL`
[innodb_compression_failure_threshold_pct](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_compression_failure_threshold_pct) | numeric | `GLOBAL`
[innodb_compression_level](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_compression_level) | numeric | `GLOBAL`
[innodb_compression_pad_pct_max](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_compression_pad_pct_max) | numeric | `GLOBAL`
[innodb_concurrency_tickets](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_concurrency_tickets) | numeric | `GLOBAL`
[innodb_disable_sort_file_cache](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_disable_sort_file_cache) | boolean | `GLOBAL`
[innodb_fast_shutdown](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_fast_shutdown) | numeric | `GLOBAL`
[innodb_file_format](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_file_format) | string | `GLOBAL`
[innodb_file_format_max](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_file_format_max) | string | `GLOBAL`
[innodb_file_per_table](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_file_per_table) | boolean | `GLOBAL`
[innodb_flush_log_at_timeout](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_flush_log_at_timeout) | numeric | `GLOBAL`
[innodb_flush_log_at_trx_commit](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_flush_log_at_trx_commit) | enumeration | `GLOBAL`
[innodb_flush_neighbors](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_flush_neighbors) | enumeration | `GLOBAL`
[innodb_flushing_avg_loops](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_flushing_avg_loops) | numeric | `GLOBAL`
[innodb_ft_aux_table](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_ft_aux_table) | string | `GLOBAL`
[innodb_ft_enable_diag_print](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_ft_enable_diag_print) | boolean | `GLOBAL`
[innodb_ft_enable_stopword](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_ft_enable_stopword) | boolean | `GLOBAL`
[innodb_ft_num_word_optimize](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_ft_num_word_optimize) | numeric | `GLOBAL`
[innodb_ft_server_stopword_table](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_ft_server_stopword_table) | string | `GLOBAL`
[innodb_ft_user_stopword_table](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_ft_user_stopword_table) | string | `GLOBAL` ¦ `SESSION`
[innodb_io_capacity](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_io_capacity) | numeric | `GLOBAL`
[innodb_io_capacity_max](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_io_capacity_max) | numeric | `GLOBAL`
[innodb_large_prefix](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_large_prefix) | boolean | `GLOBAL`
[innodb_lock_wait_timeout](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_lock_wait_timeout) | numeric | `GLOBAL` ¦ `SESSION`
[innodb_log_compressed_pages](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_log_compressed_pages) | boolean | `GLOBAL`
[innodb_lru_scan_depth](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_lru_scan_depth) | numeric | `GLOBAL`
[innodb_max_dirty_pages_pct](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_max_dirty_pages_pct) | numeric | `GLOBAL`
[innodb_max_dirty_pages_pct_lwm](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_max_dirty_pages_pct_lwm) | numeric | `GLOBAL`
[innodb_max_purge_lag](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_max_purge_lag) | numeric | `GLOBAL`
[innodb_max_purge_lag_delay](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_max_purge_lag_delay) | numeric | `GLOBAL`
[innodb_monitor_disable](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_monitor_disable) | string | `GLOBAL`
[innodb_monitor_enable](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_monitor_enable) | string | `GLOBAL`
[innodb_monitor_reset](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_monitor_reset) | string | `GLOBAL`
[innodb_monitor_reset_all](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_monitor_reset_all) | string | `GLOBAL`
[innodb_old_blocks_pct](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_old_blocks_pct) | numeric | `GLOBAL`
[innodb_old_blocks_time](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_old_blocks_time) | numeric | `GLOBAL`
[innodb_online_alter_log_max_size](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_online_alter_log_max_size) | numeric | `GLOBAL`
[innodb_optimize_fulltext_only](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_optimize_fulltext_only) | boolean | `GLOBAL`
[innodb_print_all_deadlocks](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_print_all_deadlocks) | boolean | `GLOBAL`
[innodb_purge_batch_size](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_purge_batch_size) | numeric | `GLOBAL`
[innodb_random_read_ahead](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_random_read_ahead) | boolean | `GLOBAL`
[innodb_read_ahead_threshold](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_read_ahead_threshold) | numeric | `GLOBAL`
[innodb_replication_delay](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_replication_delay) | numeric | `GLOBAL`
[innodb_rollback_segments](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_rollback_segments) | numeric | `GLOBAL`
[innodb_spin_wait_delay](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_spin_wait_delay) | numeric | `GLOBAL`
[innodb_stats_auto_recalc](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_stats_auto_recalc) | boolean | `GLOBAL`
[innodb_stats_method](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_stats_method) | enumeration | `GLOBAL`
[innodb_stats_on_metadata](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_stats_on_metadata) | boolean | `GLOBAL`
[innodb_stats_persistent](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_stats_persistent) | boolean | `GLOBAL`
[innodb_stats_persistent_sample_pages](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_stats_persistent_sample_pages) | numeric | `GLOBAL`
[innodb_stats_sample_pages](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_stats_sample_pages) | numeric | `GLOBAL`
[innodb_stats_transient_sample_pages](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_stats_transient_sample_pages) | numeric | `GLOBAL`
[innodb_strict_mode](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_strict_mode) | boolean | `GLOBAL` ¦ `SESSION`
[innodb_support_xa](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_support_xa) | boolean | `GLOBAL` ¦ `SESSION`
[innodb_sync_spin_loops](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_sync_spin_loops) | numeric | `GLOBAL`
[innodb_table_locks](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_table_locks) | boolean | `GLOBAL` ¦ `SESSION`
[innodb_thread_concurrency](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_thread_concurrency) | numeric | `GLOBAL`
[innodb_thread_sleep_delay](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_thread_sleep_delay) | numeric | `GLOBAL`
[innodb_undo_logs](../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md#sysvar_innodb_undo_logs) | numeric | `GLOBAL`
[insert_id](#sysvar_insert_id) | numeric | `SESSION`
[interactive_timeout](#sysvar_interactive_timeout) | numeric | `GLOBAL` ¦ `SESSION`
[join_buffer_size](#sysvar_join_buffer_size) | numeric | `GLOBAL` ¦ `SESSION`
[keep_files_on_create](#sysvar_keep_files_on_create) | boolean | `GLOBAL` ¦ `SESSION`
[key_buffer_size](#sysvar_key_buffer_size) | numeric | `GLOBAL`
[key_cache_age_threshold](#sysvar_key_cache_age_threshold) | numeric | `GLOBAL`
[key_cache_block_size](#sysvar_key_cache_block_size) | numeric | `GLOBAL`
[key_cache_division_limit](#sysvar_key_cache_division_limit) | numeric | `GLOBAL`
[last_insert_id](#sysvar_last_insert_id) | numeric | `SESSION`
[lc_messages](./05.01.03_Server_Command_Options.md#option_mysqld_lc-messages) | string | `GLOBAL` ¦ `SESSION`
[lc_time_names](#sysvar_lc_time_names) | string | `GLOBAL` ¦ `SESSION`
[local_infile](#sysvar_local_infile) | boolean | `GLOBAL`
[lock_wait_timeout](#sysvar_lock_wait_timeout) | numeric | `GLOBAL` ¦ `SESSION`
[log](./05.01.03_Server_Command_Options.md#option_mysqld_log) | string | `GLOBAL`
[log_output](./05.01.03_Server_Command_Options.md#option_mysqld_log-output) | set | `GLOBAL`
[log_queries_not_using_indexes](./05.01.03_Server_Command_Options.md#option_mysqld_log-queries-not-using-indexes) | boolean | `GLOBAL`
[log_slow_admin_statements](#sysvar_log_slow_admin_statements) | boolean | `GLOBAL`
[log_slow_queries](./05.01.03_Server_Command_Options.md#option_mysqld_log-slow-queries) | boolean | `GLOBAL`
[log_slow_slave_statements](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_log_slow_slave_statements) | boolean | `GLOBAL`
[log_throttle_queries_not_using_indexes](#sysvar_log_throttle_queries_not_using_indexes) | numeric | `GLOBAL`
[log_warnings](./05.01.03_Server_Command_Options.md#option_mysqld_log-warnings) | numeric | `GLOBAL`
[long_query_time](#sysvar_long_query_time) | numeric | `GLOBAL` ¦ `SESSION`
[low_priority_updates](./05.01.03_Server_Command_Options.md#option_mysqld_low-priority-updates) | boolean | `GLOBAL` ¦ `SESSION`
[master_info_repository](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_master_info_repository) | string | `GLOBAL`
[master_verify_checksum](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_master_verify_checksum) | boolean | `GLOBAL`
[max_allowed_packet](#sysvar_max_allowed_packet) | numeric | `GLOBAL`
[max_binlog_cache_size](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_max_binlog_cache_size) | numeric | `GLOBAL`
[max_binlog_size](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_max_binlog_size) | numeric | `GLOBAL`
[max_binlog_stmt_cache_size](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_max_binlog_stmt_cache_size) | numeric | `GLOBAL`
[max_connect_errors](#sysvar_max_connect_errors) | numeric | `GLOBAL`
[max_connections](#sysvar_max_connections) | numeric | `GLOBAL`
[max_delayed_threads](#sysvar_max_delayed_threads) | numeric | `GLOBAL` ¦ `SESSION`
[max_error_count](#sysvar_max_error_count) | numeric | `GLOBAL` ¦ `SESSION`
[max_heap_table_size](#sysvar_max_heap_table_size) | numeric | `GLOBAL` ¦ `SESSION`
[max_insert_delayed_threads](#sysvar_max_insert_delayed_threads) | numeric | `GLOBAL` ¦ `SESSION`
[max_join_size](#sysvar_max_join_size) | numeric | `GLOBAL` ¦ `SESSION`
[max_length_for_sort_data](#sysvar_max_length_for_sort_data) | numeric | `GLOBAL` ¦ `SESSION`
[max_prepared_stmt_count](#sysvar_max_prepared_stmt_count) | numeric | `GLOBAL`
[max_relay_log_size](#sysvar_max_relay_log_size) | numeric | `GLOBAL`
[max_seeks_for_key](#sysvar_max_seeks_for_key) | numeric | `GLOBAL` ¦ `SESSION`
[max_sort_length](#sysvar_max_sort_length) | numeric | `GLOBAL` ¦ `SESSION`
[max_sp_recursion_depth](#sysvar_max_sp_recursion_depth) | numeric | `GLOBAL` ¦ `SESSION`
[max_user_connections](#sysvar_max_user_connections) | numeric | `GLOBAL` ¦ `SESSION`
[max_write_lock_count](#sysvar_max_write_lock_count) | numeric | `GLOBAL`
[min_examined_row_limit](./05.01.03_Server_Command_Options.md#option_mysqld_min-examined-row-limit) | numeric | `GLOBAL` ¦ `SESSION`
[myisam_data_pointer_size](#sysvar_myisam_data_pointer_size) | numeric | `GLOBAL`
[myisam_max_sort_file_size](#sysvar_myisam_max_sort_file_size) | numeric | `GLOBAL`
[myisam_repair_threads](#sysvar_myisam_repair_threads) | numeric | `GLOBAL` ¦ `SESSION`
[myisam_sort_buffer_size](#sysvar_myisam_sort_buffer_size) | numeric | `GLOBAL` ¦ `SESSION`
[myisam_stats_method](#sysvar_myisam_stats_method) | enumeration | `GLOBAL` ¦ `SESSION`
[myisam_use_mmap](#sysvar_myisam_use_mmap) | boolean | `GLOBAL`
[ndb_autoincrement_prefetch_sz](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_autoincrement_prefetch_sz) | numeric | `GLOBAL` ¦ `SESSION`
[ndb_blob_read_batch_bytes](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#option_mysqld_ndb-blob-read-batch-bytes) | numeric | `GLOBAL` ¦ `SESSION`
[ndb_blob_write_batch_bytes](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#option_mysqld_ndb-blob-write-batch-bytes) | numeric | `GLOBAL` ¦ `SESSION`
[ndb_cache_check_time](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_cache_check_time) | numeric | `GLOBAL`
[ndb_deferred_constraints](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#option_mysqld_ndb-deferred-constraints) | integer | `GLOBAL` ¦ `SESSION`
[ndb_deferred_constraints](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_deferred_constraints) | integer | `GLOBAL` ¦ `SESSION`
[ndb_distribution={KEYHASH¦LINHASH}](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_distribution) | enumeration | `GLOBAL`
[ndb_distribution](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#option_mysqld_ndb-distribution) | enumeration | `GLOBAL`
[ndb_extra_logging](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_extra_logging) | numeric | `GLOBAL`
[ndb_force_send](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_force_send) | boolean | `GLOBAL` ¦ `SESSION`
[ndb_log_bin](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_log_bin) | boolean | `GLOBAL` ¦ `SESSION`
[ndb_log_binlog_index](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_log_binlog_index) | boolean | `GLOBAL`
[ndb_log_empty_epochs](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_log_empty_epochs) | boolean | `GLOBAL`
[ndb_log_empty_epochs](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#option_mysqld_ndb-log-empty-epochs) | boolean | `GLOBAL`
[ndb_log_update_as_write](../Chapter_17/17.06.11_MySQL_Cluster_Replication_Conflict_Resolution.md#option_mysqld_ndb-log-update-as-write) | boolean | `GLOBAL`
[ndb_log_updated_only](../Chapter_17/17.06.11_MySQL_Cluster_Replication_Conflict_Resolution.md#option_mysqld_ndb-log-updated-only) | boolean | `GLOBAL`
[ndb_optimization_delay](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#option_mysqld_ndb_optimization_delay) | numeric | `GLOBAL`
[ndb_recv_thread_cpu_mask](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_recv_thread_cpu_mask) | bitmap | `GLOBAL`
[ndb_table_no_logging](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_table_no_logging) | boolean | `SESSION`
[ndb_table_temporary](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_table_temporary) | boolean | `SESSION`
[ndb_use_exact_count](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_use_exact_count) | boolean | `GLOBAL` ¦ `SESSION`
[ndb_use_transactions](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndb_use_transactions) | boolean | `GLOBAL` ¦ `SESSION`
[ndbinfo_max_bytes](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndbinfo_max_bytes) | numeric | `GLOBAL` ¦ `SESSION`
[ndbinfo_max_rows](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndbinfo_max_rows) | numeric | `GLOBAL` ¦ `SESSION`
[ndbinfo_show_hidden](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndbinfo_show_hidden) | boolean | `GLOBAL` ¦ `SESSION`
[ndbinfo_table_prefix](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_ndbinfo_table_prefix) | string | `GLOBAL` ¦ `SESSION`
[net_buffer_length](#sysvar_net_buffer_length) | numeric | `GLOBAL` ¦ `SESSION`
[net_read_timeout](#sysvar_net_read_timeout) | numeric | `GLOBAL` ¦ `SESSION`
[net_retry_count](#sysvar_net_retry_count) | numeric | `GLOBAL` ¦ `SESSION`
[net_write_timeout](#sysvar_net_write_timeout) | numeric | `GLOBAL` ¦ `SESSION`
[new](#sysvar_new) | boolean | `GLOBAL` ¦ `SESSION`
[old_alter_table](./05.01.03_Server_Command_Options.md#option_mysqld_old-alter-table) | boolean | `GLOBAL` ¦ `SESSION`
[old_passwords](#sysvar_old_passwords) | boolean | `GLOBAL` ¦ `SESSION`
[optimizer_join_cache_level](#sysvar_optimizer_join_cache_level) | numeric | `GLOBAL` ¦ `SESSION`
[optimizer_prune_level](#sysvar_optimizer_prune_level) | boolean | `GLOBAL` ¦ `SESSION`
[optimizer_search_depth](#sysvar_optimizer_search_depth) | numeric | `GLOBAL` ¦ `SESSION`
[optimizer_switch](#sysvar_optimizer_switch) | set | `GLOBAL` ¦ `SESSION`
[optimizer_trace](#sysvar_optimizer_trace) | string | `GLOBAL` ¦ `SESSION`
[optimizer_trace_features](#sysvar_optimizer_trace_features) | string | `GLOBAL` ¦ `SESSION`
[optimizer_trace_limit](#sysvar_optimizer_trace_limit) | numeric | `GLOBAL` ¦ `SESSION`
[optimizer_trace_max_mem_size](#sysvar_optimizer_trace_max_mem_size) | numeric | `GLOBAL` ¦ `SESSION`
[optimizer_trace_offset](#sysvar_optimizer_trace_offset) | numeric | `GLOBAL` ¦ `SESSION`
[preload_buffer_size](#sysvar_preload_buffer_size) | numeric | `GLOBAL` ¦ `SESSION`
[profiling](#sysvar_profiling) | boolean | `GLOBAL` ¦ `SESSION`
[profiling_history_size](#sysvar_profiling_history_size) | numeric | `GLOBAL` ¦ `SESSION`
[pseudo_slave_mode](#sysvar_pseudo_slave_mode) | numeric | `SESSION`
[pseudo_thread_id](#sysvar_pseudo_thread_id) | numeric | `SESSION`
[query_alloc_block_size](#sysvar_query_alloc_block_size) | numeric | `GLOBAL` ¦ `SESSION`
[query_cache_limit](#sysvar_query_cache_limit) | numeric | `GLOBAL`
[query_cache_min_res_unit](#sysvar_query_cache_min_res_unit) | numeric | `GLOBAL`
[query_cache_size](#sysvar_query_cache_size) | numeric | `GLOBAL`
[query_cache_type](#sysvar_query_cache_type) | enumeration | `GLOBAL` ¦ `SESSION`
[query_cache_wlock_invalidate](#sysvar_query_cache_wlock_invalidate) | boolean | `GLOBAL` ¦ `SESSION`
[query_prealloc_size](#sysvar_query_prealloc_size) | numeric | `GLOBAL` ¦ `SESSION`
[rand_seed1](#sysvar_rand_seed1) | numeric | `SESSION`
[rand_seed2](#sysvar_rand_seed2) | numeric | `SESSION`
[range_alloc_block_size](#sysvar_range_alloc_block_size) | numeric | `GLOBAL` ¦ `SESSION`
[read_buffer_size](#sysvar_read_buffer_size) | numeric | `GLOBAL` ¦ `SESSION`
[read_only](#sysvar_read_only) | boolean | `GLOBAL`
[read_rnd_buffer_size](#sysvar_read_rnd_buffer_size) | numeric | `GLOBAL` ¦ `SESSION`
[relay_log_info_repository](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_relay_log_info_repository) | string | `GLOBAL`
[relay_log_purge](#sysvar_relay_log_purge) | boolean | `GLOBAL`
[relay_log_recovery](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_relay_log_recovery) | boolean | `GLOBAL`
[rpl_semi_sync_master_enabled](#sysvar_rpl_semi_sync_master_enabled) | boolean | `GLOBAL`
[rpl_semi_sync_master_timeout](#sysvar_rpl_semi_sync_master_timeout) | numeric | `GLOBAL`
[rpl_semi_sync_master_trace_level](#sysvar_rpl_semi_sync_master_trace_level) | numeric | `GLOBAL`
[rpl_semi_sync_master_wait_no_slave](#sysvar_rpl_semi_sync_master_wait_no_slave) | boolean | `GLOBAL`
[rpl_semi_sync_slave_enabled](#sysvar_rpl_semi_sync_slave_enabled) | boolean | `GLOBAL`
[rpl_semi_sync_slave_trace_level](#sysvar_rpl_semi_sync_slave_trace_level) | numeric | `GLOBAL`
[rpl_stop_slave_timeout](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_rpl_stop_slave_timeout) | integer | `GLOBAL`
[secure_auth](./05.01.03_Server_Command_Options.md#option_mysqld_secure-auth) | boolean | `GLOBAL`
[server_id](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#option_mysqld_server-id) | numeric | `GLOBAL`
[slave_allow_batching](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_allow_batching) | boolean | `GLOBAL`
[slave_checkpoint_group=#](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_checkpoint_group) | numeric | `GLOBAL`
[slave_checkpoint_period=#](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_checkpoint_period) | numeric | `GLOBAL`
[slave_compressed_protocol](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_compressed_protocol) | boolean | `GLOBAL`
[slave_exec_mode](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_exec_mode) | enumeration | `GLOBAL`
[slave_max_allowed_packet](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_max_allowed_packet) | numeric | `GLOBAL`
[slave_net_timeout](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#option_mysqld_slave-net-timeout) | numeric | `GLOBAL`
[slave_parallel_workers](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_parallel_workers) | numeric | `GLOBAL`
[slave_pending_jobs_size_max](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_pending_jobs_size_max) | numeric | `GLOBAL`
[slave_rows_search_algorithms=list](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_rows_search_algorithms) | set | `GLOBAL`
[slave_sql_verify_checksum](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_sql_verify_checksum) | boolean | `GLOBAL`
[slave_transaction_retries](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_slave_transaction_retries) | numeric | `GLOBAL`
[slow_launch_time](#sysvar_slow_launch_time) | numeric | `GLOBAL`
[slow_query_log](./05.01.03_Server_Command_Options.md#option_mysqld_slow-query-log) | boolean | `GLOBAL`
[slow_query_log_file](#sysvar_slow_query_log_file) | filename | `GLOBAL`
[sort_buffer_size](#sysvar_sort_buffer_size) | numeric | `GLOBAL` ¦ `SESSION`
[sql_auto_is_null](#sysvar_sql_auto_is_null) | boolean | `GLOBAL` ¦ `SESSION`
[sql_big_selects](#sysvar_sql_big_selects) | boolean | `GLOBAL` ¦ `SESSION`
[sql_big_tables](#sysvar_big_tables) | boolean | `GLOBAL` ¦ `SESSION`
[sql_buffer_result](#sysvar_sql_buffer_result) | boolean | `GLOBAL` ¦ `SESSION`
[sql_log_bin](#sysvar_sql_log_bin) | boolean | `GLOBAL` ¦ `SESSION`
[sql_log_off](#sysvar_sql_log_off) | boolean | `GLOBAL` ¦ `SESSION`
[sql_low_priority_updates](#sysvar_low_priority_updates) | boolean | `GLOBAL` ¦ `SESSION`
[sql_max_join_size](#sysvar_max_join_size) | numeric | `GLOBAL` ¦ `SESSION`
[sql_mode](./05.01.03_Server_Command_Options.md#option_mysqld_sql-mode) | set | `GLOBAL` ¦ `SESSION`
[sql_notes](#sysvar_sql_notes) | boolean | `GLOBAL` ¦ `SESSION`
[sql_quote_show_create](#sysvar_sql_quote_show_create) | boolean | `GLOBAL` ¦ `SESSION`
[sql_safe_updates](#sysvar_sql_safe_updates) | boolean | `GLOBAL` ¦ `SESSION`
[sql_select_limit](#sysvar_sql_select_limit) | numeric | `GLOBAL` ¦ `SESSION`
[sql_slave_skip_counter](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_sql_slave_skip_counter) | numeric | `GLOBAL`
[sql_warnings](#sysvar_sql_warnings) | boolean | `GLOBAL` ¦ `SESSION`
[storage_engine](#sysvar_storage_engine) | enumeration | `GLOBAL` ¦ `SESSION`
[stored_program_cache](#sysvar_stored_program_cache) | numeric | `GLOBAL`
[sync_binlog](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_sync_binlog) | numeric | `GLOBAL`
[sync_frm](#sysvar_sync_frm) | boolean | `GLOBAL`
[sync_master_info](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_sync_master_info) | numeric | `GLOBAL`
[sync_relay_log](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_sync_relay_log) | numeric | `GLOBAL`
[sync_relay_log_info](../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md#sysvar_sync_relay_log_info) | numeric | `GLOBAL`
[table_definition_cache](#sysvar_table_definition_cache) | numeric | `GLOBAL`
[table_open_cache](#sysvar_table_open_cache) | numeric | `GLOBAL`
[thread_cache_size](#sysvar_thread_cache_size) | numeric | `GLOBAL`
[thread_pool_high_priority_connection](#sysvar_thread_pool_high_priority_connection) | numeric | `GLOBAL` ¦ `SESSION`
[thread_pool_max_unused_threads](#sysvar_thread_pool_max_unused_threads) | numeric | `GLOBAL`
[thread_pool_prio_kickup_timer](#sysvar_thread_pool_prio_kickup_timer) | numeric | `GLOBAL` ¦ `SESSION`
[thread_pool_stall_limit](#sysvar_thread_pool_stall_limit) | numeric | `GLOBAL`
[time_zone](#sysvar_time_zone) | string | `GLOBAL` ¦ `SESSION`
[timed_mutexes](#sysvar_timed_mutexes) | boolean | `GLOBAL`
[timestamp](#sysvar_timestamp) | numeric | `SESSION`
[tmp_table_size](#sysvar_tmp_table_size) | numeric | `GLOBAL` ¦ `SESSION`
[transaction_alloc_block_size](#sysvar_transaction_alloc_block_size) | numeric | `GLOBAL` ¦ `SESSION`
[transaction_allow_batching](../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md#sysvar_transaction_allow_batching) | boolean | `SESSION`
[transaction_prealloc_size](#sysvar_transaction_prealloc_size) | numeric | `GLOBAL` ¦ `SESSION`
[tx_isolation](#sysvar_tx_isolation) | enumeration | `GLOBAL` ¦ `SESSION`
[tx_read_only](#sysvar_tx_read_only) | boolean | `GLOBAL` ¦ `SESSION`
[unique_checks](#sysvar_unique_checks) | boolean | `GLOBAL` ¦ `SESSION`
[updatable_views_with_limit](#sysvar_updatable_views_with_limit) | boolean | `GLOBAL` ¦ `SESSION`
[validate_password_length](../Chapter_06/06.01.02_Keeping_Passwords_Secure.md#sysvar_validate_password_length) | numeric | `GLOBAL`
[validate_password_mixed_case_count](../Chapter_06/06.01.02_Keeping_Passwords_Secure.md#sysvar_validate_password_mixed_case_count) | numeric | `GLOBAL`
[validate_password_number_count](../Chapter_06/06.01.02_Keeping_Passwords_Secure.md#sysvar_validate_password_number_count) | numeric | `GLOBAL`
[validate_password_policy](../Chapter_06/06.01.02_Keeping_Passwords_Secure.md#sysvar_validate_password_policy) | enumeration | `GLOBAL`
[validate_password_special_char_count](../Chapter_06/06.01.02_Keeping_Passwords_Secure.md#sysvar_validate_password_special_char_count) | numeric | `GLOBAL`
[wait_timeout](#sysvar_wait_timeout) | numeric | `GLOBAL` ¦ `SESSION`
