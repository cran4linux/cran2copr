%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GenMarkov
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Markov Chains

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet >= 7.3.16
BuildRequires:    R-CRAN-Hmisc >= 4.5.0
BuildRequires:    R-stats >= 4.1.0
BuildRequires:    R-CRAN-alabama >= 2015.3.1
BuildRequires:    R-CRAN-fastDummies >= 1.6.3
BuildRequires:    R-CRAN-maxLik >= 1.4.8
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
Requires:         R-CRAN-nnet >= 7.3.16
Requires:         R-CRAN-Hmisc >= 4.5.0
Requires:         R-stats >= 4.1.0
Requires:         R-CRAN-alabama >= 2015.3.1
Requires:         R-CRAN-fastDummies >= 1.6.3
Requires:         R-CRAN-maxLik >= 1.4.8
Requires:         R-CRAN-matrixcalc >= 1.0.3

%description
Provides routines to estimate the Mixture Transition Distribution Model
based on Raftery (1985) <http://www.jstor.org/stable/2345788> and Nicolau
(2014) <doi:10.1111/sjos.12087> specifications, for multivariate data.
Additionally, provides a function for the estimation of a new model for
multivariate non-homogeneous Markov chains. This new specification,
Generalized Multivariate Markov Chains (GMMC) was proposed by Carolina
Vasconcelos and Bruno Damasio and considers (continuous or discrete)
covariates exogenous to the Markov chain.

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
