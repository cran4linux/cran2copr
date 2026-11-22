%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayGMST
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Reconstruction of Global Mean Surface Temperature

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-instantiate 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-instantiate 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
Fits a Bayesian hierarchical AR(1)-driven state-space model relating
annual global mean surface temperature (GMST) to a reduced paleoclimate
proxy (computed from cached or user-specified paleoclimate multi-proxy
network data), instrumental temperature observations, and radiative
forcings (greenhouse gases, volcanic aerosols, and solar irradiance).
Unobserved pre-instrumental temperatures are estimated jointly with the
model parameters using 'Stan' via the 'instantiate' and 'cmdstanr'
packages. Includes tools to reduce a multi-proxy network to a single
representative proxy series (via principal component regression, partial
least squares, LASSO, or supervised PCR), estimate the parameters in the
reconstruction model, run k-fold cross-validation, provide uncertainty
quantification on the reconstructed temperatures, and visualize
reconstructions and posterior draws. The model and methods follow Barboza
et al. (2014) <doi:10.1214/14-AOAS785>, Barboza et al. (2019)
<doi:10.1007/s13253-019-00372-4>, and Wang (2020)
<doi:10.25335/vb7s-rh49>.

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
