%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  convergEU
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Monitoring Convergence of EU Countries

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-eurostat 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-eurostat 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-ggpubr 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 

%description
Indicators and measures by country and time describe what happens at
economic and social levels. This package provides functions to calculate
several measures of convergence after imputing missing values. The
automated downloading of Eurostat data, followed by the production of
country fiches and indicator fiches, makes possible to produce automated
reports. The Eurofound report (<doi:10.2806/68012>) "Upward convergence in
the EU: Concepts, measurements and indicators", 2018, is a detailed
presentation of convergence.

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
