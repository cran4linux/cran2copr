%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prt
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tabular Data Backed by Partitioned 'fst' Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pillar >= 1.7.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-pillar >= 1.7.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-backports 
Requires:         R-CRAN-rlang 

%description
Intended for larger-than-memory tabular data, 'prt' objects provide an
interface to read row and/or column subsets into memory as data.table
objects. Data queries, constructed as 'R' expressions, are evaluated using
the non-standard evaluation framework provided by 'rlang' and file-backing
is powered by the fast and efficient 'fst' package.

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
