%global packname  pbatR
%global packver   2.2-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.13
Release:          1%{?dist}
Summary:          Pedigree/Family-Based Genetic Association Tests Analysis andPower

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-survival 
Requires:         R-CRAN-rootSolve 

%description
This R package provides power calculations via internal simulation
methods. The package also provides a frontend to the now abandoned PBAT
program (developed by Christoph Lange), and reads in the corresponding
output and displays results and figures when appropriate. The license of
this R package itself is GPL. However, to have the program interact with
the PBAT program for some functionality of the R package, users must
additionally obtain the PBAT program from Christoph Lange, and accept his
license. Both the data analysis and power calculations have command line
and graphical interfaces using tcltk.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
