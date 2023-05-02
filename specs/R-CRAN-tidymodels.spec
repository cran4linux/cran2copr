%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidymodels
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load the 'Tidymodels' Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-hardhat >= 1.3.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-conflicted >= 1.2.0
BuildRequires:    R-CRAN-dials >= 1.2.0
BuildRequires:    R-CRAN-yardstick >= 1.2.0
BuildRequires:    R-CRAN-workflows >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-rsample >= 1.1.1
BuildRequires:    R-CRAN-tune >= 1.1.1
BuildRequires:    R-CRAN-modeldata >= 1.1.0
BuildRequires:    R-CRAN-parsnip >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-recipes >= 1.0.6
BuildRequires:    R-CRAN-broom >= 1.0.4
BuildRequires:    R-CRAN-infer >= 1.0.4
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-workflowsets >= 1.0.1
BuildRequires:    R-CRAN-rstudioapi >= 0.14
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-hardhat >= 1.3.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-conflicted >= 1.2.0
Requires:         R-CRAN-dials >= 1.2.0
Requires:         R-CRAN-yardstick >= 1.2.0
Requires:         R-CRAN-workflows >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-rsample >= 1.1.1
Requires:         R-CRAN-tune >= 1.1.1
Requires:         R-CRAN-modeldata >= 1.1.0
Requires:         R-CRAN-parsnip >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-recipes >= 1.0.6
Requires:         R-CRAN-broom >= 1.0.4
Requires:         R-CRAN-infer >= 1.0.4
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-workflowsets >= 1.0.1
Requires:         R-CRAN-rstudioapi >= 0.14

%description
The tidy modeling "verse" is a collection of packages for modeling and
statistical analysis that share the underlying design philosophy, grammar,
and data structures of the tidyverse.

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
