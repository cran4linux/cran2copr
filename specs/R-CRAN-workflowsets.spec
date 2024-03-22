%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  workflowsets
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create a Collection of 'tidymodels' Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-pillar >= 1.7.0
BuildRequires:    R-CRAN-hardhat >= 1.2.0
BuildRequires:    R-CRAN-parsnip >= 1.2.0
BuildRequires:    R-CRAN-tune >= 1.2.0
BuildRequires:    R-CRAN-workflows >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-CRAN-generics >= 0.1.2
BuildRequires:    R-CRAN-rsample >= 0.0.9
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-pillar >= 1.7.0
Requires:         R-CRAN-hardhat >= 1.2.0
Requires:         R-CRAN-parsnip >= 1.2.0
Requires:         R-CRAN-tune >= 1.2.0
Requires:         R-CRAN-workflows >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-generics >= 0.1.2
Requires:         R-CRAN-rsample >= 0.0.9
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-withr 

%description
A workflow is a combination of a model and preprocessors (e.g, a formula,
recipe, etc.) (Kuhn and Silge (2021) <https://www.tmwr.org/>). In order to
try different combinations of these, an object can be created that
contains many workflows. There are functions to create workflows en masse
as well as training them and visualizing the results.

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
