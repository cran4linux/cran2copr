%global __brp_check_rpaths %{nil}
%global packname  chandwich
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Chandler-Bate Sandwich Loglikelihood Adjustment

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-utils 

%description
Performs adjustments of a user-supplied independence loglikelihood
function using a robust sandwich estimator of the parameter covariance
matrix, based on the methodology in Chandler and Bate (2007)
<doi:10.1093/biomet/asm015>.  This can be used for cluster correlated data
when interest lies in the parameters of the marginal distributions or for
performing inferences that are robust to certain types of model
misspecification.  Functions for profiling the adjusted loglikelihoods are
also provided, as are functions for calculating and plotting confidence
intervals, for single model parameters, and confidence regions, for pairs
of model parameters.  Nested models can be compared using an adjusted
likelihood ratio test.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
