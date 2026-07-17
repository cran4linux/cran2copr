%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dtametaTMB
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostic Test Accuracy Meta-Analysis using Template Model Builder

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-forestploter 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-forestploter 
Requires:         R-CRAN-glmmTMB 
Requires:         R-grid 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-TMB 

%description
Fits the hierarchical summary receiver operating characteristic (HSROC)
model of Rutter and Gatsonis (2001) <doi:10.1002/sim.942>, the bivariate
binomial-normal model of Reitsma et al. (2005)
<doi:10.1016/j.jclinepi.2005.02.022>, and the threshold-based bivariate
time-to-event model of Hoyer et al. (2018) <doi:10.1002/jrsm.1273> using
Template Model Builder (TMB). Provides subgroup analyses, HSROC
meta-regression, likelihood-ratio tests, SROC plots, and coupled forest
plots.

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
