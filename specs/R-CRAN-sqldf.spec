%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sqldf
%global packver   0.4-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.12
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulate R Data Frames Using SQL

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gsubfn >= 0.6
BuildRequires:    R-CRAN-proto 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-chron 
Requires:         R-CRAN-gsubfn >= 0.6
Requires:         R-CRAN-proto 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-chron 

%description
The sqldf() function is typically passed a single argument which is an SQL
select statement where the table names are ordinary R data frame names.
sqldf() transparently sets up a database, imports the data frames into
that database, performs the SQL select or other statement and returns the
result using a heuristic to determine which class to assign to each column
of the returned data frame.  The sqldf() or read.csv.sql() functions can
also be used to read filtered files into R even if the original files are
larger than R itself can handle. 'RSQLite', 'RH2', 'RMySQL' and
'RPostgreSQL' backends are supported.

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
