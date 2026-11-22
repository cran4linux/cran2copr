%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Stem
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Expectation-Maximization Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-spdep 
Requires:         R-stats 

%description
Estimation of hierarchical spatio-temporal models through the
Expectation-Maximization (EM) algorithm within a likelihood-based
framework, following Fasso and Cameletti (2010)
<doi:10.1177/0037549709102150> and the heterogeneous-network model of
Fasso, Cameletti and Nicolis (2007) <doi:10.1002/env.837>, with the EM
machinery of McLachlan and Krishnan (2008, ISBN:9780470191613). Parameters
are estimated by maximum likelihood via Kalman filtering and smoothing;
standard errors and spatial prediction uncertainty are obtained by a
spatio-temporal parametric bootstrap. The package also provides the
spatially-clustered STEM (SC-STEM) models, an extension in which
regression coefficients, variance components and latent dynamics vary
across spatial regimes estimated from the data by maximizing a
Potts-penalized likelihood, in the spirit of the spatially-clustered
regression of Sugasawa and Murakami (2021)
<doi:10.1016/j.spasta.2021.100525> and of the spatially-clustered spatial
autoregressive models of Cerqueti, Maranzano and Mattera (2025)
<doi:10.1007/s13253-025-00685-7>. SC-STEM comes with likelihood-based
information criteria, a two-step rule based on the Bayesian information
criterion for selecting the number of regimes and the spatial penalty, and
a refit-with-clustering parametric bootstrap that propagates the
uncertainty of the estimated partition into intervals and tests.

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
