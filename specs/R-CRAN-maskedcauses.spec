%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  maskedcauses
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood Models for Systems with Masked Component Cause of Failure

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-likelihood.model 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-likelihood.model 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-numDeriv 

%description
Maximum likelihood estimation for series systems where the component cause
of failure is masked. Implements analytical log-likelihood, score, and
Hessian functions for exponential, homogeneous Weibull, and heterogeneous
Weibull component lifetimes under masked cause conditions (C1, C2, C3).
Supports exact, right-censored, left-censored, and interval-censored
observations via composable observation functors. Provides random data
generation, model fitting, and Fisher information for asymptotic
inference. See Lin, Loh, and Bai (1993) <doi:10.1109/24.257799> and Craiu
and Reiser (2006) <doi:10.1111/j.1541-0420.2005.00498.x>.

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
