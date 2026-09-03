%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BKVerify
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Consistency Auditing of Reported Plant Breeding Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Audits published or draft plant breeding tables for internal arithmetic
consistency. Analysis of variance tables, precision statistics and genetic
variability parameters are jointly over-determined by exact algebraic
identities; 'BKVerify' recomputes every derivable quantity using
rounding-interval arithmetic and reports a value as inconsistent only when
no combination of values inside the reported rounding intervals can
satisfy the identity. The package deliberately restricts itself to
relationships that hold irrespective of which variance-component
definition an author adopted, so that flagged results reflect arithmetic
inconsistency rather than methodological disagreement. Implemented checks
cover analysis of variance internal structure, coefficient of variation,
standard error of mean and critical difference, the genetic advance
identity of Johnson, Robinson and Comstock (1955)
<doi:10.2134/agronj1955.00021962004700070009x>, the relation between
genotypic and phenotypic coefficients of variation and broad-sense
heritability, and admissibility of reported correlation matrices.

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
