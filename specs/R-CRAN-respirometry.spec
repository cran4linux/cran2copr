%global packname  respirometry
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Tools for Conducting and Analyzing Respirometry Experiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-seacarb >= 3.1
BuildRequires:    R-CRAN-measurements >= 1.1.0
BuildRequires:    R-CRAN-segmented >= 1.0.0
BuildRequires:    R-CRAN-PKNCA 
BuildRequires:    R-CRAN-birk 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-marelac 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-seacarb >= 3.1
Requires:         R-CRAN-measurements >= 1.1.0
Requires:         R-CRAN-segmented >= 1.0.0
Requires:         R-CRAN-PKNCA 
Requires:         R-CRAN-birk 
Requires:         R-graphics 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-marelac 
Requires:         R-methods 
Requires:         R-CRAN-minpack.lm 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools to enable the researcher to more precisely conduct
respirometry experiments. Strong emphasis is on aquatic respirometry.
Tools focus on helping the researcher setup and conduct experiments.
Functions for analysis of resulting respirometry data are also provided.
This package provides tools for intermittent, flow-through, and closed
respirometry techniques.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
