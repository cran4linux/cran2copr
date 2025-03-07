%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  restez
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Create and Query a Local Copy of 'GenBank' in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rentrez 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-utils 
Requires:         R-CRAN-rentrez 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-ape 

%description
Download large sections of 'GenBank'
<https://www.ncbi.nlm.nih.gov/genbank/> and generate a local SQL-based
database. A user can then query this database using 'restez' functions or
through 'rentrez' <https://CRAN.R-project.org/package=rentrez> wrappers.

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
