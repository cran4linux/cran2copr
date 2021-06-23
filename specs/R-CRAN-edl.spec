%global __brp_check_rpaths %{nil}
%global packname  edl
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Toolbox for Error-Driven Learning Simulations with Two-Layer Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotfunctions >= 1.4
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-plotfunctions >= 1.4
Requires:         R-CRAN-data.table 

%description
Error-driven learning (based on the Widrow & Hoff
(1960)<https://isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf>
learning rule, and essentially the same as Rescorla-Wagner's learning
equations (Rescorla & Wagner, 1972, ISBN: 0390718017), which are also at
the core of Naive Discrimination Learning, (Baayen et al, 2011,
<doi:10.1037/a0023851>) can be used to explain bottom-up human learning
(Hoppe et al, <doi:10.31234/osf.io/py5kd>), but is also at the core of
artificial neural networks applications in the form of the Delta rule.
This package provides a set of functions for building small-scale
simulations to investigate the dynamics of error-driven learning and it's
interaction with the structure of the input. For modeling error-driven
learning using the Rescorla-Wagner equations the package 'ndl' (Baayen et
al, 2011, <doi:10.1037/a0023851>) is available on CRAN at
<https://cran.r-project.org/package=ndl>. However, the package currently
only allows tracing of a cue-outcome combination, rather than returning
the learned networks. To fill this gap, we implemented a new package with
a few functions that facilitate inspection of the networks for small error
driven learning simulations. Note that our functions are not optimized for
training large data sets (no parallel processing), as they are intended
for small scale simulations and course examples. (Consider the python
implementation 'pyndl' <https://pyndl.readthedocs.io/en/latest/> for that
purpose.)

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
