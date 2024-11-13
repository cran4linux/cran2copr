%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LaMa
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Numerical Maximum Likelihood Estimation for Latent Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RTMB 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RTMB 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-splines 
Requires:         R-methods 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-circular 

%description
A variety of latent Markov models, including hidden Markov models, hidden
semi-Markov models, state-space models and continuous-time variants can be
formulated and estimated within the same framework via directly maximising
the likelihood function using the so-called forward algorithm. Applied
researchers often need custom models that standard software does not
easily support. Writing tailored 'R' code offers flexibility but suffers
from slow estimation speeds. We address these issues by providing
easy-to-use functions (written in 'C++' for speed) for common tasks like
the forward algorithm. These functions can be combined into custom models
in a Lego-type approach, offering up to 10-20 times faster estimation via
standard numerical optimisers. To aid in building fully custom likelihood
functions, several vignettes are included that show how to simulate data
from and estimate all the above model classes.

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
