%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bread
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Big Files Without Loading Them in Memory

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-data.table 

%description
A simple set of wrapper functions for data.table::fread() that allows
subsetting or filtering rows and selecting columns of table-formatted
files too large for the available RAM. 'b stands for 'big files'. bread
makes heavy use of Unix commands like 'grep', 'sed', 'wc', 'awk' and
'cut'. They are available by default in all Unix environments. For
Windows, you need to install those commands externally in order to
simulate a Unix environment and make sure that the executables are in the
Windows PATH variable. To my knowledge, the simplest ways are to install
'RTools', 'Git' or 'Cygwin'. If they have been correctly installed (with
the expected registry entries), they should be detected on loading the
package and the correct directories will be added automatically to the
PATH.

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
