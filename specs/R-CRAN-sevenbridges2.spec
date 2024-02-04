%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sevenbridges2
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The 'Seven Bridges Platform' API Client

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-data.table 

%description
R client and utilities for 'Seven Bridges Platform' API, from 'Cancer
Genomics Cloud' to other 'Seven Bridges' supported platforms. API
documentation is hosted publicly at
<https://docs.sevenbridges.com/docs/the-api>.

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
