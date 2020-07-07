%global packname  rmake
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Makefile Generator for R Analytical Projects

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-tools 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-visNetwork 

%description
Creates and maintains a build process for complex analytic tasks in R.
Package allows to easily generate Makefile for the (GNU) 'make' tool,
which drives the build process by (in parallel) executing build commands
in order to update results accordingly to given dependencies on changed
data or updated source files.

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
