%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  globpso
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Swarm Intelligence Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-RcppArmadillo >= 0.12.6.6.1
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-RcppArmadillo >= 0.12.6.6.1
Requires:         R-methods 
Requires:         R-utils 

%description
A fast and flexible general-purpose implementation of Particle Swarm
Optimization (PSO) and Differential Evolution (DE) for solving global
minimization problems is provided. It is designed to handle complex
optimization tasks with nonlinear, non-differentiable, and multi-modal
objective functions defined by users. There are five types of PSO
variants: Particle Swarm Optimization (PSO, Eberhart & Kennedy, 1995)
<doi:10.1109/MHS.1995.494215>, Quantum-behaved particle Swarm Optimization
(QPSO, Sun et al., 2004) <doi:10.1109/CEC.2004.1330875>, Locally
convergent rotationally invariant particle swarm optimization (LcRiPSO,
Bonyadi & Michalewicz, 2014) <doi:10.1007/s11721-014-0095-1>, Competitive
Swarm Optimizer (CSO, Cheng & Jin, 2015) <doi:10.1109/TCYB.2014.2322602>
and Double exponential particle swarm optimization (DExPSO, Stehlik et
al., 2024) <doi:10.1016/j.asoc.2024.111913>. For the DE algorithm, six
types in Storn, R. & Price, K. (1997) <doi:10.1023/A:1008202821328> are
included: DE/rand/1, DE/rand/2, DE/best/1, DE/best/2, DE/rand_to-best/1
and DE/rand_to-best/2.

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
