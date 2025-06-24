%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  denguedatahub
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Tidy Format Datasets of Dengue by Country

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-tabulapdf 
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-here 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-tabulapdf 

%description
Provides a weekly, monthly, yearly summary of dengue cases by state/
province/ country.

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
