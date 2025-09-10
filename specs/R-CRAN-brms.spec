%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  brms
%global packver   2.23.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.23.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Regression Models using 'Stan'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-loo >= 2.8.0
BuildRequires:    R-CRAN-rstan >= 2.29.0
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-mgcv >= 1.8.13
BuildRequires:    R-CRAN-posterior >= 1.6.0
BuildRequires:    R-CRAN-bayesplot >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-future >= 1.19.0
BuildRequires:    R-CRAN-Matrix >= 1.1.1
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-future.apply >= 1.0.0
BuildRequires:    R-CRAN-bridgesampling >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-loo >= 2.8.0
Requires:         R-CRAN-rstan >= 2.29.0
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-mgcv >= 1.8.13
Requires:         R-CRAN-posterior >= 1.6.0
Requires:         R-CRAN-bayesplot >= 1.5.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-future >= 1.19.0
Requires:         R-CRAN-Matrix >= 1.1.1
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-future.apply >= 1.0.0
Requires:         R-CRAN-bridgesampling >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-abind 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-grDevices 
Requires:         R-CRAN-backports 
Requires:         R-CRAN-rstantools

%description
Fit Bayesian generalized (non-)linear multivariate multilevel models using
'Stan' for full Bayesian inference. A wide range of distributions and link
functions are supported, allowing users to fit -- among others -- linear,
robust linear, count data, survival, response times, ordinal,
zero-inflated, hurdle, and even self-defined mixture models all in a
multilevel context. Further modeling options include both theory-driven
and data-driven non-linear terms, auto-correlation structures, censoring
and truncation, meta-analytic standard errors, and quite a few more. In
addition, all parameters of the response distribution can be predicted in
order to perform distributional regression. Prior specifications are
flexible and explicitly encourage users to apply prior distributions that
actually reflect their prior knowledge. Models can easily be evaluated and
compared using several methods assessing posterior or prior predictions.
References: Bürkner (2017) <doi:10.18637/jss.v080.i01>; Bürkner (2018)
<doi:10.32614/RJ-2018-017>; Bürkner (2021) <doi:10.18637/jss.v100.i05>;
Carpenter et al. (2017) <doi:10.18637/jss.v076.i01>.

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
