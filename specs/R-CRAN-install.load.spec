%global packname  install.load
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          3%{?dist}
Summary:          Check, Install and Load CRAN & USGS GRAN Packages

License:          CC BY-SA 4.0 | GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-utils 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-assertthat 

%description
The function `install_load` checks the local R library(ies) to see if the
required package(s) is/are installed or not. If the package(s) is/are not
installed, then the package(s) will be installed along with the required
dependency(ies). This function pulls source or binary packages from the
Rstudio-sponsored CRAN mirror and/or the USGS GRAN Repository. Lastly, the
chosen package(s) is/are loaded. The function `load_package` simply loads
the provided packages. If this package does not fit your needs, then you
may want to consider these other R packages: 'needs', 'easypackages',
'pacman', 'pak', 'anyLib', and/or 'librarian'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHT
%{rlibdir}/%{packname}/INDEX
