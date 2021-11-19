%global __brp_check_rpaths %{nil}
%global packname  isoreader
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Read Stable Isotope Data Files

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-UNF >= 2.0.6
BuildRequires:    R-CRAN-lubridate >= 1.7.9.2
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-future >= 1.18.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-vctrs >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-UNF >= 2.0.6
Requires:         R-CRAN-lubridate >= 1.7.9.2
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-future >= 1.18.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-vctrs >= 0.3.4
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-magrittr 

%description
Interface to the raw data file formats commonly encountered in scientific
disciplines that make use of stable isotopes.

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
