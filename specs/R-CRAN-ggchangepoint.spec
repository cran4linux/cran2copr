%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggchangepoint
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Combines Changepoint Analysis with 'ggplot2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-changepoint.np 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ecp 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-changepoint.np 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ecp 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
A unified, tidy, 'ggplot2'-native interface to changepoint detection in R.
Provides the 'ggcpt' S3 result class with 'broom'-style
tidy/glance/augment methods, 'autoplot()' (with confidence intervals,
significance regions, detector statistics, solution paths, scale space,
and multivariate facets), composable geoms ('geom_changepoint()',
'geom_cpt_segment()', 'geom_cpt_ci()', 'geom_cpt_region()',
'geom_cpt_label()', 'geom_cpt_event()', 'stat_changepoint()'), and a
'cpt_detect()' dispatcher covering fifty methods with introspection via
'cpt_methods()': penalised/optimal partitioning, multiscale and search
methods, nonparametric and kernel methods, Bayesian methods,
high-dimensional, functional, covariance and network methods, regression
breaks, seasonal-trend decomposition, the classical single-change tests,
and robust detection under drift and autocorrelation. Adds inference
(Narrowest Significance Pursuit regions, a unified 'cpt_confint()',
post-detection tests), selection of the number of changes, influence and
sensitivity diagnostics, supervised detection with learned penalties,
consensus and method recommendation, event annotation and reproducible
reports, benchmarks against the Turing Change Point Dataset, sequential
monitoring with detection-delay accounting, power and study design, and an
extension mechanism ('as_ggcpt()', 'cpt_register_method()') that brings
external and non-CRAN detectors into the same grammar.

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
