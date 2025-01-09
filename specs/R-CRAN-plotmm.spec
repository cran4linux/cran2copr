%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plotmm
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Tools for Visualizing Mixture Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-wesanderson 
BuildRequires:    R-CRAN-amerika 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-EMCluster 
BuildRequires:    R-CRAN-flexmix 
Requires:         R-methods 
Requires:         R-CRAN-wesanderson 
Requires:         R-CRAN-amerika 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-EMCluster 
Requires:         R-CRAN-flexmix 

%description
The main function, plot_mm(), is used for (gg)plotting output from mixture
models, including both densities and overlaying mixture weight component
curves from the fit models in line with the tidy principles. The package
includes several additional functions for added plot customization.
Supported model objects include: 'mixtools', 'EMCluster', and 'flexmix',
with more from each in active dev. Supported mixture model specifications
include mixtures of univariate Gaussians, multivariate Gaussians, Gammas,
logistic regressions, linear regressions, and Poisson regressions.

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
