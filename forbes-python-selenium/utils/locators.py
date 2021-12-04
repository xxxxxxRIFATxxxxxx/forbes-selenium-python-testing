from selenium.webdriver.common.by import By


class HomePageLocators(object):
    SUBSCRIBE = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > header > nav > div.header__right > div > a",
    )

    SIGN_IN = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > header > nav > div.header__right > div > div > button",
    )

    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > header > nav > div.header__right > button",
    )

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > div.search-modal > form > input",
    )

    EXPLORE = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > header > nav > div.header__left > button.icon--hamburger",
    )

    BILLIONAIRE = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > header > nav > div.header__channels--wrapper > ul > li.header__channel.header__color--centennial-silver.header__hoverable",
    )

    WORLDS_BILLIONAIRE = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > header > nav > div.header__channels--wrapper > ul > li.header__channel.header__color--centennial-silver.header__hoverable > div.header__subnav > ul > li:nth-child(2) > a",
    )

    FORBES_400 = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > header > nav > div.header__channels--wrapper > ul > li.header__channel.header__color--centennial-silver.header__hoverable > div.header__subnav > ul > li:nth-child(3) > a'",
    )

    INNOVATION = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > header > nav > div.header__channels--wrapper > ul > li.header__channel.header__color--diamondring-blue.header__hoverable > a",
    )

    FIVE_G = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > header > nav > div.header__channels--wrapper > ul > li.header__channel.header__color--diamondring-blue.header__hoverable > div.header__subnav > ul > li:nth-child(2) > a",
    )

    AI = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > header > nav > div.header__channels--wrapper > ul > li.header__channel.header__color--diamondring-blue.header__hoverable > div.header__subnav > ul > li:nth-child(3) > a",
    )

    FORBES_LIVE_EVENTS = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > footer > div.footer--desktop.fs-content > div.footer__content > div:nth-child(1) > div:nth-child(2) > a",
    )

    FORBES_BILLIONAIRES_PORTFOLIO = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > footer > div.footer--desktop.fs-content > div.footer__content > div:nth-child(1) > div:nth-child(4) > a:nth-child(1)",
    )

    ADVERTISE = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > footer > div.footer--desktop.fs-content > div.footer__content > div:nth-child(2) > div:nth-child(4) > a:nth-child(1)",
    )

    FORBES_ISRAEL = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > footer > div.footer--desktop.fs-content > div.footer__content > div.footer__column--right > div.footer__bottomright-promo > div > div:nth-child(2) > a:nth-child(1)",
    )

    FORBES_JAPAN = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--universal-header > footer > div.footer--desktop.fs-content > div.footer__content > div.footer__column--right > div.footer__bottomright-promo > div > div:nth-child(2) > a:nth-child(3)",
    )


class AdvertisePageLocators(object):
    US_EUROPE = (
        By.CSS_SELECTOR,
        "body > main > div.media-hero-section > div > div.tabs-widget > div > ul > li:nth-child(1) > a",
    )

    US_EUROPE_1ST_POST = (
        By.CSS_SELECTOR,
        "#\\32 021_media_kit > div > div > div.col-md-5.media-kit-content > div > a",
    )

    ASIA_PACIFIC = (
        By.CSS_SELECTOR,
        "body > main > div.media-hero-section > div > div.tabs-widget > div > ul > li:nth-child(2) > a",
    )

    ASIA_PACIFIC_POST = (
        By.CSS_SELECTOR,
        "#\\32 021_forbes_asia_media_kit > div > div > div.col-md-5.media-kit-content > div > a",
    )


class BillionairesPageLocators(object):

    FACEBOOK_SHARE = (
        By.CSS_SELECTOR,
        "#gatsby-focus-wrapper > div > div > div.title.has-left-rail > div.left-rail > div:nth-child(3) > div.social > div > div:nth-child(1)",
    )

    TWITTER_SHARE = (
        By.CSS_SELECTOR,
        "#gatsby-focus-wrapper > div > div > div.title.has-left-rail > div.left-rail > div:nth-child(3) > div.social > div > div:nth-child(2)",
    )

    LINKDIN_SHARE = (
        By.CSS_SELECTOR,
        "#gatsby-focus-wrapper > div > div > div.title.has-left-rail > div.left-rail > div:nth-child(3) > div.social > div > div:nth-child(3)",
    )

    MAIL = (
        By.CSS_SELECTOR,
        "#gatsby-focus-wrapper > div > div > div.title.has-left-rail > div.left-rail > div:nth-child(3) > div.social > div > div:nth-child(4)",
    )

    SEARCH = (
        By.CSS_SELECTOR,
        "#gatsby-focus-wrapper > div > header > div > a.header__search",
    )

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "body > div.main-content.main-content--overflow-visible.main-content--universal-header > main > div.search-content-wrapper > div.search-content.main-content__left-col > div.search-box > input",
    )

    ELON_MUSK = (
        By.CSS_SELECTOR,
        "#elon-musk > div.personName",
    )

    ELON_MUSK_PROFILE = (
        By.CSS_SELECTOR,
        "#gatsby-focus-wrapper > div > div > div.table-block > div.table-block-wrapper > div.table > div.table-body > div:nth-child(1) > div.expanded-content > div.person-bio > div.bio-container > div.bio-button-container > a",
    )


class BillionairesPortfolioPageLocators(object):
    EDITION = (
        By.CSS_SELECTOR,
        "#row-0 > div.channel__header > div.edition-dropdown > button",
    )

    US = (
        By.CSS_SELECTOR,
        "#row-0 > div.channel__header > div.edition-dropdown.edition-dropdown--open > ul > li:nth-child(1) > a",
    )

    INTEL_SAYS_POST = (
        By.CSS_SELECTOR,
        "#row-0 > div.channel__content > div.card.card--large.csf-block > div.card--large__title > a",
    )

    ASIA = (
        By.CSS_SELECTOR,
        "#row-0 > div.channel__header > div.edition-dropdown.edition-dropdown--open > ul > li:nth-child(2)",
    )

    AC_VENTURES_POST = (
        By.CSS_SELECTOR,
        "#row-0 > div.channel__content > div.channel__columns > div:nth-child(1) > div > a.headlink",
    )

    EUROPE = (
        By.CSS_SELECTOR,
        "#row-0 > div.channel__header > div.edition-dropdown.edition-dropdown--open > ul > li:nth-child(3)",
    )

    HALLOFFRAMEPOST = (
        By.CSS_SELECTOR,
        "#row-0 > div.channel__content > div.channel__columns > div:nth-child(1) > div > a.headlink",
    )
