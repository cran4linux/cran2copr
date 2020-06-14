%global packname  qrmtools
%global packver   0.0-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.13
Release:          2%{?dist}
Summary:          Tools for Quantitative Risk Management

License:          GPL (>= 3) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-graphics 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-Quandl 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ADGofTest 
Requires:         R-graphics 
Requires:         R-lattice 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-Quandl 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-rugarch 
Requires:         R-utils 
Requires:         R-CRAN-ADGofTest 

%description
Functions and data sets for reproducing selected results from the book
"Quantitative Risk Management: Concepts, Techniques and Tools".
Furthermore, new developments and auxiliary functions for Quantitative
Risk Management practice.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
