%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MAPCtools
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Age-Period-Cohort (MAPC) Modeling for Health Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-survey 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-purrr 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-survey 

%description
Bayesian multivariate age-period-cohort (MAPC) models for analyzing health
data, with support for model fitting, visualization, stratification, and
model comparison. Inference focuses on identifiable cross-strata
differences, as described by Riebler and Held (2010)
<doi:10.1093/biostatistics/kxp037>. Methods for handling complex survey
data via the 'survey' package are included, as described in Mercer et al.
(2014) <doi:10.1016/j.spasta.2013.12.001>.

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
