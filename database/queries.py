from database import get_database_connection

def insert_root():
    try: 
        postgres = get_database_connection()
        cursor = postgres.cursor()

        root_nodes = [
            {"title": "server-alpha", "description": "primary server alpha", "status": "up"},
            {"title": "server-beta", "description": "secondary server beta", "status": "down"},
            {"title": "database-master", "description": "main database node", "status": "critical"},
            {"title": "cache-node-1", "description": "cache layer node one", "status": "up"},
            {"title": "load-balancer", "description": "traffic load balancer", "status": "expired"},
            {"title": "api-gateway", "description": "gateway for API requests", "status": "critical"},
            {"title": "backup-server", "description": "backup server for disaster recovery", "status": "up"},
            # {"title": "auth-service", "description": "authentication service", "status": "down"},
            # {"title": "kafka-broker", "description": "message broker", "status": "expired"},
            # {"title": "dns-node", "description": "DNS configuration node", "status": "up"},
            # {"title": "firewall-01", "description": "primary firewall", "status": "critical"},
            # {"title": "worker-node-1", "description": "worker node processing tasks", "status": "up"},
            # {"title": "worker-node-2", "description": "worker node processing tasks", "status": "down"},
            # {"title": "monitoring-agent", "description": "system monitoring agent", "status": "up"},
            # {"title": "scheduler", "description": "task scheduler for jobs", "status": "expired"},
            # {"title": "web-server-01", "description": "frontend web server", "status": "critical"},
            # {"title": "web-server-02", "description": "frontend web server", "status": "down"},
            # {"title": "storage-node-01", "description": "main storage node", "status": "up"},
            # {"title": "storage-node-02", "description": "backup storage node", "status": "expired"},
            # {"title": "analytics-engine", "description": "data analytics engine", "status": "critical"},
            # {"title": "mail-server", "description": "email server", "status": "up"},
            # {"title": "proxy-server", "description": "proxy for incoming traffic", "status": "down"},
            # {"title": "log-collector", "description": "system log collector", "status": "expired"},
            # {"title": "search-engine", "description": "search engine node", "status": "critical"},
            # {"title": "data-mirror", "description": "data mirroring service", "status": "up"},
            # {"title": "build-server", "description": "server for CI/CD builds", "status": "down"},
            # {"title": "test-runner", "description": "test automation runner", "status": "up"},
            # {"title": "reporting-service", "description": "generates reports", "status": "expired"},
            # {"title": "resource-manager", "description": "manages cloud resources", "status": "critical"},
            # {"title": "vm-instance-01", "description": "virtual machine instance", "status": "up"},
            # {"title": "vm-instance-02", "description": "virtual machine instance", "status": "down"},
            # {"title": "gpu-node", "description": "node with GPU acceleration", "status": "critical"},
            # {"title": "data-stream", "description": "real-time data stream", "status": "up"},
            # {"title": "config-server", "description": "configuration server", "status": "expired"},
            # {"title": "debug-node", "description": "debugging environment", "status": "down"},
            # {"title": "health-checker", "description": "health check service", "status": "critical"},
            # {"title": "api-mock", "description": "mock API service", "status": "up"},
            # {"title": "ci-agent", "description": "CI/CD agent", "status": "down"},
            # {"title": "orchestrator", "description": "orchestrates deployments", "status": "up"},
            # {"title": "iot-hub", "description": "hub for IoT devices", "status": "critical"},
            # {"title": "data-pipeline-01", "description": "data pipeline processor", "status": "up"},
            # {"title": "data-pipeline-02", "description": "data pipeline processor", "status": "expired"},
            # {"title": "identity-provider", "description": "identity and access management", "status": "critical"},
            # {"title": "cloud-storage", "description": "cloud storage bucket", "status": "up"},
            # {"title": "edge-device-01", "description": "edge computing device", "status": "down"},
            # {"title": "edge-device-02", "description": "edge computing device", "status": "up"},
            # {"title": "cluster-manager", "description": "manages cluster nodes", "status": "expired"},
            # {"title": "metrics-service", "description": "system metrics service", "status": "critical"},
            # {"title": "webhook-handler", "description": "handles webhooks", "status": "down"},
            # {"title": "file-system", "description": "distributed file system", "status": "up"},
            # {"title": "gateway-node", "description": "network gateway node", "status": "critical"},
            # {"title": "security-scanner", "description": "vulnerability scanner", "status": "expired"},
            # {"title": "dns-cache", "description": "DNS caching server", "status": "up"},
            # {"title": "build-cache", "description": "caching for build artifacts", "status": "down"},
            # {"title": "etl-engine", "description": "ETL processing engine", "status": "critical"},
            # {"title": "ai-model-node", "description": "serves AI models", "status": "up"},
            # {"title": "frontend-server", "description": "user-facing server", "status": "expired"},
            # {"title": "backend-server", "description": "API backend server", "status": "up"},
            # {"title": "load-generator", "description": "generates system load for testing", "status": "down"},
            # {"title": "service-bus", "description": "messaging service bus", "status": "critical"},
            # {"title": "ml-training-node", "description": "machine learning training node", "status": "up"},
            # {"title": "audit-logger", "description": "logs audit trails", "status": "expired"},
            # {"title": "billing-service", "description": "handles billing operations", "status": "down"},
            # {"title": "cdn-node", "description": "content delivery node", "status": "up"},
            # {"title": "data-lake", "description": "data lake for analytics", "status": "expired"},
            # {"title": "key-vault", "description": "secure key storage", "status": "critical"},
            # {"title": "encryption-service", "description": "handles encryption tasks", "status": "up"},
            # {"title": "session-manager", "description": "manages user sessions", "status": "down"},
            # {"title": "integration-test-node", "description": "node for integration tests", "status": "expired"},
            # {"title": "redis-cluster", "description": "distributed Redis cluster", "status": "critical"},
            # {"title": "ml-inference-node", "description": "runs ML inference tasks", "status": "up"},
            # {"title": "job-queue", "description": "handles background job queues", "status": "expired"},
            # {"title": "vpn-node", "description": "VPN gateway node", "status": "down"},
            # {"title": "incident-responder", "description": "handles incident responses", "status": "critical"},
            # {"title": "webhook-scheduler", "description": "schedules webhook events", "status": "up"},
            # {"title": "data-archive", "description": "long-term data archive", "status": "down"},
            # {"title": "streaming-node", "description": "streaming service node", "status": "critical"},
            # {"title": "voice-gateway", "description": "gateway for voice services", "status": "expired"},
            # {"title": "image-processor", "description": "processes image uploads", "status": "up"},
            # {"title": "pdf-generator", "description": "generates PDF files", "status": "down"},
            # {"title": "ai-training-cluster", "description": "AI training cluster node", "status": "up"},
            # {"title": "ci-cache", "description": "cache for CI builds", "status": "expired"},
            # {"title": "data-connector", "description": "connects to external data sources", "status": "critical"},
            # {"title": "user-profile-service", "description": "manages user profiles", "status": "up"},
            # {"title": "payment-gateway", "description": "handles payment transactions", "status": "down"},
            # {"title": "metrics-aggregator", "description": "aggregates system metrics", "status": "up"},
        ]

        for root_node in root_nodes:
            title = root_node["title"]
            description = root_node["description"]
            status = root_node["status"]

            print(title, description, status)

            cursor.execute("insert into nodes (title, description, status) values (%s, %s, %s)", (title, description, status))
            postgres.commit()
            
    except Exception as e:
        print(e)

insert_root()