%global packname  MCPMod
%global packver   1.0-10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10.1
Release:          1%{?dist}
Summary:          Design and Analysis of Dose-Finding Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.1
Requires:         R-core >= 2.4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-lattice 
Requires:         R-CRAN-mvtnorm 
Requires:         R-lattice 

%description
Implements a methodology for the design and analysis of dose-response
studies that combines aspects of multiple comparison procedures and
modeling approaches (Bretz, Pinheiro and Branson, 2005, Biometrics 61,
738-748, <doi: 10.1111/j.1541-0420.2005.00344.x>). The package provides
tools for the analysis of dose finding trials as well as a variety of
tools necessary to plan a trial to be conducted with the MCP-Mod
methodology. Please note: The 'MCPMod' package will not be further
developed, all future development of the MCP-Mod methodology will be done
in the 'DoseFinding' R-package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX
