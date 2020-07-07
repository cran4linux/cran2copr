%global packname  GLDEX
%global packver   2.0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0.7
Release:          3%{?dist}
Summary:          Fitting Single and Mixture of Generalised Lambda Distributions(RS and FMKL) using Various Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-cluster 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-cluster 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
The fitting algorithms considered in this package have two major
objectives. One is to provide a smoothing device to fit distributions to
data using the weight and unweighted discretised approach based on the bin
width of the histogram. The other is to provide a definitive fit to the
data set using the maximum likelihood and quantile matching estimation.
Other methods such as moment matching, starship method, L moment matching
are also provided. Diagnostics on goodness of fit can be done via qqplots,
KS-resample tests and comparing mean, variance, skewness and kurtosis of
the data with the fitted distribution.

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
%{rlibdir}/%{packname}/libs
