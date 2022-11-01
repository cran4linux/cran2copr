%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spate
%global packver   1.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Modeling of Large Data Using a Spectral SPDE Approach

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-truncnorm 

%description
Functionality for spatio-temporal modeling of large data sets is provided.
A Gaussian process in space and time is defined through a stochastic
partial differential equation (SPDE). The SPDE is solved in the spectral
space, and after discretizing in time and space, a linear Gaussian state
space model is obtained. When doing inference, the main computational
difficulty consists in evaluating the likelihood and in sampling from the
full conditional of the spectral coefficients, or equivalently, the latent
space-time process. In comparison to the traditional approach of using a
spatio-temporal covariance function, the spectral SPDE approach is
computationally advantageous. See Sigrist, Kuensch, and Stahel (2015)
<doi:10.1111/rssb.12061> for more information on the methodology. This
package aims at providing tools for two different modeling approaches.
First, the SPDE based spatio-temporal model can be used as a component in
a customized hierarchical Bayesian model (HBM). The functions of the
package then provide parameterizations of the process part of the model as
well as computationally efficient algorithms needed for doing inference
with the HBM. Alternatively, the adaptive MCMC algorithm implemented in
the package can be used as an algorithm for doing inference without any
additional modeling. The MCMC algorithm supports data that follow a
Gaussian or a censored distribution with point mass at zero. Covariates
can be included in the model through a regression term.

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
