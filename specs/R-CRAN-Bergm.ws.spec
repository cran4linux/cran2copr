%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Bergm.ws
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Multi-Layer ERGMs for Weighted and Signed Weighted Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm >= 4.6.0
BuildRequires:    R-CRAN-ergm.multi >= 0.2.0
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ergm >= 4.6.0
Requires:         R-CRAN-ergm.multi >= 0.2.0
Requires:         R-CRAN-network 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-parallel 

%description
Bayesian hierarchical multi-layer dissolution exponential random graph
models for weighted and signed weighted networks. A weighted network is
decomposed into nested binary layers by thresholding its edge weights, and
each transition between consecutive layers is modelled conditionally on
the observed lower layers: on the layers alone with bergm_w(), or jointly
with the edge signs with bergm_ws(). Layer-specific parameters are
partially pooled through a Normal-inverse-Wishart hierarchical prior and
estimated with an adaptive approximate exchange algorithm: joint or
layer-wise updates, delayed acceptance with a Gaussian approximation of
the likelihood, the hierarchical mean integrated out of the exchange step,
and a proposal covariance initialised from the Fisher information, learned
during the burn-in and pooled across chains. The package also provides a
model builder that checks that every statistic is computed on its own
layer, prior and posterior predictive checks with goodness-of-fit
statistics not used in the model, convergence diagnostics and a check of
the length of the auxiliary chains.

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
