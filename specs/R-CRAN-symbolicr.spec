%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  symbolicr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Symbolic Regression Framework

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-RcppAlgos 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-RcppAlgos 
Requires:         R-stats 
Requires:         R-CRAN-stringr 

%description
Find non-linear formulas that fits your input data. You can systematically
explore and memorize the possible formulas and it's cross-validation
performance, in an incremental fashion. Three main interoperable search
functions are available: 1) random.search() performs a random exploration,
2) genetic.search() employs a genetic optimization algorithm, 3)
comb.search() combines best results of the first two. For more details see
Tomasoni et al. (2026) <doi:10.1208/s12248-026-01232-z>.

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
