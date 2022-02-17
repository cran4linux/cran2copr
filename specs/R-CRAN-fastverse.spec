%global __brp_check_rpaths %{nil}
%global packname  fastverse
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
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
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-kit 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-fst 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-kit 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-fst 

%description
Easy installation, loading and management, of a complementary set of
high-performance packages for statistical computing and data manipulation.
The core 'fastverse' consists of 6 packages: 'data.table', 'collapse',
'matrixStats', 'kit', 'magrittr' and 'fst', that jointly only depend on
'Rcpp'. These packages are attached and harmonized through the
'fastverse'. In addition, the 'fastverse' can be freely and permanently
extended with additional packages, both globally or for individual
projects. Entirely separate package verses can also be created. Selected
fast and low-dependency packages are suggested for various topics such as
time series, dates and times, strings, spatial data, statistics and data
serialization (see GitHub / website).

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
