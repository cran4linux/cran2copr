%global packname  irace
%global packver   3.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.1
Release:          1%{?dist}
Summary:          Iterated Racing for Automatic Algorithm Configuration

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-R6 

%description
Iterated race is an extension of the Iterated F-race method for the
automatic configuration of optimization algorithms, that is, (offline)
tuning their parameters by finding the most appropriate settings given a
set of instances of an optimization problem. M. López-Ibáñez, J.
Dubois-Lacoste, L. Pérez Cáceres, T. Stützle, and M. Birattari (2016)
<doi:10.1016/j.orp.2016.09.002>.

%prep
%setup -q -c -n %{packname}
find %{packname} -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \;
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
%{rlibdir}/%{packname}/bin
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/exdata
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
