%global packname  TSMining
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Mining Univariate and Multivariate Motifs in Time-Series Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 

%description
Implementations of a number of functions used to mine numeric time-series
data. It covers the implementation of SAX transformation, univariate motif
discovery (based on the random projection method), multivariate motif
discovery (based on graph clustering), and several functions used for the
ease of visualizing the motifs discovered. The details of SAX
transformation can be found in J. Lin. E. Keogh, L. Wei, S. Lonardi,
Experiencing SAX: A novel symbolic representation of time series, Data
Mining and Knowledge Discovery 15 (2) (2007) 107-144. Details on
univariate motif discovery method implemented can be found in B. Chiu, E.
Keogh, S. Lonardi, Probabilistic discovery of time series motifs, ACM
SIGKDD, Washington, DC, USA, 2003, pp. 493-498. Details on the
multivariate motif discovery method implemented can be found in A.
Vahdatpour, N. Amini, M. Sarrafzadeh, Towards unsupervised activity
discovery using multi-dimensional motif detection in time series, IJCAI
2009 21st International Joint Conference on Artificial Intelligence.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
