%global packname  oddstream
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Outlier Detection in Data Streams

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-mvtsplot 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-pcaPP 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ks 
Requires:         R-MASS 
Requires:         R-CRAN-RcppRoll 
Requires:         R-mgcv 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-mvtsplot 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-magrittr 

%description
We proposes a framework that provides real time support for early
detection of anomalous series within a large collection of streaming time
series data. By definition, anomalies are rare in comparison to a system's
typical behaviour. We define an anomaly as an observation that is very
unlikely given the forecast distribution. The algorithm first forecasts a
boundary for the system's typical behaviour using a representative sample
of the typical behaviour of the system. An approach based on extreme value
theory is used for this boundary prediction process. Then a sliding window
is used to test for anomalous series within the newly arrived collection
of series. Feature based representation of time series is used as the
input to the model. To cope with concept drift, the forecast boundary for
the system's typical behaviour is updated periodically.  More details
regarding the algorithm can be found in Talagala, P. D., Hyndman, R. J.,
Smith-Miles, K., et al. (2019) <doi:10.1080/10618600.2019.1617160>.

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
