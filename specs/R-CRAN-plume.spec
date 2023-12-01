%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plume
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Simple Author Handler for Scientific Writing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-yaml >= 2.3.5
BuildRequires:    R-CRAN-jsonlite >= 1.6.0
BuildRequires:    R-CRAN-knitr >= 1.40
BuildRequires:    R-CRAN-glue >= 1.3.2
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-readr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-yaml >= 2.3.5
Requires:         R-CRAN-jsonlite >= 1.6.0
Requires:         R-CRAN-knitr >= 1.40
Requires:         R-CRAN-glue >= 1.3.2
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-stringr 

%description
Handles and formats author information in scientific writing in 'R
Markdown' and 'Quarto'. 'plume' provides easy-to-use and flexible tools
for injecting author metadata in 'YAML' headers as well as generating
author and contribution lists (among others) as strings from tabular data.

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
