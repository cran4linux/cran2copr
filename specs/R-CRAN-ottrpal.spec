%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ottrpal
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Companion Tools for Open-Source Tools for Training Resources (OTTR)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-gitcreds 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-webshot2 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-spelling 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-gitcreds 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-webshot2 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-spelling 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-yaml 

%description
Tools for converting Open-Source Tools for Training Resources (OTTR)
courses into Leanpub or Coursera courses. 'ottrpal' is for use with the
OTTR Template repository to create courses.

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
