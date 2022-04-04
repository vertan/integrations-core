# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
METRIC_MAP = {
    # agency metrics
    'arangodb_agency_cache_callback_number': 'agency.cache.callback',
    'arangodb_agency_callback_number': 'agency.callback',
    'arangodb_agency_callback_registered_total': 'agency.callback.registered.total',
    'arangodb_agency_client_lookup_table_size': 'agency.client.lookup.table_size',
    'arangodb_agency_commit_hist': 'agency.commit',
    'arangodb_agency_compaction_hist': 'agency.compaction',
    'arangodb_agency_log_size_bytes': 'agency.log.size',
    'arangodb_agency_read_no_leader_total': 'agency.read.no_leader.total',
    'arangodb_agency_read_ok_total': 'agency.read.ok.total',
    'arangodb_agency_supervision_failed_server_total': 'agency.supervision.failed.server.total',
    'arangodb_agency_write_hist': 'agency.write',
    'arangodb_agency_write_no_leader_total': 'agency.write.no_leader.total',
    'arangodb_agency_write_ok_total': 'agency.write.ok.total',
    'arangodb_agencycomm_request_time_msec': 'agency.request.time',
    # network
    'arangodb_network_forwarded_requests_total': 'network.forwarded.requests.total',
    'arangodb_network_request_timeouts_total': 'network.request.timeouts.total',
    'arangodb_network_requests_in_flight': 'network.requests.in.flight',
    # aql
    'arangodb_aql_all_query_total': 'aql.all.query.total',
    'arangodb_aql_current_query': 'aql.current.query',
    'arangodb_aql_global_memory_limit': 'aql.global.memory.limit',
    'arangodb_aql_global_memory_usage': 'aql.global.memory.usage',
    'arangodb_aql_global_query_memory_limit_reached_total': 'aql.global.query.memory.limit.reached.total',
    'arangodb_aql_local_query_memory_limit_reached_total': 'aql.local.query.memory.limit.reached.total',
    'arangodb_aql_query_time': 'aql.query.time',
    'arangodb_aql_slow_query_time': 'aql.slow.query.time',
    # client connection
    'arangodb_client_connection_statistics_bytes_received': 'client.connection.bytes.received',
    'arangodb_client_connection_statistics_client_connections': 'client.connections',
    'arangodb_client_connection_statistics_connection_time': 'client.connection.time',
    'arangodb_client_connection_statistics_io_time': 'client.connection.io.time',
    'arangodb_client_connection_statistics_queue_time': 'client.connection.queue.time',
    'arangodb_client_connection_statistics_request_time': 'client.connection.request.time',
    'arangodb_client_connection_statistics_total_time': 'client.connection.total.time',
    # http
    'arangodb_http_request_statistics_async_requests_total': 'http.async.requests.total',
    'arangodb_http_request_statistics_http_delete_requests_total': 'http.delete.requests.total',
    'arangodb_http_request_statistics_http_get_requests_total': 'http.get.requests.total',
    'arangodb_http_request_statistics_http_head_requests_total': 'http.head.requests.total',
    'arangodb_http_request_statistics_http_options_requests_total': 'http.options.requests.total',
    'arangodb_http_request_statistics_http_patch_requests_total': 'http.patch.requests.total',
    'arangodb_http_request_statistics_http_post_requests_total': 'http.post.requests.total',
    'arangodb_http_request_statistics_http_put_requests_total': 'http.put.requests.total',
    'arangodb_http_request_statistics_other_http_requests_total': 'http.other.requests.total',
    'arangodb_http_request_statistics_total_requests_total': 'http.total.requests.total',
    'arangodb_http_request_statistics_user_requests_total': 'http.user.requests.total',
    # process
    'arangodb_process_statistics_major_page_faults_total': 'process.page.faults.major.total',
    'arangodb_process_statistics_minor_page_faults_total': 'process.page.faults.minor.total',
    'arangodb_process_statistics_number_of_threads': 'process.threads',
    'arangodb_process_statistics_resident_set_size': 'process.resident_set_size',
    'arangodb_process_statistics_system_time': 'process.system_time',
    'arangodb_process_statistics_user_time': 'process.user_time',
    'arangodb_process_statistics_virtual_memory_size': 'process.virtual_memory_size',
    # server stat
    'arangodb_server_statistics_cpu_cores': 'server.cpu_cores',
    'arangodb_server_statistics_idle_percent': 'server.idle_percent',
    'arangodb_server_statistics_iowait_percent': 'server.iowait_percent',
    'arangodb_server_statistics_physical_memory': 'server.physical_memory',
    'arangodb_server_statistics_system_percent': 'server.kernel_mode.percent',
    'arangodb_server_statistics_user_percent': 'server.user_mode.percent',
    # collection
    'arangodb_collection_lock_acquisition_micros_total': 'collection.lock.acquisition.total',
    'arangodb_collection_lock_sequential_mode_total': 'collection.lock.sequential_mode.total',
    'arangodb_collection_lock_timeouts_exclusive_total': 'collection.lock.timeouts_exclusive.total',
    'arangodb_collection_lock_timeouts_write_total': 'collection.lock.timeouts_write.total',
    # transaction
    'arangodb_read_transactions_total': 'transactions.read.total',
    'arangodb_transactions_aborted_total': 'transactions.aborted.total',
    'arangodb_transactions_committed_total': 'transactions.committed.total',
    'arangodb_transactions_expired_total': 'transactions.expired.total',
    'arangodb_transactions_started_total': 'transactions.started.total',
    # rocksDB
    'arangodb_collection_lock_acquisition_time': 'rocksdb.collection_lock.acquisition_time',
    'arangodb_rocksdb_write_stalls_total': 'rocksdb.write.stalls.total',
    'arangodb_rocksdb_write_stops_total': 'rocksdb.write.stops.total',
    'rocksdb_actual_delayed_write_rate': 'rocksdb.actual.delayed.write.rate',
    'rocksdb_archived_wal_files': 'rocksdb.archived.wal.files',
    'rocksdb_background_errors': 'rocksdb.background.errors',
    'rocksdb_base_level': 'rocksdb.base.level',
    'rocksdb_block_cache_capacity': 'rocksdb.block.cache.capacity',
    'rocksdb_block_cache_pinned_usage': 'rocksdb.block.cache.pinned.usage',
    'rocksdb_block_cache_usage': 'rocksdb.block.cache.usage',
    'rocksdb_cache_hit_rate_lifetime': 'rocksdb.cache.hit.rate.lifetime',
    'rocksdb_cache_limit': 'rocksdb.cache.limit',
    'rocksdb_compaction_pending': 'rocksdb.compaction.pending',
    'rocksdb_cur_size_active_mem_table': 'rocksdb.cur.size.active.mem.table',
    'rocksdb_cur_size_all_mem_tables': 'rocksdb.cur.size.all.mem.tables',
    'rocksdb_engine_throttle_bps': 'rocksdb.engine.throttle.bps',
    'rocksdb_estimate_live_data_size': 'rocksdb.estimate.live.data.size',
    'rocksdb_estimate_num_keys': 'rocksdb.estimate.num.keys',
    'rocksdb_estimate_pending_compaction_bytes': 'rocksdb.estimate.pending.compaction.bytes',
    'rocksdb_estimate_table_readers_mem': 'rocksdb.estimate.table.readers.mem',
    'rocksdb_free_disk_space': 'rocksdb.free.disk.space',
    'rocksdb_free_inodes': 'rocksdb.free.inodes',
    'rocksdb_live_sst_files_size': 'rocksdb.live.sst.files.size',
    'rocksdb_mem_table_flush_pending': 'rocksdb.mem.table.flush.pending',
    'rocksdb_min_log_number_to_keep': 'rocksdb.min.log.number.to.keep',
    'rocksdb_num_deletes_active_mem_table': 'rocksdb.num.deletes.active.mem.table',
    'rocksdb_num_deletes_imm_mem_tables': 'rocksdb.num.deletes.imm.mem.tables',
    'rocksdb_num_entries_active_mem_table': 'rocksdb.num.entries.active.mem.table',
    'rocksdb_num_entries_imm_mem_tables': 'rocksdb.num.entries.imm_mem.tables',
    'rocksdb_num_immutable_mem_table': 'rocksdb.num.immutable.mem.table',
    'rocksdb_num_immutable_mem_table_flushed': 'rocksdb.num.immutable.mem.table.flushed',
    'rocksdb_num_live_versions': 'rocksdb.num.live.versions',
    'rocksdb_num_running_compactions': 'rocksdb.num.running.compactions',
    'rocksdb_num_running_flushes': 'rocksdb.num.running.flushes',
    'rocksdb_num_snapshots': 'rocksdb.num.snapshots',
    'rocksdb_prunable_wal_files': 'rocksdb.prunable.wal.files',
    'rocksdb_size_all_mem_tables': 'rocksdb.size.all.mem.tables',
    'rocksdb_total_disk_space': 'rocksdb.total.disk.space',
    # health:
    'arangodb_dropped_followers_total': 'health.dropped_followers.total',
    'arangodb_heartbeat_failures_total': 'health.heartbeat_failures.total',
    'arangodb_heartbeat_send_time_msec': 'health.heartbeat.sent.time',
}


def construct_metrics_config(metric_map, type_overrides):
    metrics = []
    for raw_metric_name, metric_name in metric_map.items():
        if raw_metric_name.endswith('_total'):
            raw_metric_name = raw_metric_name[:-6]
            metric_name = metric_name[:-6]
        elif metric_name.endswith('.count'):
            metric_name = metric_name[:-6]

        config = {raw_metric_name: {'name': metric_name}}
        if raw_metric_name in type_overrides:
            config[raw_metric_name]['type'] = type_overrides[raw_metric_name]

        metrics.append(config)

    return metrics
