%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesRTMB
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference Using 'RTMB'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RTMB 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-RTMB 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-MASS 

%description
Provides tools for Markov chain Monte Carlo (MCMC) and Maximum A
Posteriori (MAP) estimation utilizing the 'RTMB' package. It supports
various statistical models including generalized linear mixed models,
factor analysis, item response theory, and multidimensional unfolding. The
package allows users to easily transition between frequentist and Bayesian
paradigms using a unified interface. Automatic differentiation and Laplace
approximation follow Kristensen et al. (2016) <doi:10.18637/jss.v070.i05>,
and MCMC sampling uses the No-U-Turn Sampler described by Hoffman and
Gelman (2014) <https://jmlr.org/papers/v15/hoffman14a.html>.

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
