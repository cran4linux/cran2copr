%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSEML
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Case-Based Least Squares Estimation of Nonlinear Structural Equation Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RTMB 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-stats 
Requires:         R-CRAN-RTMB 
Requires:         R-CRAN-nloptr 
Requires:         R-stats 

%description
Estimates structural equation models by case-based least squares: the
latent scores of every observation are treated as free variables of a
constrained optimization problem, so that arbitrary nonlinear model
equations, bounds and constraints on latent variables and inequality
constraints on parameters become possible.  Model equations are specified
as plain text (e.g. "y == a*exp(b*eta)"). Gradients are obtained by
automatic differentiation via 'RTMB', and the constrained problem is
solved with 'nloptr' (SLSQP or augmented Lagrangian).  Missing data are
handled case-wise.  The methodology is described in Oldenburg (2024)
<doi:10.19139/soic-2310-5070-1868> and Oldenburg (2025)
<doi:10.19139/soic-2310-5070-2324>.

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
