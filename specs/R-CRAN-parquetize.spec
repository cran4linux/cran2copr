%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  parquetize
%global packver   0.5.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Convert Files to Parquet Format

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-lifecycle 
Requires:         R-tools 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-dplyr 

%description
Collection of functions to get files in parquet format. Parquet is a
columnar storage file format <https://parquet.apache.org/>. The files to
convert can be of several formats ("csv", "RData", "rds", "RSQLite",
"json", "ndjson", "SAS", "SPSS"...).

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
