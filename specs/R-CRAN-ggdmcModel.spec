%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggdmcModel
%global packver   0.2.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Builders for 'ggdmc' Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.7.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggdmcHeaders 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-methods 

%description
A suite of tools for specifying and examining experimental designs related
to choice response time models (e.g., the Diffusion Decision Model). This
package allows users to define how experimental factors influence one or
more model parameters using R-style formula syntax, while also checking
the logical consistency of these associations. Additionally, it integrates
with the 'ggdmc' package, which employs Differential Evolution Markov
Chain Monte Carlo (DE-MCMC) sampling to optimise model parameters. For
further details on the model-building approach, see Heathcote, Lin,
Reynolds, Strickland, Gretton, and Matzke (2019)
<doi:10.3758/s13428-018-1067-y>.

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
