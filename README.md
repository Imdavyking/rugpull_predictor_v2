# Rugpull Predictor

## Overview

Welcome to the Rugpull Predictor project! Our aim is to provide insights into the probability of an ERC20 token being involved in a rugpull when traded with WETH in a Uniswap V3 pool. We have developed an XGBoost Ensemble model that utilizes a comprehensive dataset comprising pool day data, mint data, and burn data spanning the last three years. This data was meticulously collected using The Graph API Substreams Uniswap v3 Ethereum subgraph, which you can explore [here](https://thegraph.com/explorer/subgraphs/HUZDsRpEVP2AvzDCyzDHtdc64dyDxx8FQjzsmqSg4H3B?view=Overview&chain=arbitrum-one).

## Table of Contents

- [Rugpull Predictor](#rugpull-predictor)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Data Collection](#data-collection)
  - [Labeling](#labeling)
  - [Challenges](#challenges)

## Getting Started

To begin exploring our dataset and model, you can clone our repository from [here](https://github.com/SamuelMoor-Smith/rugpull_predictor_v2.git).

### Prerequisites

Before using the model, make sure you have the necessary prerequisites installed. Our model relies on PyTorch and the Graph API. To access the Graph API, you will need to obtain an API key.

## Data Collection

Our data collection process involved querying the relevant data from the subgraph mentioned above. We collected pool day data, mint data, and burn data for Uniswap V3 pools. To narrow down our focus, we filtered the pools to include only those that traded an ERC20 token with WETH and had a substantial active period. We also set a minimum threshold for the total value locked (USD) to ensure the pools we analyzed were significant. This meticulous process resulted in approximately 6,000 pools and 5,000 tokens for analysis.

## Labeling

To label each pool as a potential rugpull, we examined the pool day data. Our criteria for identifying a rugpull involved a 99% drop in the total value locked (USD) compared to the previous day, provided that the previous day had a total value locked of more than $5,000 USD. You can find the code for this labeling process in the labeling folder of our repository.

## Challenges

One of the main challenges we encountered during this project was mitigating the risk of future biases in our predictive model. Our primary goal was to predict rugpulls before they occurred, necessitating the use of only pre-rugpull data for model training. Additionally, we aspired to incorporate token holder information, but the available data was not suitable for tokens that had already experienced rugpulls.

We hope this project provides valuable insights into the world of decentralized finance (DeFi) and helps users make informed decisions when interacting with ERC20 tokens and Uniswap V3 pools.
