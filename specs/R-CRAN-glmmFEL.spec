%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmmFEL
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Linear Mixed Models via Fully Exponential Laplace in EM

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-methods 

%description
Fit generalized linear mixed models (GLMMs) with normal random effects
using first-order Laplace, fully exponential Laplace (FEL) with mean-only
corrections, and FEL with mean and covariance corrections in the E-step of
an expectation-maximization (EM) algorithm. The current development
version provides a matrix-based interface (y, X, Z) and supports binary
logit and probit, and Poisson log-link models. An EM framework is used to
update fixed effects, random effects, and a single variance component
tau^2 for G = tau^2 I, with staged approximations (Laplace -> FEL
mean-only -> FEL full) for efficiency and stability. A pseudo-likelihood
engine glmmFEL_pl() implements the working-response / working-weights
linearization approach of Wolfinger and O'Connell (1993)
<doi:10.1080/00949659308811554>, and is adapted from the implementation
used in the 'RealVAMS' package (Broatch, Green, and Karl (2018))
<doi:10.32614/RJ-2018-033>. The FEL implementation follows Karl, Yang, and
Lohr (2014) <doi:10.1016/j.csda.2013.11.019> and related work (e.g.,
Tierney, Kass, and Kadane (1989) <doi:10.1080/01621459.1989.10478824>;
Rizopoulos, Verbeke, and Lesaffre (2009)
<doi:10.1111/j.1467-9868.2008.00704.x>; Steele (1996)
<doi:10.2307/2532845>). Package code was drafted with assistance from
generative AI tools.

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
