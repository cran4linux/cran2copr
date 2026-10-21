%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  solvency2
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Offline Solvency II Calculations and Regulatory Parameters

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-xml2 

%description
Native, offline components for insurance solvency calculations under
Solvency II, including valuation, technical provisions, market and
underwriting risks, capital aggregation, own funds, groups and archived
reporting checks. Provides explicit dated rule profiles, regulatory
parameters, correlation matrices, synthetic reference cases, local
discount curve adapters and traceable analyst overrides. Implements
components of Directive 2009/138/EC, European Parliament and Council
(2009) <https://eur-lex.europa.eu/eli/dir/2009/138/oj>, and Delegated
Regulation (EU) 2015/35, European Commission (2014)
<https://eur-lex.europa.eu/eli/reg_del/2015/35/oj>. Users provide
portfolio inputs, market observations and model results; no network
connection or 'Python' runtime is required.

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
