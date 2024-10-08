%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lulab.utils
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Supporting Functions Maintained by Zhen Lu

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-descr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-table1 
BuildRequires:    R-utils 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-car 
Requires:         R-CRAN-descr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-table1 
Requires:         R-utils 

%description
Miscellaneous functions commonly used by LuLab. This package aims to help
more researchers on epidemiology to perform data management and
visualization more efficiently.

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
