%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RestoreNet
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random-Effects Stochastic Reaction Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scatterpie 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scatterpie 
Requires:         R-CRAN-RColorBrewer 

%description
A random-effects stochastic model that allows quick detection of clonal
dominance events from clonal tracking data collected in gene therapy
studies. Starting from the Ito-type equation describing the dynamics of
cells duplication, death and differentiation at clonal level, we first
considered its local linear approximation as the base model. The
parameters of the base model, which are inferred using a maximum
likelihood approach, are assumed to be shared across the clones. Although
this assumption makes inference easier, in some cases it can be too
restrictive and does not take into account possible scenarios of clonal
dominance. Therefore we extended the base model by introducing random
effects for the clones. In this extended formulation the dynamic
parameters are estimated using a tailor-made expectation maximization
algorithm. Further details on the methods can be found in L. Del Core et
al., (2022) <doi:10.1101/2022.05.31.494100>.

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
