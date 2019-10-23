%global packname  sysid
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          System Identification in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-tframe 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-signal 
Requires:         R-CRAN-tframe 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-zoo 

%description
Provides functions for constructing mathematical models of dynamical
systems from measured input-output data.

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
