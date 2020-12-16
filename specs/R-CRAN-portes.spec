%global packname  portes
%global packver   5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Portmanteau Tests for Univariate and Multivariate Time Series Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-forecast 
Requires:         R-parallel 
Requires:         R-CRAN-forecast 

%description
Contains common univariate and multivariate portmanteau test statistics in
time series based on the asymptotic distributions and the Monte Carlo
significance tests. Simulate univariate and multivariate data from
seasonal and nonseasonal time series models. See Mahdi and McLeod (2012)
<doi:10.1111/j.1467-9892.2011.00752.x> and Mahdi and McLeod (2020)
<arXiv:2005.00931>.

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
