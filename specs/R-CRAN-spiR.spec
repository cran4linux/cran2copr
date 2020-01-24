%global packname  spiR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Wrapper for the Social Progress Index Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gsheet 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-gsheet 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 

%description
In 2015, The 17 United Nations' Sustainable Development Goals were
adopted. 'spiR' is a wrapper of several open datasets published by the
Social Progress Imperative (<https://www.socialprogress.org/>), including
the Social Progress Index (a synthetic measure of human development across
the world). 'spiR''s goal is to provide data to help policymakers and
researchers prioritize actions that accelerate social progress across the
world in the context of the Sustainable Development Goals. Please cite:
Warin, Th. (2019) "spiR: An R Package for the Social Progress Index",
<doi:10.6084/m9.figshare.11421573>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
