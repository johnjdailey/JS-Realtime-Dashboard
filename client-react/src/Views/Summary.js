import React, { Component } from "react";
import wallet from "../img/money-bag.svg";
import exchange_green from "../img/exchange.svg";
import exchange_red from "../img/exchange-red.svg";
import returns from "../img/discount.svg";

class Summary extends Component {
  constructor() {
    super();
    this.state = {
      model_score: {},
      profit: {},
    };
  }

  componentDidMount() {
    setInterval(async () => {
      fetch("http://127.0.0.1:9000/btc/profit")
        .then((res) => res.json())
        .then((data) => {
          this.setState({ profit: data });
        });
    }, 15000);
  }

  render() {
    const { profit } = this.state;

    return (
      <div className="col">
        <div className="card border-0">
          <div className="card-content">
            <div className="card-body">
              <div className="row">
                <div className="col-xl-4 col-lg-6 col-md-12 border-right clearfix">
                  <div className="float-left pl-2 block-content">
                    <span className="grey darken-1 block title">
                      Initial Investment
                    </span>
                    <div className="font-large-3 line-height-1 text-bold-33 value">
                      10,000 $
                      <img src={wallet} alt="" />
                    </div>
                  </div>
                </div>
                <div className="col-xl-4 col-lg-6 col-md-12 border-right clearfix">
                  <div className="float-left pl-2 block-content">
                    <span className="title">Return Percentage</span>
                    <div className="font-large-3 line-height-1 text-bold-33 value">
                      {Number(profit["rtn_pct"]) !== 0
                        ? (Number(profit["rtn_pct"]) - 100)
                            .toFixed(2)
                            .toLocaleString()
                        : Number(profit["rtn_pct"])
                            .toFixed(2)
                            .toLocaleString()}{" "}
                      %
                      <img src={returns} alt="" />
                    </div>
                  </div>
                </div>
                <div className="col-xl-4 col-lg-6 col-md-12 clearfix">
                  <div className="float-left pl-2 block-content">
                    <span className="title">Profit/Loss</span>
                    <div className="font-large-3 line-height-1 text-bold-33 value">
                      {Number(profit["profit_loss"])
                        .toFixed(1)
                        .toLocaleString()}{" "}
                      $
                      <img
                        src={
                          Number(profit["profit_loss"]) > 0
                            ? exchange_green
                            : exchange_red
                        }
                        alt=""
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Summary;
