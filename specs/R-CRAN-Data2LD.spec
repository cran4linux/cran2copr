%global packname  Data2LD
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Functional Data Analysis with Linear Differential Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-splines 
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-fda 
Requires:         R-splines 
Requires:         R-Matrix 
Requires:         R-graphics 
Requires:         R-CRAN-deSolve 

%description
Provides methods for using differential equations as modelling objects as
described in J. Ramsay G. and Hooker (2017,ISBN 978-1-4939-7188-6) Dynamic
Data Analysis, New York: Springer. Data sets and script files for
analyzing many of the examples in this book are included. This version
corrects bugs and adds a new demo, CruiseControl. 'Matlab' versions of the
code and sample analyses are available by ftp from
<http://www.psych.mcgill.ca/misc/fda/downloads/Data2LD/>.  There you find
a set of .zip files containing the functions and sample analyses, as well
as two .txt files giving instructions for installation and some additional
information.

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
