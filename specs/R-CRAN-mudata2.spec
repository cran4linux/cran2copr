%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mudata2
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interchange Tools for Multi-Parameter Spatiotemporal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-fs 

%description
Formatting and structuring multi-parameter spatiotemporal data is often a
time-consuming task. This package offers functions and data structures
designed to easily organize and visualize these data for applications in
geology, paleolimnology, dendrochronology, and paleoclimate. See
Dunnington and Spooner (2018) <doi:10.1139/facets-2017-0026>.

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
