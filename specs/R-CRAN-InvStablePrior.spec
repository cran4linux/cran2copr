%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  InvStablePrior
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inverse Stable Prior for Widely-Used Exponential Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-nimble 
Requires:         R-stats 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-nimble 

%description
Contains functions that allow Bayesian inference on a parameter of some
widely-used exponential models. The functions can generate independent
samples from the closed-form posterior distribution using the inverse
stable prior. Inverse stable is a non-conjugate prior for a parameter of
an exponential subclass of discrete and continuous data distributions
(e.g. Poisson, exponential, inverse gamma, double exponential (Laplace),
half-normal/half-Gaussian, etc.). The prior class provides flexibility in
capturing a wide array of prior beliefs (right-skewed and left-skewed) as
modulated by a parameter that is bounded in (0,1). The generated samples
can be used to simulate the prior and posterior predictive distributions.
More details can be found in Cahoy and Sedransk (2019)
<doi:10.1007/s42519-018-0027-2>. The package can also be used as a
teaching demo for introductory Bayesian courses.

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
