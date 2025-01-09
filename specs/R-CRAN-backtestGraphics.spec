%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  backtestGraphics
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Graphics for Portfolio Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tibble 

%description
Creates an interactive graphics interface to visualize backtest results of
different financial instruments, such as equities, futures, and credit
default swaps. The package does not run backtests on the given data set
but displays a graphical explanation of the backtest results. Users can
look at backtest graphics for different instruments, investment
strategies, and portfolios. Summary statistics of different portfolio
holdings are shown in the left panel, and interactive plots of profit and
loss (P&L), net market value (NMV) and gross market value (GMV) are
displayed in the right panel.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
