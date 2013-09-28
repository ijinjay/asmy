set global event_scheduler=1;
create event designer_pfmc2zero on schedule every month starts '2013-10-01 00:00:00' do update mytest_designer set performance = 0;
