%global __brp_check_rpaths %{nil}
%global packname  MAPA
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Multiple Aggregation Prediction Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 5.3
BuildRequires:    R-CRAN-smooth >= 1.4.7
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-forecast >= 5.3
Requires:         R-CRAN-smooth >= 1.4.7
Requires:         R-parallel 
Requires:         R-CRAN-RColorBrewer 

%description
Functions and wrappers for using the Multiple Aggregation Prediction
Algorithm (MAPA) for time series forecasting. MAPA models and forecasts
time series at multiple temporal aggregation levels, thus strengthening
and attenuating the various time series components for better holistic
estimation of its structure. For details see Kourentzes et al. (2014)
<doi:10.1016/j.ijforecast.2013.09.006>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
