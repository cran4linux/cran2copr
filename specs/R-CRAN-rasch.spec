%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rasch
%global packver   1.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          Models and Diagnostics for Rasch Measurement Theory

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 

%description
Fits models within Rasch Measurement Theory, whose defining properties
include sufficiency and invariance (Rasch, 1960 <ISBN:9780226705538>;
Andrich and Marais, 2019 <doi:10.1007/978-981-13-7496-8>). Models include
the dichotomous Rasch, partial credit, rating scale, explanatory,
many-facet and extended frame of reference models. Explanatory models
include the linear logistic test model (Fischer, 1973
<doi:10.1016/0001-6918(73)90003-6>) and linear partial credit model
(Fischer and Ponocny, 1994 <doi:10.1007/BF02295182>). Comparative
judgement models, including explanatory object models, are available for
dichotomous (Andrich, 1978 <doi:10.1177/014662167800200319>) and ordered
pairwise responses (Tutz, 1986 <doi:10.1016/0022-2496(86)90034-9>). Item
parameters for item-response models are estimated by pairwise conditional
maximum likelihood (Zwinderman, 1995 <doi:10.1177/014662169501900406>),
comparative judgement parameters by maximum likelihood, and person
locations by weighted likelihood (Warm, 1989 <doi:10.1007/BF02294627>).
Functions cover fit, targeting, reliability, dimensionality, local
dependence, differential item functioning, equating and simulation. A
'shiny' application provides a graphical interface to the analyses.

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
