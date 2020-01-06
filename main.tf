provider "heroku" {
  version = "~> 2.2.1"
}
provider "cloudflare" {
  version = "~> 1.9"
}
terraform {
  backend "s3" {
    bucket  = "crowdbotics-terraform"
    key     = "djangotestdemo_dev_1445"
    region  = "us-east-1"
    encrypt = "true"
  }
}
