%global packname  lubridate
%global packver   1.7.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.8
Release:          1%{?dist}
Summary:          Make Dealing with Dates a Little Easier

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-generics 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-methods 
Requires:         R-CRAN-generics 

%description
Functions to work with date-times and time-spans: fast and user friendly
parsing of date-time data, extraction and updating of components of a
date-time (years, months, days, hours, minutes, and seconds), algebraic
manipulation on date-time and time-span objects. The 'lubridate' package
has a consistent and memorable syntax that makes working with dates easy
and fun.  Parts of the 'CCTZ' source code, released under the Apache 2.0
License, are included in this package. See
<https://github.com/google/cctz> for more details.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cctz.sh
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/pkgdown
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
