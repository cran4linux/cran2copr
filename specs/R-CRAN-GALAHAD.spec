%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GALAHAD
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geometry-Adaptive Lyapunov-Assured Hybrid Optimizer with Softplus Reparameterization and Trust-Region Control

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements the GALAHAD algorithm (Geometry-Adaptive Lyapunov-Assured
Hybrid Optimizer), updated in version 2 to replace the hard-clamp
positivity constraint of v1 with a numerically smooth softplus
reparameterization, add rho-based trust-region adaptation (actual vs.
predicted objective reduction), extend convergence detection to include
both absolute and relative function-stall criteria, and enrich the
per-iteration history with Armijo backtrack counts and trust-region
quality ratios. Parameters constrained to be positive (rates,
concentrations, scale parameters) are handled in a transformed z-space via
the softplus map so that gradients remain well-defined at the constraint
boundary. A two-partition API (positive / euclidean) replaces the
three-way T/P/E partition of v1; the legacy form is still accepted for
backwards compatibility. Designed for biological modeling problems
(germination, dose-response, prion RT-QuIC, survival) where rates,
concentrations, and unconstrained coefficients coexist. Developed at the
Minnesota Center for Prion Research and Outreach (MNPRO), University of
Minnesota. Based on Conn et al. (2000) <doi:10.1137/1.9780898719857>,
Barzilai and Borwein (1988) <doi:10.1093/imanum/8.1.141>, Xu and An (2024)
<doi:10.48550/arXiv.2409.14383>, Polyak (1969)
<doi:10.1016/0041-5553(69)90035-4>, Nocedal and Wright (2006,
ISBN:978-0-387-30303-1), and Dugas et al. (2009)
<https://www.jmlr.org/papers/v10/dugas09a.html>.

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
