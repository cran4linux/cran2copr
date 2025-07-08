%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggdmcHeaders
%global packver   0.2.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          'C++' Headers for 'ggdmc' Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A fast 'C++' implementation of the design-based, Diffusion Decision Model
(DDM) and the Linear Ballistic Accumulation (LBA) model. It enables the
user to optimise the choice response time model by connecting with the
Differential Evolution Markov Chain Monte Carlo (DE-MCMC) sampler
implemented in the 'ggdmc' package. The package fuses the hierarchical
modelling, Bayesian inference, choice response time models and factorial
designs, allowing users to build their own design-based models. For more
information on the underlying models, see the works by Voss, Rothermund,
and Voss (2004) <doi:10.3758/BF03196893>, Ratcliff and McKoon (2008)
<doi:10.1162/neco.2008.12-06-420>, and Brown and Heathcote (2008)
<doi:10.1016/j.cogpsych.2007.12.002>.

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
