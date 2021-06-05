%global packname  sitsfeats
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Satellite Image Time Series Features

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-geos 
BuildRequires:    R-CRAN-libgeos 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-geos 
Requires:         R-CRAN-libgeos 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 

%description
Provides a set of temporal metrics derived from satellite image time
series. The basics metrics are composed of basic statistics,
histogram-based statistics, and methods based on time series analysis. The
polar metrics, an approach proposed by Korting et al. (2013)
<doi:10.1016/j.cageo.2013.02.007>, is based on the polar representation to
describe cyclic events, whose events are common in agricultural
applications.

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
