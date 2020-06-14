%global packname  Rbeast
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Bayesian Change-Point Detection and Time Series Decomposition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-utils 

%description
Interpretation of time series data is affected by model choices. Different
models can give different or even contradicting estimates of patterns,
trends, and mechanisms for the same data--a limitation alleviated by the
Bayesian estimator of abrupt change,seasonality, and trend (BEAST) of this
package. BEAST seeks to improve time series decomposition by forgoing the
"single-best-model" concept and embracing all competing models into the
inference via a Bayesian model averaging scheme. It is a flexible tool to
uncover abrupt changes (i.e., change-points), cyclic variations (e.g.,
seasonality), and nonlinear trends in time-series observations. BEAST not
just tells when changes occur but also quantifies how likely the detected
changes are true. It detects not just piecewise linear trends but also
arbitrary nonlinear trends. BEAST is applicable to real-valued time series
data of all kinds, be it for remote sensing, economics, climate sciences,
ecology, and hydrology. Example applications include its use to identify
regime shifts in ecological data, map forest disturbance and land
degradation from satellite imagery, detect market trends in economic data,
pinpoint anomaly and extreme events in climate data, and unravel system
dynamics in biological data. Details on BEAST are reported in Zhao et al.
(2019) <doi:10.1016/j.rse.2019.04.034>.

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
%{rlibdir}/%{packname}/libs
