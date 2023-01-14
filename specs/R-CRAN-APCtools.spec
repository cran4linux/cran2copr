%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  APCtools
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Routines for Descriptive and Model-Based APC Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 

%description
Age-Period-Cohort (APC) analyses are used to differentiate relevant
drivers for long-term developments. The 'APCtools' package offers
visualization techniques and general routines to simplify the workflow of
an APC analysis. Sophisticated functions are available both for
descriptive and regression model-based analyses. For the former, we use
density (or ridgeline) matrices and (hexagonally binned) heatmaps as
innovative visualization techniques building on the concept of Lexis
diagrams. Model-based analyses build on the separation of the temporal
dimensions based on generalized additive models, where a tensor product
interaction surface (usually between age and period) is utilized to
represent the third dimension (usually cohort) on its diagonal. Such
tensor product surfaces can also be estimated while accounting for further
covariates in the regression model. See Weigert et al. (2021)
<doi:10.1177/1354816620987198> for methodological details.

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
