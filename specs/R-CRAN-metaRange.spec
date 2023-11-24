%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaRange
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Framework to Build Mechanistic and Metabolic Constrained Species Distribution Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-terra 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-checkmate 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 

%description
Build spatially and temporally explicit process-based species distribution
models, that can include an arbitrary number of environmental factors,
species and processes including metabolic constraints and species
interactions. The focus of the package is simulating populations of one or
multiple species in a grid-based landscape and studying the
meta-population dynamics and emergent patterns that arise from the
interaction of species under complex environmental conditions. It provides
functions for common ecological processes such as negative exponential,
kernel-based dispersal (see Nathan et al. (2012)
<doi:10.1093/acprof:oso/9780199608898.003.0015>), calculation of the
environmental suitability based on cardinal values ( Yin et al. (1995)
<doi:10.1016/0168-1923(95)02236-Q>, simplified by Yan and Hunt (1999)
<doi:10.1006/anbo.1999.0955> see eq: 4), reproduction in form of an Ricker
model (see Ricker (1954) <doi:10.1139/f54-039> and Cabral and Schurr
(2010) <doi:10.1111/j.1466-8238.2009.00492.x>), as well as metabolic
scaling based on the metabolic theory of ecology (see Brown et al. (2004)
<doi:10.1890/03-9000> and Brown, Sibly and Kodric-Brown (2012)
<doi:10.1002/9781119968535.ch>).

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
