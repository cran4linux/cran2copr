%global packname  progress
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          2%{?dist}
Summary:          Terminal Progress Bars

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-crayon 

%description
Configurable Progress bars, they may include percentage, elapsed time,
and/or the estimated completion time. They work in terminals, in 'Emacs'
'ESS', 'RStudio', 'Windows' 'Rgui' and the 'macOS' 'R.app'. The package
also provides a 'C++' 'API', that works with or without 'Rcpp'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
