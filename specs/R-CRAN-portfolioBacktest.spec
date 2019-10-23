%global packname  portfolioBacktest
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Automated Backtesting of Portfolios over Multiple Datasets

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-snow 
Requires:         R-utils 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Automated backtesting of multiple portfolios over multiple datasets of
stock prices in a rolling-window fashion. Intended for researchers and
practitioners to backtest a set of different portfolios, as well as by a
course instructor to assess the students in their portfolio design in a
fully automated and convenient manner, with results conveniently formatted
in tables and plots. Each portfolio design is easily defined as a function
that takes as input a window of the stock prices and outputs the portfolio
weights. Multiple portfolios can be easily specified as a list of
functions or as files in a folder. Multiple datasets can be conveniently
extracted randomly from different markets, different time periods, and
different subsets of the stock universe. The results can be later assessed
and ranked with tables based on a number of performance criteria (e.g.,
expected return, volatility, Sharpe ratio, drawdown, turnover rate, return
on investment, computational time, etc.), as well as plotted in a number
of ways with nice barplots and boxplots.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
