%global packname  coca
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Cluster-of-Clusters Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-fpc 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-cluster 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-caret 
Requires:         R-nnet 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-fpc 

%description
Contains the R functions needed to perform Cluster-Of-Clusters Analysis
(COCA) and Consensus Clustering (CC). For further details please see
Cabassi and Kirk (2019) <arXiv:1904.07701>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/script
%{rlibdir}/%{packname}/INDEX
