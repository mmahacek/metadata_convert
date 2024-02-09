# metadata_convert.py

"""One-time convert custom OpenNMS metadata to `X-` prefix"""

import getpass

import pyonms
from pyonms.dao.nodes import NodeComponents
from pyonms.models.node import Metadata
from tqdm import tqdm

RESERVED_CONTEXTS = ["requisition"]


hostname = input("Enter hostname: ")
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

server = pyonms.PyONMS(
    hostname=hostname,
    username=username,
    password=password,
)

nodes = server.nodes.get_nodes(
    components=[NodeComponents.IP, NodeComponents.SERVICES, NodeComponents.METADATA]
)

for node in tqdm(nodes, unit="node", desc="Updating nodes"):
    # print(node.id, node.label)
    for meta in node.metadata:
        # print(" -", meta)
        if meta.context in RESERVED_CONTEXTS:
            continue
        if meta.context[:2] != "X-":
            new_meta = Metadata(
                context=f"X-{meta.context}", key=meta.key, value=meta.value
            )
            server.nodes.set_node_metadata(node=node, metadata=new_meta)
    for ip in tqdm(
        node.ipInterfaces, unit="ip", desc=f"Updating IPs for node {node.id}"
    ):
        # print(" -", ip.ipAddress)
        for meta in ip.metadata:
            # print("  -", meta)
            if meta.context in RESERVED_CONTEXTS:
                continue
            if meta.context[:2] != "X-":
                new_meta = Metadata(
                    context=f"X-{meta.context}", key=meta.key, value=meta.value
                )
                server.nodes.set_ip_metadata(
                    node=node, ip=ip.ipAddress, metadata=new_meta
                )
        for service in tqdm(
            ip.services, unit="service", desc=f"Updating services for IP {ip.ipAddress}"
        ):
            # print("  -", service.serviceType.name)
            for meta in service.metadata:
                # print("   -", meta)
                if meta.context in RESERVED_CONTEXTS:
                    continue
                if meta.context[:2] != "X-":
                    new_meta = Metadata(
                        context=f"X-{meta.context}", key=meta.key, value=meta.value
                    )
                    server.nodes.set_service_metadata(
                        node=node,
                        ip=ip.ipAddress,
                        service=service.serviceType.name,
                        metadata=new_meta,
                    )
