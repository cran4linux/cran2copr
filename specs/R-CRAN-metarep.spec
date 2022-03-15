%global __brp_check_rpaths %{nil}
%global packname  metarep
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Replicability-Analysis Tools for Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 4.9.10
Requires:         R-CRAN-meta >= 4.9.10

%description
User-friendly package for reporting replicability-analysis methods,
affixed to meta-analyses summary. This package implements the methods
introduced in Jaljuli et. al. (2022) <doi:10.1080/19466315.2022.2050291>.
The replicability-analysis output provides an assessment of the
investigated intervention, where it offers quantification of effect
replicability and assessment of the consistency of findings. -
Replicability-analysis for fixed-effects and random-effect meta analysis:
- r(u)-value; - lower bounds on the number of studies with replicated
positive andor negative effect; - Allows detecting inconsistency of
signals; - forest plots with the summary of replicability analysis
results; - Allows Replicability-analysis with or without the common-effect
assumption.

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
