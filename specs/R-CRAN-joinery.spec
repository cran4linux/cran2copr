%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  joinery
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Heuristic Index-Based Record Linkage

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-phonics 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tinyplot 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-S7 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-phonics 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tinyplot 
Requires:         R-graphics 

%description
Links records that refer to the same entity across sources that share no
common key, such as people, firms, or addresses with spelling variation,
abbreviations, or reordered words. Linkage is described declaratively as a
strategy that normalises, tokenises, phonetically encodes, weights, and
blocks each field; candidate pairs are then scored by the rarity-weighted
overlap of their tokens and every score is attributed back to individual
tokens for explainability. Strategies compose into staged pipelines of
exact, fuzzy, and optional embedding-based matching that carry unmatched
records forward and resolve entities as connected components. The same
strategy runs on an in-memory 'data.table' backend or an out-of-core
'DuckDB' backend, and diagnostic and calibration tools help tune a
strategy and filter false positives. The token-retrieval heuristic follows
Doherr (2023) <doi:10.2139/ssrn.4326848>.

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
