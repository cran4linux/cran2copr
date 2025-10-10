%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psme
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Splines Mixed-Effects Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-lme4 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-lme4 

%description
Fit penalized splines mixed-effects models (a special case of additive
models) for large longitudinal datasets. The package includes a psme()
function that (1) relies on package 'mgcv' for constructing population and
subject smooth functions as penalized splines, (2) transforms the
constructed additive model to a linear mixed-effects model, (3) exploits
package 'lme4' for model estimation and (4) backtransforms the estimated
linear mixed-effects model to the additive model for interpretation and
visualization. See Pedersen et al. (2019) <doi:10.7717/peerj.6876> and
Bates et al. (2015) <doi:10.18637/jss.v067.i01> for an introduction.
Unlike the gamm() function in 'mgcv', the psme() function is fast and
memory-efficient, able to handle datasets with millions of observations.

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
