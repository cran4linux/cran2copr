%global packname  clustRcompaR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Easy Interface for Clustering a Set of Documents and ExploringGroup- Based Patterns

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ppls 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ppls 

%description
Provides an interface to perform cluster analysis on a corpus of text.
Interfaces to Quanteda to assemble text corpuses easily. Deviationalizes
text vectors prior to clustering using technique described by Sherin
(Sherin, B. [2013]. A computational study of commonsense science: An
exploration in the automated analysis of clinical interview data. Journal
of the Learning Sciences, 22(4), 600-638. Chicago.
<doi:10.1080/10508406.2013.836654>). Uses cosine similarity as distance
metric for two stage clustering process, involving Ward's algorithm
hierarchical agglomerative clustering, and k-means clustering. Selects
optimal number of clusters to maximize "variance explained" by clusters,
adjusted by the number of clusters. Provides plotted output of clustering
results as well as printed output. Assesses "model fit" of clustering
solution to a set of preexisting groups in dataset.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
