%global packname  pkgbuild
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}
Summary:          Find Tools Needed to Build R Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.2.0
BuildRequires:    R-CRAN-withr >= 2.1.2
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rprojroot 
Requires:         R-CRAN-callr >= 3.2.0
Requires:         R-CRAN-withr >= 2.1.2
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rprojroot 

%description
Provides functions used to build R packages. Locates compilers needed to
build R packages on various platforms and ensures the PATH is configured
appropriately so R can use them.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
