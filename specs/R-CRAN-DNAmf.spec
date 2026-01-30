%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DNAmf
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Diffusion Non-Additive Model with Tunable Precision

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plgp 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-plgp 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-mvtnorm 

%description
Performs Diffusion Non-Additive (DNA) model proposed by Heo, Boutelet, and
Sung (2025+) <doi:10.48550/arXiv.2506.08328> for multi-fidelity computer
experiments with tuning parameters. The DNA model captures nonlinear
dependencies across fidelity levels using Gaussian process priors and is
particularly effective when simulations at different fidelity levels are
nonlinearly correlated. The DNA model targets not only interpolation
across given fidelity levels but also extrapolation to smaller tuning
parameters including the exact solution corresponding to a zero-valued
tuning parameter, leveraging a nonseparable covariance kernel structure
that models interactions between the tuning parameter and input variables.
Closed-form expressions for the predictive mean and variance enable
efficient inference and uncertainty quantification. Hyperparameters in the
model are estimated via maximum likelihood estimation.

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
