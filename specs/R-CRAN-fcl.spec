%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fcl
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Financial Calculator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-ymd 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-ymd 

%description
A financial calculator that provides very fast implementations of common
financial indicators using 'Rust' code. It includes functions for
bond-related indicators, such as yield to maturity ('YTM'), modified
duration, and Macaulay duration, as well as functions for calculating
time-weighted and money-weighted rates of return (using 'Modified Dietz'
method) for multiple portfolios, given their market values and profit and
loss ('PnL') data. 'fcl' is designed to be efficient and accurate for
financial analysis and computation. The methods used in this package are
based on the following references:
<https://en.wikipedia.org/wiki/Modified_Dietz_method>,
<https://en.wikipedia.org/wiki/Time-weighted_return>.

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
