%global packname  DTWUMI
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Imputation of Multivariate Time Series Based on Dynamic TimeWarping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-lsa 
BuildRequires:    R-CRAN-DTWBI 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-rlist 
Requires:         R-stats 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-lsa 
Requires:         R-CRAN-DTWBI 

%description
Functions to impute large gaps within multivariate time series based on
Dynamic Time Warping methods. Gaps of size 1 or inferior to a defined
threshold are filled using simple average and weighted moving average
respectively. Larger gaps are filled using the methodology provided by
Phan et al. (2017) <DOI:10.1109/MLSP.2017.8168165>: a query is built
immediately before/after a gap and a moving window is used to find the
most similar sequence to this query using Dynamic Time Warping. To lower
the calculation time, similar sequences are pre-selected using global
features. Contrary to the univariate method (package 'DTWBI'), these
global features are not estimated over the sequence containing the gap(s),
but a feature matrix is built to summarize general features of the whole
multivariate signal. Once the most similar sequence to the query has been
identified, the adjacent sequence to this window is used to fill the gap
considered. This function can deal with multiple gaps over all the
sequences componing the input multivariate signal. However, for better
consistency, large gaps at the same location over all sequences should be
avoided.

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
