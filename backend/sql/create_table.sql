create table trademark (
    id bigserial not null,
    name text,
    logo text,
    active bool default true,
    constraint pkey_trademark primary key (id)
);

create table category (
    id bigserial not null,
    name text,
    parent bigint,
    image bigint,
    active bool default true,
    constraint pkey_category primary key (id)
);

create table product (
    id bigserial not null,
    trademark bigint,
    name text,
    category bigint,
    cost int,
    price int,
    star int,
    images bigint[],
    description text,
    sales int,
    comment text,
    ship_comment text,
    active bool default true,
    constraint pkey_product primary key (id)
);

create table image (
    id bigserial not null,
    name text,
    url text,
    path text,
    active bool default true,
    constraint pkey_image primary key (id)
);

create table "user" (
    id bigserial not null,
    name text,
    code text,
    password text,
    tel text,
    email text,
    address text,
    role int, -- 0: user, 1: admin
    active bool default true,
    constraint pkey_user primary key (id)
);

create table "cart" (
    id bigserial not null,
    user_id bigint,
    product_id bigint,
    quantity int,
    is_ordered bool,
    active bool default true,
    constraint pkey_cart primary key (id)
);

create table "order" (
    id bigserial not null,
    user_id bigint,
    product_id bigint,
    quantity int,
    status text,
    active bool default true,
    constraint pkey_order primary key (id)
);