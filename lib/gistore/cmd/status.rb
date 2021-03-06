module Gistore
  class Runner
    map "st" => :status
    desc "status", "Show backup entries list and run git status"
    option :config, :type => :boolean, :desc => "Show gistore configurations"
    option :backup, :type => :boolean,
                    :aliases => [:entries, :entry, :backups],
                    :desc => "Show backup list"
    option :git, :type => :boolean, :desc => "Show git status"
    def status(*args)
      parse_common_options_and_repo
      all = (not options.include? "config" and
             not  options.include? "backup" and
             not  options.include? "git")

      if all or options[:config]
        puts "Task name     : #{gistore.task_name || "-"}"
        puts "Gistore       : #{gistore.repo_path}"
        puts "Configurations:"
        puts Tty.show_columns gistore.gistore_config.to_a.map {|h| "#{h[0]}: #{h[1].inspect}"}
        puts
      end

      if all
        puts "Backup entries:"
        puts Tty.show_columns gistore.gistore_backups
        puts
      elsif options[:backup]
        puts gistore.gistore_backups.join("\n")
      end

      if all or options[:git]
        puts "#{'-' * 30} Git status #{'-' * 30}" if all
        gistore.safe_system(git_cmd, "status", *args)
      end
    rescue Exception => e
      Tty.die "#{e.message}"
    end
  end
end
