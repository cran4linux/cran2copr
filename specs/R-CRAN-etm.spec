%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  etm
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Transition Matrix

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-survival 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-data.table 

%description
The etm (empirical transition matrix) package permits to estimate the
matrix of transition probabilities for any time-inhomogeneous multi-state
model with finite state space using the Aalen-Johansen estimator.
Functions for data preparation and for displaying are also included
(Allignol et al., 2011 <doi:10.18637/jss.v038.i04>). Functionals of the
Aalen-Johansen estimator, e.g., excess length-of-stay in an intermediate
state, can also be computed (Allignol et al. 2011
<doi:10.1007/s00180-010-0200-x>).

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
