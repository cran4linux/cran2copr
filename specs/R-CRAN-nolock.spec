%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nolock
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Append 'WITH (NOLOCK)' to 'SQL' Queries, Get Packages in Active Script

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-NCmisc 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-rstudioapi 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-NCmisc 

%description
Provides a suite of tools that can assist in enhancing the processing
efficiency of 'SQL' and 'R' scripts. - The 'libr_unused()' retrieves a
vector of package names that are called within an 'R' script but are never
actually used in the script. - The 'libr_used()' retrieves a vector of
package names actively utilized within an 'R' script; packages loaded
using 'library()' but not actually used in the script will not be
included. - The 'libr_called()' retrieves a vector of all package names
which are called within an 'R' script. - 'nolock()' appends 'WITH
(nolock)' to all tables in 'SQL' queries. This facilitates reading from
databases in scenarios where non-blocking reads are preferable, such as in
high-transaction environments.

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
