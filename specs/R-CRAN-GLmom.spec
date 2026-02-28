%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GLmom
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized L-Moments Estimation for Extreme Value Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lmomco 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-graphics 
Requires:         R-CRAN-lmomco 
Requires:         R-CRAN-nleqslv 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ismev 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-zoo 
Requires:         R-graphics 

%description
Provides generalized L-moments estimation methods for the generalized
extreme value ('GEV') distribution. Implements both stationary 'GEV' and
non-stationary 'GEV11' models where location and scale parameters vary
with time. Includes various penalty functions ('Martins'-'Stedinger',
Park, Cannon, 'Coles'-Dixon) for shape parameter regularization. Also
provides model averaging estimation ('ma.gev') that combines MLE and
L-moment methods with multiple weighting schemes for robust high quantile
estimation. The 'GLME' methodology is described in Shin et al. (2025a)
<doi:10.48550/arXiv.2512.20385>. The non-stationary L-moment method is
based on Shin et al. (2025b) <doi:10.1007/s42952-025-00325-3>. The model
averaging method is described in Shin et al. (2026)
<doi:10.1007/s00477-025-03167-x>. See also 'Hosking' (1990)
<doi:10.1111/j.2517-6161.1990.tb01775.x> for L-moments theory and
'Martins' and 'Stedinger' (2000) <doi:10.1029/1999WR900330> for penalized
likelihood methods.

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
