%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gbifdb
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          High Performance Interface to 'GBIF'

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow >= 8.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-duckdbfs 
Requires:         R-CRAN-arrow >= 8.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-duckdbfs 

%description
A high performance interface to the Global Biodiversity Information
Facility, 'GBIF'.  In contrast to 'rgbif', which can access small subsets
of 'GBIF' data through web-based queries to a central server, 'gbifdb'
provides enhanced performance for R users performing large-scale analyses
on servers and cloud computing providers, providing full support for
arbitrary 'SQL' or 'dplyr' operations on the complete 'GBIF' data tables
(now over 1 billion records, and over a terabyte in size). 'gbifdb'
accesses a copy of the 'GBIF' data in 'parquet' format, which is already
readily available in commercial computing clouds such as the Amazon Open
Data portal and the Microsoft Planetary Computer, or can be accessed
directly without downloading, or downloaded to any server with suitable
bandwidth and storage space. The high-performance techniques for local and
remote access are described in <https://duckdb.org/why_duckdb> and
<https://arrow.apache.org/docs/r/articles/fs.html> respectively.

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
