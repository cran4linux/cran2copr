%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  harmonicmeanp
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Harmonic Mean p-Values and Model Averaging by Mean Maximum Likelihood

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FMStable 
Requires:         R-CRAN-FMStable 

%description
The harmonic mean p-value (HMP) test combines p-values and corrects for
multiple testing while controlling the strong-sense family-wise error
rate. It is more powerful than common alternatives including Bonferroni
and Simes procedures when combining large proportions of all the p-values,
at the cost of slightly lower power when combining small proportions of
all the p-values. It is more stringent than controlling the false
discovery rate, and possesses theoretical robustness to positive
correlations between tests and unequal weights. It is a multi-level test
in the sense that a superset of one or more significant tests is certain
to be significant and conversely when the superset is non-significant, the
constituent tests are certain to be non-significant. It is based on MAMML
(model averaging by mean maximum likelihood), a frequentist analogue to
Bayesian model averaging, and is theoretically grounded in generalized
central limit theorem. For detailed examples type
vignette("harmonicmeanp") after installation. Version 3.0 addresses errors
in versions 1.0 and 2.0 that led function p.hmp to control the familywise
error rate only in the weak sense, rather than the strong sense as
intended.

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
