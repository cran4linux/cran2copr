%global __brp_check_rpaths %{nil}
%global packname  trialr
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Trial Designs in 'rstan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-rstan >= 2.18.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.1
BuildRequires:    R-CRAN-tidybayes >= 2.0.3
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-rstan >= 2.18.2
Requires:         R-CRAN-tidybayes >= 2.0.3
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rstantools

%description
A collection of clinical trial designs and methods, implemented in 'rstan'
and R, including: the Continual Reassessment Method by O'Quigley et al.
(1990) <doi:10.2307/2531628>; EffTox by Thall & Cook (2004)
<doi:10.1111/j.0006-341X.2004.00218.x>; the two-parameter logistic method
of Neuenschwander, Branson & Sponer (2008) <doi:10.1002/sim.3230>; and the
Augmented Binary method by Wason & Seaman (2013) <doi:10.1002/sim.5867>;
and more. We provide functions to aid model-fitting and analysis. The
'rstan' implementations may also serve as a cookbook to anyone looking to
extend or embellish these models. We hope that this package encourages the
use of Bayesian methods in clinical trials. There is a preponderance of
early phase trial designs because this is where Bayesian methods are used
most. If there is a method you would like implemented, please get in
touch.

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
