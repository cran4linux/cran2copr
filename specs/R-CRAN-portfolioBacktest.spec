%global __brp_check_rpaths %{nil}
%global packname  portfolioBacktest
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Backtesting of Portfolios over Multiple Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-parallel 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
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

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
