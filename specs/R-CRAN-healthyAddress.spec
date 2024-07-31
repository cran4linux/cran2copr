%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  healthyAddress
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Convert Addresses to Standard Inputs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-hutils 
BuildRequires:    R-CRAN-hutilscpp 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-qs 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-hutils 
Requires:         R-CRAN-hutilscpp 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-qs 
Requires:         R-utils 

%description
Efficient tools for parsing and standardizing Australian addresses from
textual data. It utilizes optimized algorithms to accurately identify and
extract components of addresses, such as street names, types, and
postcodes, especially for large batched data in contexts where sending
addresses to internet services may be slow or inappropriate. The core
functionality is built on fast string processing techniques to handle
variations in address formats and abbreviations commonly found in
Australian address data. Designed for data scientists, urban planners, and
logistics analysts, the package facilitates the cleaning and normalization
of address information, supporting better data integration and analysis in
urban studies, geography, and related fields.

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
