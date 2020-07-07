%global packname  locits
%global packver   1.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.3
Release:          3%{?dist}
Summary:          Test of Stationarity and Localized Autocovariance

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-wavethresh 
Requires:         R-CRAN-igraph 

%description
Provides test of second-order stationarity for time series (for dyadic and
arbitrary-n length data). Provides localized autocovariance, with
confidence intervals, for locally stationary (nonstationary) time series.

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
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
