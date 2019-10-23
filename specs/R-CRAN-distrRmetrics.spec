%global packname  distrRmetrics
%global packver   2.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.0
Release:          1%{?dist}
Summary:          Distribution Classes for Distributions from Rmetrics

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fBasics >= 270
BuildRequires:    R-CRAN-fGarch >= 270.73
BuildRequires:    R-CRAN-distr >= 2.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-startupmsg 
Requires:         R-CRAN-fBasics >= 270
Requires:         R-CRAN-fGarch >= 270.73
Requires:         R-CRAN-distr >= 2.4
Requires:         R-methods 
Requires:         R-CRAN-startupmsg 

%description
S4-distribution classes based on package distr for distributions from
packages 'fBasics' and 'fGarch'.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/TOBEDONE
%{rlibdir}/%{packname}/INDEX
