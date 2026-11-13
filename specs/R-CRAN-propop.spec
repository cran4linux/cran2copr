%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  propop
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Project Population Growth in Switzerland Using the Cohort Component Method

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-BFS 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-BFS 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-purrr 

%description
Project the development of the population at different spatial levels
(e.g., cantons, districts, municipalities) using the cohort component
method, broken down by 101 one-year age classes, gender, and nationality
(see e.g. Preston et al. (2000, ISBN: 978-1-557-86451-2)). Includes helper
functions to download required population data and projection parameters
as open data for Switzerland, plus tools for model evaluation against
benchmarks such as population records or a base model.

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
