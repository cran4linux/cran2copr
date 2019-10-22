%global packname  TSclust
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Time Series Clustering Utilities

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-wmtsa 
BuildRequires:    R-CRAN-pdc 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-locpol 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-longitudinalData 
Requires:         R-CRAN-wmtsa 
Requires:         R-CRAN-pdc 
Requires:         R-cluster 
Requires:         R-CRAN-locpol 
Requires:         R-KernSmooth 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-longitudinalData 

%description
A set of measures of dissimilarity between time series to perform time
series clustering. Metrics based on raw data, on generating models and on
the forecast behavior are implemented. Some additional utilities related
to time series clustering are also provided, such as clustering algorithms
and cluster evaluation metrics.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
