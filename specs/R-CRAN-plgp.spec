%global __brp_check_rpaths %{nil}
%global packname  plgp
%global packver   1.1-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Particle Learning of Gaussian Processes

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4
Requires:         R-core >= 2.4
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tgp 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tgp 

%description
Sequential Monte Carlo (SMC) inference for fully Bayesian Gaussian process
(GP) regression and classification models by particle learning (PL)
following Gramacy & Polson (2011) <arXiv:0909.5262>. The sequential nature
of inference and the active learning (AL) hooks provided facilitate
thrifty sequential design (by entropy) and optimization (by improvement)
for classification and regression models, respectively. This package
essentially provides a generic PL interface, and functions (arguments to
the interface) which implement the GP models and AL heuristics.  Functions
for a special, linked, regression/classification GP model and an
integrated expected conditional improvement (IECI) statistic provide for
optimization in the presence of unknown constraints. Separable and
isotropic Gaussian, and single-index correlation functions are supported.
See the examples section of ?plgp and demo(package="plgp") for an index of
demos.

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
