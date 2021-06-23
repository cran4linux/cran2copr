%global __brp_check_rpaths %{nil}
%global packname  do
%global packver   1.8.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Operator

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tmcn 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tmcn 
Requires:         R-methods 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-rstudioapi 

%description
Flexibly convert data between long and wide format using just two
functions: reshape_toLong() and reshape_toWide().

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
