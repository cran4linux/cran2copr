%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spStack
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Geostatistics Using Predictive Stacking

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MBA 
Requires:         R-CRAN-rstudioapi 

%description
Fits Bayesian hierarchical spatial and spatial-temporal process models for
point-referenced Gaussian, Poisson, binomial, and binary data using
stacking of predictive densities. It involves sampling from analytically
available posterior distributions conditional upon candidate values of the
spatial process parameters and, subsequently assimilate inference from
these individual posterior distributions using Bayesian predictive
stacking. Our algorithm is highly parallelizable and hence, much faster
than traditional Markov chain Monte Carlo algorithms while delivering
competitive predictive performance. See Zhang, Tang, and Banerjee (2025)
<doi:10.48550/arXiv.2304.12414>, and, Pan, Zhang, Bradley, and Banerjee
(2025) <doi:10.48550/arXiv.2406.04655> for details.

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
