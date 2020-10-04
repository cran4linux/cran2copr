%global packname  acs
%global packver   2.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Download, Manipulate, and Present American Community Survey andDecennial Data from the US Census

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-XML 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-utils 
Requires:         R-CRAN-httr 

%description
Provides a general toolkit for downloading, managing, analyzing, and
presenting data from the U.S. Census
(<https://www.census.gov/data/developers/data-sets.html>), including SF1
(Decennial short-form), SF3 (Decennial long-form), and the American
Community Survey (ACS).  Confidence intervals provided with ACS data are
converted to standard errors to be bundled with estimates in complex acs
objects.  Package provides new methods to conduct standard operations on
acs objects and present/plot data in statistically appropriate ways.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
