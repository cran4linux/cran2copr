%global __brp_check_rpaths %{nil}
%global packname  synRNASeqNet
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Synthetic RNA-Seq Network Generation and Mutual InformationEstimates

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parmigene 
BuildRequires:    R-CRAN-GenKern 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-KernSmooth 
Requires:         R-parallel 
Requires:         R-CRAN-parmigene 
Requires:         R-CRAN-GenKern 
Requires:         R-CRAN-igraph 
Requires:         R-KernSmooth 

%description
It implements various estimators of mutual information, such as the
maximum likelihood and the Millow-Madow estimator, various Bayesian
estimators, the shrinkage estimator, and the Chao-Shen estimator. It also
offers wrappers to the kNN and kernel density estimators. Furthermore, it
provides various index of performance evaluation such as precision,
recall, FPR, F-Score, ROC-PR Curves and so on. Lastly, it provides a brand
new way of generating synthetic RNA-Seq Network with known dependence
structure.

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
