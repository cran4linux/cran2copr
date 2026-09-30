%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autoslider.trade
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Slide Automation for Trading Tables, Listings and Figures

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-autoslider.core 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-formatters 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlistings 
BuildRequires:    R-CRAN-rtables 
BuildRequires:    R-stats 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-autoslider.core 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-formatters 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlistings 
Requires:         R-CRAN-rtables 
Requires:         R-stats 

%description
A downstream package of 'autoslider.core' that produces tables, listings
and figures for finance trading, in the same style as 'autoslider'. Where
'autoslider.core' automates clinical study outputs, this package automates
trading outputs from price and trade data: performance tables, equity
curves and trade listings.

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
