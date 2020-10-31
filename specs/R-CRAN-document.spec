%global packname  document
%global packver   3.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Run 'roxygen2' on (Chunks of) Single Code Files

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-rcmdcheck 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-rcmdcheck 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-withr 

%description
Have you ever been tempted to create 'roxygen2'-style documentation
comments for one of your functions that was not part of one of your
packages (yet)? This is exactly what this package is about: running
'roxygen2' on (chunks of) a single code file.

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
