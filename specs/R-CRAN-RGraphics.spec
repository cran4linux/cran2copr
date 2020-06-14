%global packname  RGraphics
%global packver   3.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          2%{?dist}
Summary:          Data and Functions from the Book R Graphics, Third Edition

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-datasets 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-grImport 
BuildRequires:    R-CRAN-grImport2 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-gridGraphics 
BuildRequires:    R-CRAN-gridSVG 
Requires:         R-datasets 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-lattice 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-grImport 
Requires:         R-CRAN-grImport2 
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-gridGraphics 
Requires:         R-CRAN-gridSVG 

%description
Data and Functions from the book R Graphics, Third Edition. There is a
function to produce each figure in the book, plus several functions,
classes, and methods defined in Chapter 8.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/extra
%{rlibdir}/%{packname}/INDEX
