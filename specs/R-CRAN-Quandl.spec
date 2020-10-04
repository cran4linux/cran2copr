%global packname  Quandl
%global packver   2.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10.0
Release:          3%{?dist}%{?buildtag}
Summary:          API Wrapper for Quandl.com

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9.14
BuildRequires:    R-CRAN-httr >= 0.6.1
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-jsonlite >= 0.9.14
Requires:         R-CRAN-httr >= 0.6.1
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Functions for interacting directly with the Quandl API to offer data in a
number of formats usable in R, downloading a zip with all data from a
Quandl database, and the ability to search. This R package uses the Quandl
API. For more information go to <https://www.quandl.com/docs/api>. For
more help on the package itself go to <https://www.quandl.com/help/r>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
