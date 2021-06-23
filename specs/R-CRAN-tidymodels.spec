%global __brp_check_rpaths %{nil}
%global packname  tidymodels
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load the 'Tidymodels' Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-cli >= 2.4.0
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.0.5
BuildRequires:    R-CRAN-conflicted >= 1.0.4
BuildRequires:    R-CRAN-broom >= 0.7.6
BuildRequires:    R-CRAN-infer >= 0.5.4
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-workflows >= 0.2.2
BuildRequires:    R-CRAN-rstudioapi >= 0.13
BuildRequires:    R-CRAN-parsnip >= 0.1.5
BuildRequires:    R-CRAN-tune >= 0.1.3
BuildRequires:    R-CRAN-recipes >= 0.1.16
BuildRequires:    R-CRAN-modeldata >= 0.1.0
BuildRequires:    R-CRAN-dials >= 0.0.9
BuildRequires:    R-CRAN-rsample >= 0.0.9
BuildRequires:    R-CRAN-yardstick >= 0.0.8
BuildRequires:    R-CRAN-workflowsets >= 0.0.2
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-cli >= 2.4.0
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.0.5
Requires:         R-CRAN-conflicted >= 1.0.4
Requires:         R-CRAN-broom >= 0.7.6
Requires:         R-CRAN-infer >= 0.5.4
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-workflows >= 0.2.2
Requires:         R-CRAN-rstudioapi >= 0.13
Requires:         R-CRAN-parsnip >= 0.1.5
Requires:         R-CRAN-tune >= 0.1.3
Requires:         R-CRAN-recipes >= 0.1.16
Requires:         R-CRAN-modeldata >= 0.1.0
Requires:         R-CRAN-dials >= 0.0.9
Requires:         R-CRAN-rsample >= 0.0.9
Requires:         R-CRAN-yardstick >= 0.0.8
Requires:         R-CRAN-workflowsets >= 0.0.2

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
