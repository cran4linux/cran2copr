%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spANOVA
%global packver   0.99.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.4
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Field Trials with Geostatistics & Spatial AR Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ScottKnott 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-spatialreg 
BuildRequires:    R-CRAN-shinycssloaders 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-geoR 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ScottKnott 
Requires:         R-CRAN-car 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-spatialreg 
Requires:         R-CRAN-shinycssloaders 

%description
Perform analysis of variance when the experimental units are spatially
correlated. There are two methods to deal with spatial dependence: Spatial
autoregressive models (see Rossoni, D. F., & Lima, R. R. (2019)
<doi:10.28951/rbb.v37i2.388>) and geostatistics (see Pontes, J. M., &
Oliveira, M. S. D. (2004) <doi:10.1590/S1413-70542004000100018>). For both
methods, there are three multicomparison procedure available: Tukey,
multivariate T, and Scott-Knott.

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
