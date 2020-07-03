# -*- mode: ruby -*-
# vi: set ft=ruby  :

machines = {
  "samba" => {"memory" => "1024", "cpu" => "1", "ip" => "101", "image" => "ubuntu/bionic64"},
}

Vagrant.configure("2") do |config|

  machines.each do |name, conf|
    config.vm.define "#{name}" do |machine|
      machine.vm.box = "#{conf["image"]}"
      machine.vm.synced_folder ".", "/vagrant", disabled: true
      machine.ssh.forward_agent = true
      machine.vm.network "private_network", ip: "192.168.33.#{conf["ip"]}"
      machine.vm.hostname = "#{name}.pirodriguees.github.io"
      machine.vm.provider "virtualbox" do |vb|
        vb.name = "#{name}"
        vb.memory = conf["memory"]
        vb.cpus = conf["cpu"]
      end
    end
  end

#  config.vm.provision 'shell', path: 'vagrant_script/user.sh'
  
end
