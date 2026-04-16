%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FAPA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Factor Analytic Profile Analysis of Ipsatized Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-boot 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements Factor Analytic Profile Analysis of Ipsatized Data ('FAPA'), a
metric inferential framework for pattern detection and person-level
reconstruction in multivariate profile data.  After row-centering
(ipsatization) to remove profile elevation, 'FAPA' applies singular value
decomposition ('SVD') to recover shared core profiles and individual
pattern weights.  Dimensionality is determined by a variance-matched
Horn's parallel analysis.  A three-stage bootstrap verification framework
assesses (1) dimensionality via parallel analysis, (2) subspace stability
via Procrustes principal angles, and (3) profile replicability via
Tucker's congruence coefficients.  BCa bootstrap confidence intervals for
core-profile coordinates are computed via the canonical 'boot' package
implementation of Davison and Hinkley (1997)
<doi:10.1017/CBO9780511802843>.

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
