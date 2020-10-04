%global packname  GPrank
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Gaussian Process Ranking of Multiple Time Series

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gptk 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-tigreBrowserWriter 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-gptk 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-tigreBrowserWriter 
Requires:         R-CRAN-RColorBrewer 

%description
Implements a Gaussian process (GP)-based ranking method which can be used
to rank multiple time series according to their temporal activity levels.
An example is the case when expression levels of all genes are measured
over a time course and the main concern is to identify the most active
genes, i.e. genes which show significant non-random variation in their
expression levels. This is achieved by computing Bayes factors for each
time series by comparing the marginal likelihoods under time-dependent and
time-independent GP models. Additional variance information from
pre-processing of the observations is incorporated into the GP models,
which makes the ranking more robust against model overfitting. The package
supports exporting the results to 'tigreBrowser' for visualisation,
filtering or ranking.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
