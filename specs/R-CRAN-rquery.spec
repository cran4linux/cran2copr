%global packname  rquery
%global packver   1.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Relational Query Generator for Data Manipulation at Scale

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wrapr >= 2.0.2
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-wrapr >= 2.0.2
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 

%description
A piped query generator based on Edgar F. Codd's relational algebra, and
on production experience using 'SQL' and 'dplyr' at big data scale.  The
design represents an attempt to make 'SQL' more teachable by denoting
composition by a sequential pipeline notation instead of nested queries or
functions.  The implementation delivers reliable high performance data
processing on large data systems such as 'Spark', databases, and
'data.table'. Package features include: data processing trees or pipelines
as observable objects (able to report both columns produced and columns
used), optimized 'SQL' generation as an explicit user visible table
modeling step, plus explicit query reasoning and checking.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
