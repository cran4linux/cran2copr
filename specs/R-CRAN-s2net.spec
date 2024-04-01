%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  s2net
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          The Generalized Semi-Supervised Elastic-Net

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-MASS 

%description
Implements the generalized semi-supervised elastic-net. This method
extends the supervised elastic-net problem, and thus it is a practical
solution to the problem of feature selection in semi-supervised contexts.
Its mathematical formulation is presented from a general perspective,
covering a wide range of models.  We focus on linear and logistic
responses, but the implementation could be easily extended to other losses
in generalized linear models. We develop a flexible and fast
implementation, written in 'C++' using 'RcppArmadillo' and integrated into
R via 'Rcpp' modules. See Culp, M. 2013 <doi:10.1080/10618600.2012.657139>
for references on the Joint Trained Elastic-Net.

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
