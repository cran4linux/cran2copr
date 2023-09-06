%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  locits
%global packver   1.7.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.7
Release:          1%{?dist}%{?buildtag}
Summary:          Test of Stationarity and Localized Autocovariance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-wavethresh 
Requires:         R-CRAN-igraph 

%description
Provides test of second-order stationarity for time series (for dyadic and
arbitrary-n length data). Provides localized autocovariance, with
confidence intervals, for locally stationary (nonstationary) time series.
See Nason, G P (2013) "A test for second-order stationarity and
approximate confidence intervals for localized autocovariance for locally
stationary time series." Journal of the Royal Statistical Society, Series
B, 75, 879-904.  <doi:10.1111/rssb.12015>.

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
