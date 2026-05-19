%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JM4QTN
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Mapping for Quantitative Trait Loci

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lsmeans >= 2.25.5
BuildRequires:    R-CRAN-StepReg >= 1.5.0
Requires:         R-CRAN-lsmeans >= 2.25.5
Requires:         R-CRAN-StepReg >= 1.5.0

%description
A comprehensive computational framework for joint mapping, developed by Li
(2016) <doi:10.11841/j.issn.1007-4333.2016.06.002>, supports quantitative
trait locus detection in structured genetic populations. It integrates
robust phenotype summarization, computes genotype probabilities, and
imputes missing markers for association and linkage mapping. Empirical
significance thresholds are estimated via permutation testing coupled with
stepwise regression. The framework enables genome-wide scans under both
univariate and multivariate trait models, streamlining the discovery of
complex genetic architectures.

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
