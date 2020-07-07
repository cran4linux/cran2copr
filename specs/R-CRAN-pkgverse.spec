%global packname  pkgverse
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Build a Meta-Package Universe

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-usethis 
Requires:         R-utils 

%description
Build your own universe of packages similar to the 'tidyverse' package
<https://tidyverse.org/> with this meta-package creator. Create a
package-verse, or meta package, by supplying a custom name for the
collection of packages and the vector of desired package names to include–
and optionally supply a destination directory, an indicator of whether to
keep the created package directory, and/or a vector of verbs implement via
the 'usethis' <http://usethis.r-lib.org/> package.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
