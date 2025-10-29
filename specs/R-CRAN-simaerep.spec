%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simaerep
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Detect Clinical Trial Sites Over- or Under-Reporting Clinical Events

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-furrr >= 0.2.1
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-furrr >= 0.2.1
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-glue 

%description
Monitoring reporting rates of subject-level clinical events (e.g. adverse
events, protocol deviations) reported by clinical trial sites is an
important aspect of risk-based quality monitoring strategy. Sites that are
under-reporting or over-reporting events can be detected using bootstrap
simulations during which patients are redistributed between sites.
Site-specific distributions of event reporting rates are generated that
are used to assign probabilities to the observed reporting rates.
(Koneswarakantha 2024 <doi:10.1007/s43441-024-00631-8>).

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
