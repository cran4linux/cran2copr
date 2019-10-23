%global packname  diceR
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Diverse Cluster Ensemble in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-apcluster 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-blockcluster 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-CRAN-clValid 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-flux 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-kohonen 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-NMF 
BuildRequires:    R-CRAN-poLCA 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-quantable 
BuildRequires:    R-CRAN-RankAggreg 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-sigclust 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-CRAN-abind 
Requires:         R-CRAN-apcluster 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-blockcluster 
Requires:         R-CRAN-caret 
Requires:         R-class 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-clue 
Requires:         R-cluster 
Requires:         R-CRAN-clusterCrit 
Requires:         R-CRAN-clValid 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-flux 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gplots 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-kohonen 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-CRAN-NMF 
Requires:         R-CRAN-poLCA 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-quantable 
Requires:         R-CRAN-RankAggreg 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-sigclust 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Performs cluster analysis using an ensemble clustering framework, Chiu &
Talhouk (2018) <doi:10.1186/s12859-017-1996-y>.  Results from a diverse
set of algorithms are pooled together using methods such as majority
voting, K-Modes, LinkCluE, and CSPA. There are options to compare cluster
assignments across algorithms using internal and external indices,
visualizations such as heatmaps, and significance testing for the
existence of clusters.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
