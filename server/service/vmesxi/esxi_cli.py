from pyVim import connect
from pyVmomi import vim

si = connect.SmartConnect(host='192.168.66.199', user='root', pwd='123456789', disableSslCertValidation=True)
# 获取虚拟机列表
content = si.RetrieveContent()
container = content.rootFolder
viewType = [vim.VirtualMachine]
recursive = True

containerView = content.viewManager.CreateContainerView(container, viewType, recursive)
vms = containerView.view
print(vms)
for i in vms:
    print(i.name, i.runtime.powerState)
