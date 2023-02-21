%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cryptoTax
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Report Crypto Taxes (Canada Only)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-priceR 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-crypto2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-priceR 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-crypto2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-progress 

%description
Helps calculate crypto taxes in R. First, by allowing you to format .CSV
files from various exchanges to one large data frame of organized
transactions. Second, by allowing you to calculate your Adjusted Cost Base
(ACB), ACB per share, and realized and unrealized capital gains/losses.
Third, by calculating revenues gained from staking, interest, airdrops,
etc. Fourth, by calculating superficial losses as well. *Disclaimer: This
is not financial advice. Use at your own risks. There are no guarantees
whatsoever in relation to the use of this package. Please consult a tax
professional as necessary*.

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
