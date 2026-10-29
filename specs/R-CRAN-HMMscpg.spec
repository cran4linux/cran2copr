%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HMMscpg
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hidden Markov Models and Shifted Compound Poisson-Gamma Renewal Process

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Bessel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rdpack 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Bessel 
Requires:         R-CRAN-Rcpp 

%description
Provides functions to define, simulate and fit hidden Markov models,
hidden semi-Markov models, and their time-varying versions, to
incompletely observed point process records. Such data arise when some
events of an underlying point process are not recorded or are otherwise
missing. The models treat the number of missing events between each pair
of consecutively observed events of a point process record as a hidden
process. The number of missing events may be fixed or modelled as a random
variable whose distribution can vary over time. When the number of missing
events is fixed, the observed event times can be modelled as a compound
gamma renewal process. When it is random, the observed process is
represented by a shifted compound Poisson-gamma renewal process, which may
also depend on time, leading to a time-dependent shifted compound
Poisson-gamma renewal process. These modelling frameworks are described in
detail in Shahzadi, Wang, Parry and Bebbington (2023)
<doi:10.1007/s10463-022-00843-5> and Shahzadi, Wang, Parry and Bebbington
(2026) <doi:10.1007/s11634-025-00632-x>. The model parameters are
estimated through direct nonlinear numerical optimization of the
corresponding likelihood function, and each fit reports whether the change
points of its time-dependent components are identified by the data. The
package also provides methods for assessing model adequacy through
residual analysis. In addition, it calculates and plots the most probable
sequences of hidden states, allowing users to examine changes in the
underlying missing-event process over time.

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
