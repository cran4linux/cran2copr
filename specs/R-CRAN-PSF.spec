%global packname  PSF
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}
Summary:          Forecasting of Univariate Time Series Using the PatternSequence-Based Forecasting (PSF) Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-forecast 
Requires:         R-CRAN-data.table 
Requires:         R-cluster 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-forecast 

%description
Pattern Sequence Based Forecasting (PSF) takes univariate time series data
as input and assist to forecast its future values. This algorithm
forecasts the behavior of time series based on similarity of pattern
sequences. Initially, clustering is done with the labeling of samples from
database. The labels associated with samples are then used for forecasting
the future behaviour of time series data. The further technical details
and references regarding PSF are discussed in Vignette.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
