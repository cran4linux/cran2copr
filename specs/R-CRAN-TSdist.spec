%global packname  TSdist
%global packver   3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6
Release:          1%{?dist}
Summary:          Distance Measures for Time Series Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-TSclust 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-locpol 
BuildRequires:    R-CRAN-pdc 
BuildRequires:    R-CRAN-longitudinalData 
BuildRequires:    R-cluster 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-TSclust 
Requires:         R-KernSmooth 
Requires:         R-CRAN-locpol 
Requires:         R-CRAN-pdc 
Requires:         R-CRAN-longitudinalData 
Requires:         R-cluster 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 

%description
A set of commonly used distance measures and some additional functions
which, although initially not designed for this purpose, can be used to
measure the dissimilarity between time series. These measures can be used
to perform clustering, classification or other data mining tasks which
require the definition of a distance measure between time series.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
