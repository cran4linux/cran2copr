%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastverse
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Suite of High-Performance Packages for Statistics and Data Manipulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-kit 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-kit 
Requires:         R-CRAN-magrittr 

%description
Easy installation, loading and management, of high-performance packages
for statistical computing and data manipulation in R. The core 'fastverse'
consists of 4 packages: 'data.table', 'collapse', 'kit' and 'magrittr',
that jointly only depend on 'Rcpp'. The 'fastverse' can be freely and
permanently extended with additional packages, both globally or for
individual projects. Separate package verses can also be created. Fast
packages for many common tasks such as time series, dates and times,
strings, spatial data, statistics, data serialization, larger-than-memory
processing, and compilation of R code are listed in the README file:
<https://github.com/fastverse/fastverse#suggested-extensions>.

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
