%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmmrOptim
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Approximate Optimal Experimental Designs Using Generalised Linear Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-glmmrBase >= 0.4.5
BuildRequires:    R-CRAN-rminqa >= 0.2.2
BuildRequires:    R-CRAN-SparseChol >= 0.2.1
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-glmmrBase >= 0.4.5
Requires:         R-methods 
Requires:         R-CRAN-digest 

%description
Optimal design analysis algorithms for any study design that can be
represented or modelled as a generalised linear mixed model including
cluster randomised trials, cohort studies, spatial and temporal
epidemiological studies, and split-plot designs. See
<https://github.com/samuel-watson/glmmrBase/blob/master/README.md> for a
detailed manual on model specification. A detailed discussion of the
methods in this package can be found in Watson and Pan (2022)
<arXiv:2207.09183>.

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
