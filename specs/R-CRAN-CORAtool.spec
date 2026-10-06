%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CORAtool
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Combinational Regularity Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Searches configurational data for causes that are each an insufficient but
non-redundant part of an unnecessary but sufficient (INUS) condition for
their effect, so that cause-effect relations are marked by conjunctivity
and disjunctivity. The method, Combinational Regularity Analysis (CORA),
borrows its Boolean minimisation algorithms from switching circuit
analysis. Truth tables are minimised either with the classical
Quine-McCluskey algorithm over positive and don't care terms or with
McCluskey's modified algorithm over positive and negative terms, and the
resulting prime implicant charts are solved with Petrick's method.
Multi-value conditions and structures with simple as well as complex
effects are supported, together with a configurational data-mining search
and two-level logic diagrams. The package is an R port of the 'Python'
packages 'CORA' and 'LOGIGRAM' described in Sebechlebská, Mkrtchyan and
Thiem (2023) <doi:10.21105/joss.05019>; it computes in plain R and
requires no 'Python' installation. It is an independent implementation and
is not endorsed by the authors of the original packages.

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
