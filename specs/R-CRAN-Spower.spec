%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Spower
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analyses using Monte Carlo Simulations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SimDesign >= 2.20.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cocor 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-EnvStats 
Requires:         R-CRAN-SimDesign >= 2.20.0
Requires:         R-stats 
Requires:         R-CRAN-cocor 
Requires:         R-CRAN-car 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-parallelly 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-EnvStats 

%description
Provides a general purpose simulation-based power analysis API for routine
and customized simulation experimental designs. The package focuses
exclusively on Monte Carlo simulation experiment variants of (expected)
prospective power analyses, criterion analyses, compromise analyses,
sensitivity analyses, and a priori/post-hoc analyses. The default
simulation experiment functions defined within the package provide
stochastic variants of the power analysis subroutines in G*Power 3.1
(Faul, Erdfelder, Buchner, and Lang, 2009) <doi:10.3758/brm.41.4.1149>,
along with various other parametric and non-parametric power analysis
applications (e.g., mediation analyses) and support for Bayesian power
analysis by way of Bayes factors or posterior probability evaluations.
Additional functions for building empirical power curves, reanalyzing
simulation information, and for increasing the precision of the resulting
power estimates are also included, each of which utilize similar API
structures.

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
