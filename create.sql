Create database test;
create table house
(
    house_id      int auto_increment,
    toward        text          null,
    unit_price    int           null,
    building_area double        null,
    total_price   double        null,
    decoration    text          null,
    floor         text          null,
    unit_type     text          null,
    admin_id      int default 1 null,
    constraint house_house_id_uindex
        unique (house_id)
);

create table house_case
(
    house_id int null,
    case_id  int null,
    id       int auto_increment,
    constraint house_case_id_uindex
        unique (id),
    constraint house_case_house_id_0eb7c892_fk
        foreign key (house_id) references house (house_id)
);

alter table house_case
    add primary key (id);
create table intermediary
(
    house_id          int    null,
    intermediary_name text   null,
    phone             double null,
    id                int auto_increment
        primary key
);
create table location_of_house
(
    house_id       int  null,
    area           text null,
    community_name text null,
    part_area      text null,
    id             int auto_increment
        primary key
);
create table user
(
    UID           int auto_increment
        primary key,
    USERNAME      varchar(20) not null,
    PASSWORD      varchar(30) not null,
    REGISTER_TIME date        not null,
    admin         int         not null,
    constraint USERNAME
        unique (USERNAME)
);



alter table house
    add primary key (house_id);

create table `case`
(
    case_id   int  null,
    case_type text null,
    id        int auto_increment,
    constraint case_id_uindex
        unique (id)
);

alter table `case`
    add primary key (id);
