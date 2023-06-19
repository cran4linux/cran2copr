%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  packager
%global packver   1.15.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create, Build and Maintain Packages

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fritools >= 3.4.0
BuildRequires:    R-CRAN-fakemake >= 1.10.1
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cyclocomp 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-rcmdcheck 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rhub 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-tinytest 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-whoami 
Requires:         R-CRAN-fritools >= 3.4.0
Requires:         R-CRAN-fakemake >= 1.10.1
Requires:         R-CRAN-callr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-codetools 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cyclocomp 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-rcmdcheck 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rhub 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-tinytest 
Requires:         R-tools 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-whoami 

%description
Helper functions for package creation, building and maintenance. Designed
to work with a build system such as 'GNU make' or package 'fakemake' to
help you to conditionally work through the stages of package development
(such as spell checking, linting, testing, before building and checking a
package).

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
