%global packname  apollo
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Choice Model Estimation and Application

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-RSGHB 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-mvtnorm 
Requires:         R-graphics 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-RSGHB 
Requires:         R-CRAN-coda 

%description
The Choice Modelling Centre (CMC) at the University of Leeds has developed
flexible code for the estimation and application of choice models in R.
Users are able to write their own model functions or use a mix of already
available ones. Random heterogeneity, both continuous and discrete and at
the level of individuals and choices, can be incorporated for all models.
There is support for both standalone models and hybrid model structures.
Both classical and Bayesian estimation is available, and multiple discrete
continuous models are covered in addition to discrete choice.
Multi-threading processing is supported for estimation and a large number
of pre and post-estimation routines, including for computing posterior
(individual-level) distributions are available. For examples, a manual,
and a support forum, visit www.ApolloChoiceModelling.com. For more
information on choice models see Train, K. (2009) <isbn:978-0-521-74738-7>
and Hess, S. & Daly, A.J. (2014) <isbn:978-1-781-00314-5> for an overview
of the field.

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
