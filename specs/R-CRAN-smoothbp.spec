%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smoothbp
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Piecewise Regression with Smoothed Change-Points

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-bayesplot 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-bridgesampling 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-bayesplot 

%description
Fits Bayesian hierarchical piecewise regression models with multiple
logistic-smoothed change-points. Non-linear parameters (change-point
locations and transition sharpness) and linear parameters can each be
conditioned on covariates and factors via flexible design matrices. A
random-intercept structure is supported for any parameter. Spike-and-slab
regularization is supported for selecting the number of breakpoints.
Posterior inference uses a Metropolis-within-Gibbs sampler implemented in
'Rust' for speed. Methods are based on the smooth transition piecewise
regression model of Bacon and Watts (1971) <doi:10.2307/2334389> and
variable selection spike-and-slab priors of Kuo and Mallick (1998)
<https://www.jstor.org/stable/25053023>.

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
