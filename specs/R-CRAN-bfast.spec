%global packname  bfast
%global packver   1.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.7
Release:          3%{?dist}%{?buildtag}
Summary:          Breaks For Additive Season and Trend (BFAST)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 

%description
BFAST integrates the decomposition of time series into trend, seasonal,
and remainder components with methods for detecting and characterizing
abrupt changes within the trend and seasonal components. BFAST can be used
to analyze different types of satellite image time series and can be
applied to other disciplines dealing with seasonal or non-seasonal time
series, such as hydrology, climatology, and econometrics. The algorithm
can be extended to label detected changes with information on the
parameters of the fitted piecewise linear models. BFAST monitoring
functionality is added based on a paper that has been submitted to Remote
Sensing of Environment. BFAST monitor provides functionality to detect
disturbance in near real-time based on BFAST-type models. BFAST approach
is flexible approach that handles missing data without interpolation.
Furthermore now different models can be used to fit the time series data
and detect structural changes (breaks).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
