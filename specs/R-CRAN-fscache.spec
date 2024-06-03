%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fscache
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          File System Cache

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-tools 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-lgr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-stringi 
Requires:         R-tools 

%description
Manages a file system cache. Regular files can be moved or copied to the
cache folder. Sub-folders can be created in order to organize the files.
Files can be located inside the cache using a glob function. Text contents
can be easily stored in and retrieved from the cache using dedicated
functions. It can be used for an application or a package, as a global
cache, or as a per-user cache, in which case the standard OS user cache
folder will be used (e.g.: on Linux
$HOME/.cache/R/my_app_or_pkg_cache_folder).

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
