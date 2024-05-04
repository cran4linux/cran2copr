%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  repana
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Repeatable Analysis in R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI >= 1.0
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-pool 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-DBI >= 1.0
Requires:         R-CRAN-config 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-pool 
Requires:         R-CRAN-openxlsx 
Requires:         R-tools 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-digest 

%description
Set of utilities to facilitate the reproduction of analysis in R. It allow
to make_structure(), clean_structure(), and run and log programs in a
predefined order to allow secondary files, analysis and reports be
constructed in an ordered and reproducible form.

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
