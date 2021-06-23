%global __brp_check_rpaths %{nil}
%global packname  cheese
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Working with Data During Statistical Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.4.1
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-kableExtra >= 1.0.1
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.2
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-rlang >= 0.4.3
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-forcats >= 0.3.0
Requires:         R-methods >= 3.4.1
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-kableExtra >= 1.0.1
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.2
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-rlang >= 0.4.3
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-forcats >= 0.3.0

%description
Contains tools for working with data during statistical analysis,
promoting flexible, intuitive, and reproducible workflows. There are
functions designated for specific statistical tasks such building a custom
univariate descriptive table, computing pairwise association statistics,
etc. These are built on a collection of data manipulation tools designed
for general use that are motivated by the functional programming concept.

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
