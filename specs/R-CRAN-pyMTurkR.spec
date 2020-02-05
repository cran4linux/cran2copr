%global packname  pyMTurkR
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          A Client for the 'MTurk' Requester API

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-curl 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-XML 

%description
Provides access to the latest 'Amazon Mechanical Turk' ('MTurk')
<https://www.mturk.com> Requester API (version '2017–01–17'), replacing
the now deprecated 'MTurkR' package.

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
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
