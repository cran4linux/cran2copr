%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bedrock
%global packver   0.1.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.16
Release:          1%{?dist}%{?buildtag}
Summary:          Base Functions for the 'DescToolsX' Ecosystem

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-expm 
Requires:         R-tools 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-cli 

%description
Provides the low level utilities on which the 'DescToolsX' ecosystem is
built. Covered are data manipulation and reshaping, predicates for data
inspection and validation, vector and string operations, handling of
labels and metadata, and routines from number theory and combinatorics.
All functions share a common naming and argument scheme and are
implemented as S3 generics wherever several input types are meaningful,
with performance critical parts written in C++. The package is self
contained and can be used on its own, independently of the higher level
packages of the suite.

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
