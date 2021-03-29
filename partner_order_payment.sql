-- +migrate Up
CREATE TABLE `paartner_order_payments` (
    `id` BIGINT unsigned NOT NULL AUTO_INCREMENT,
    `order_id` BIGINT UNSIGNED NOT NULL,
    `amount` FLOAT(11, 2) NOT NULL DEFAULT 0,
    `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    INDEX (`product_category_id`),
    INDEX (`brand`),
    CONSTRAINT `product_sugestions_outlet_partner_id_foreign` FOREIGN KEY (`outlet_partner_id`) REFERENCES `outlet_partners` (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;
-- +migrate Down
DROP TABLE `paartner_order_payments`;
