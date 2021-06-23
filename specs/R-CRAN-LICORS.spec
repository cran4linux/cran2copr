%global __brp_check_rpaths %{nil}
%global packname  LICORS
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Light Cone Reconstruction of States - Predictive StateEstimation From Spatio-Temporal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.1
Requires:         R-core >= 2.12.1
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-locfit 
Requires:         R-Matrix 

%description
Estimates predictive states from spatio-temporal data and consequently can
provide provably optimal forecasts. Currently this implementation supports
an N-dimensional spatial grid observed over equally spaced time intervals.
E.g. a video is a 2D spatial systems observed over time. This package
implements mixed LICORS, has plotting tools (for (1+1)D and (2+1)D
systems), and methods for optimal forecasting.  Due to memory limitations
it is recommend to only analyze (1+1)D systems.

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
%{rlibdir}/%{packname}/INDEX
