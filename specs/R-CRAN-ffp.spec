%global __brp_check_rpaths %{nil}
%global packname  ffp
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fully Flexible Probabilities for Stress Testing and Portfolio Construction

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-ggdist >= 3.1.1
BuildRequires:    R-CRAN-magrittr >= 2.0.2
BuildRequires:    R-CRAN-nloptr >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.8.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-mvtnorm >= 1.1.3
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-NlcOptim >= 0.6
BuildRequires:    R-CRAN-forcats >= 0.5.1
BuildRequires:    R-CRAN-vctrs >= 0.3.8
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-ggdist >= 3.1.1
Requires:         R-CRAN-magrittr >= 2.0.2
Requires:         R-CRAN-nloptr >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.8.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-mvtnorm >= 1.1.3
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-NlcOptim >= 0.6
Requires:         R-CRAN-forcats >= 0.5.1
Requires:         R-CRAN-vctrs >= 0.3.8
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-crayon 

%description
Implements numerical entropy-pooling for scenario analysis as described in
Meucci, Attilio (2010) <doi:10.2139/ssrn.1696802>.

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
