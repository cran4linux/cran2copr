%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsg
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Publication-Ready Statistical Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.3.10
BuildRequires:    R-CRAN-jsonlite >= 2.0.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-yaml >= 2.3.10
Requires:         R-CRAN-jsonlite >= 2.0.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-haven 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 

%description
A collection of functions for generating frequency tables and
cross-tabulations of categorical variables. The resulting tables can be
exported to various formats (Excel, PDF, HTML, etc.) with extensive
formatting and layout customization options.

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
