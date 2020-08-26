%global packname  packager
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create, Build and Maintain Packages

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-codetools 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cyclocomp 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-fakemake 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-rcmdcheck 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-whoami 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-checkmate 
Requires:         R-codetools 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cyclocomp 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-fakemake 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-rcmdcheck 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rprojroot 
Requires:         R-tools 
Requires:         R-CRAN-usethis 
Requires:         R-utils 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-whoami 
Requires:         R-CRAN-withr 

%description
Helper functions for package creation, building and maintenance. Designed
to work with a build system such as 'GNU make' or package 'fakemake' to
help you to conditionally work through the stages of package development
(such as spell checking, linting, testing, before building and checking a
package).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
