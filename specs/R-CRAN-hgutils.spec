%global packname  hgutils
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          2%{?dist}
Summary:          Collection of Utility Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-grDevices 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
A handy collection of utility functions designed to aid in package
development, plotting and scientific research. Package development
functionalities includes among others tools such as cross-referencing
package imports with the description file, analysis of redundant package
imports, editing of the description file and the creation of package
badges for GitHub. Some of the other functionalities include automatic
package installation and loading, plotting points without overlap,
creating nice breaks for plots, overview tables and many more handy
utility functions.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
