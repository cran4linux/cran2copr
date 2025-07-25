%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  meta
%global packver   8.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          General Package for Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-metafor >= 3.0.0
BuildRequires:    R-CRAN-metadat 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-metafor >= 3.0.0
Requires:         R-CRAN-metadat 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-xml2 
Requires:         R-methods 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-scales 

%description
User-friendly general package providing standard methods for meta-analysis
and supporting Schwarzer, Carpenter, and Rücker
<DOI:10.1007/978-3-319-21416-0>, "Meta-Analysis with R" (2015): - common
effect and random effects meta-analysis; - several plots (forest, funnel,
Galbraith / radial, L'Abbe, Baujat, bubble); - three-level meta-analysis
model; - generalised linear mixed model; - logistic regression with
penalised likelihood for rare events; - Hartung-Knapp method for random
effects model; - Kenward-Roger method for random effects model; -
prediction interval; - statistical tests for funnel plot asymmetry; -
trim-and-fill method to evaluate bias in meta-analysis; - meta-regression;
- cumulative meta-analysis and leave-one-out meta-analysis; - import data
from 'RevMan 5'; - produce forest plot summarising several (subgroup)
meta-analyses.

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
