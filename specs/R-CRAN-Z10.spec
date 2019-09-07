%global packname  Z10
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Simple Ecological Statistics from the NEON Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 

%description
Provides simple statistics from instruments and observations at sites in
the NEON network, and acts as a simple interface for v0 of the National
Ecological Observatory Network (NEON) API. Statistics are generated for
meteorologic and soil-based observations, and are presented for daily,
annual, and one-time observations at all available NEON sites. Users can
also retrieve any dataset publicly hosted by NEON. Metadata for NEON sites
and data products can be returned, as well as information on data product
availability by site and date. For more information on NEON, please visit
<https://www.neonscience.org>. For detailed data product information,
please see the NEON data product catalog at
<https://data.neonscience.org/data-product-catalog>.

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
%{rlibdir}/%{packname}/INDEX
