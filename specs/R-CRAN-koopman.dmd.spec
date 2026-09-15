%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  koopman.dmd
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Koopman Operator and Dynamic Mode Decomposition for Dynamical Systems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0

%description
Dynamic Mode Decomposition (DMD) with Koopman operator theory extensions,
powered by a Rust backend via 'extendr'. Provides standard DMD as
described in Schmid (2010) <doi:10.1017/S0022112010001217>, DMD with
control for forced linear systems following Proctor, Brunton, and Kutz
(2016) <doi:10.1137/15M1013857>, Extended DMD with lifting functions,
Hankel-DMD via time-delay embedding, Generalized Laplace Analysis for
direct eigenfunction computation, and harmonic time averages and
mesochronic harmonic plots for phase space analysis as developed in Mezic
(2020) <doi:10.48550/arXiv.2009.05883>. Includes built-in area-preserving
and chaotic maps for experimentation.

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
