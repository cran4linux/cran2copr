%global packname  stray
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Anomaly Detection in High Dimensional and Temporal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ks 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-pcaPP 
Requires:         R-stats 
Requires:         R-CRAN-ks 

%description
This is a modification of 'HDoutliers' package. The 'HDoutliers' algorithm
is a powerful unsupervised algorithm for detecting anomalies in
high-dimensional data, with a strong theoretical foundation. However, it
suffers from some limitations that significantly hinder its performance
level, under certain circumstances. This package implements the algorithm
proposed in Talagala, Hyndman and Smith-Miles (2019) <arXiv:1908.04000>
for detecting anomalies in high-dimensional data that addresses these
limitations of 'HDoutliers' algorithm. We define an anomaly as an
observation that deviates markedly from the majority with a large distance
gap. An approach based on extreme value theory is used for the anomalous
threshold calculation.

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
