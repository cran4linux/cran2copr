%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mantis
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Time Series Scanner

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.1
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-dplyr >= 1.1.1
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-lubridate 

%description
Generate interactive html reports that enable quick visual review of
multiple related time series stored in a data frame. For static datasets,
this can help to identify any temporal artefacts that may affect the
validity of subsequent analyses. For live data feeds, regularly scheduled
reports can help to pro-actively identify data feed problems or unexpected
trends that may require action. The reports are self-contained and
shareable without a web server.

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
