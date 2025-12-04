%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VGAM
%global packver   1.1-14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.14
Release:          1%{?dist}%{?buildtag}
Summary:          Vector Generalized Linear and Additive Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-splines 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-splines 

%description
An implementation of about 6 major classes of statistical regression
models. The central algorithm is Fisher scoring and iterative reweighted
least squares. At the heart of this package are the vector generalized
linear and additive model (VGLM/VGAM) classes. VGLMs can be loosely
thought of as multivariate GLMs. VGAMs are data-driven VGLMs that use
smoothing. The book "Vector Generalized Linear and Additive Models: With
an Implementation in R" (Yee, 2015) <DOI:10.1007/978-1-4939-2818-7> gives
details of the statistical framework and the package. Currently only
fixed-effects models are implemented. Many (100+) models and distributions
are estimated by maximum likelihood estimation (MLE) or penalized MLE. The
other classes are RR-VGLMs (reduced-rank VGLMs), quadratic RR-VGLMs,
doubly constrained RR-VGLMs, quadratic RR-VGLMs, reduced-rank VGAMs, RCIMs
(row-column interaction models)---these classes perform constrained and
unconstrained quadratic ordination (CQO/UQO) models in ecology, as well as
constrained additive ordination (CAO). Hauck-Donner effect detection is
implemented. Note that these functions are subject to change; see the NEWS
and ChangeLog files for latest changes.

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
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
