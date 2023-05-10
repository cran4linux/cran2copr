%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StockDistFit
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Stock Price Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ghyp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-xts 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-quantmod 
Requires:         R-utils 
Requires:         R-CRAN-ghyp 

%description
The 'StockDistFit' package provides functions for fitting probability
distributions to stock price data. The package uses maximum likelihood
estimation to find the best-fitting distribution for a given stock. It
also offers a function to fit several distributions to one or more assets
and compare the distribution with the Akaike Information Criterion (AIC)
and then pick the best distribution. References are as follows: Siew et
al. (2008)
<https://www.jstage.jst.go.jp/article/jappstat/37/1/37_1_1/_pdf/-char/ja>
and Benth et al. (2008)
<https://books.google.co.ke/books?hl=en&lr=&id=MHNpDQAAQBAJ&oi=fnd&pg=PR7&dq=Stochastic+modeling+of+commodity+prices+using+the+Variance+Gamma+(VG)+model.+&ots=YNIL2QmEYg&sig=XZtGU0lp4oqXHVyPZ-O8x5i7N3w&redir_esc=y#v=onepage&q&f=false>.

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
