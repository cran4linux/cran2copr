%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vachette
%global packver   0.40.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.40.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Method for Visualization of Pharmacometric Models

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-prospectr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-photobiology 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-prospectr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-photobiology 

%description
A method to visualize pharmacometric analyses which are impacted by
covariate effects. Variability-aligned covariate harmonized-effects and
time-transformation equivalent ('vachette') facilitates intuitive overlays
of data and model predictions, allowing for comprehensive comparison
without dilution effects. 'vachette' improves upon previous methods
Lommerse et al. (2021) <doi:10.1002/psp4.12679>, enabling its application
to all pharmacometric models and enhancing Visual Predictive Checks (VPC)
by integrating data into cohesive plots that can highlight model
misspecification.

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
