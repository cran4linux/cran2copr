%global packname  tcl
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Testing in Conditional Likelihood Context

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-eRm 
BuildRequires:    R-CRAN-psychotools 
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-eRm 
Requires:         R-CRAN-psychotools 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-numDeriv 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-splines 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-psych 

%description
An implementation of hypothesis testing in an extended Rasch modelling
framework, including sample size planning procedures and power
computations. Provides 4 statistical tests, i.e., gradient test (GR),
likelihood ratio test (LR), Rao score or Lagrange multiplier test (RS),
and Wald test, for testing a number of hypotheses referring to the Rasch
model (RM), linear logistic test model (LLTM), rating scale model (RSM),
and partial credit model (PCM). Three types of functions for power and
sample size computations are provided. Firstly, functions to compute the
sample size given a user-specified (predetermined) deviation from the
hypothesis to be tested, the level alpha, and the power of the test.
Secondly, functions to evaluate the power of the tests given a
user-specified (predetermined) deviation from the hypothesis to be tested,
the level alpha of the test, and the sample size. Thirdly, functions to
evaluate the so-called post hoc power of the tests. This is the power of
the tests given the observed deviation of the data from the hypothesis to
be tested and a user-specified level alpha of the test. Power and sample
size computations are based on a Monte Carlo simulation approach. It is
computationally very efficient. The variance of the random error in
computing power and sample size arising from the simulation approach is
analytically derived by using the delta method. Draxler, C., &
Alexandrowicz, R. W. (2015), <doi:10.1007/s11336-015-9472-y>.

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
