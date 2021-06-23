%global __brp_check_rpaths %{nil}
%global packname  HDclust
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Clustering High Dimensional Data with Hidden Markov Model onVariable Blocks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-Rtsne >= 0.11.0
BuildRequires:    R-CRAN-RcppProgress >= 0.1
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-Rtsne >= 0.11.0
Requires:         R-CRAN-RcppProgress >= 0.1
Requires:         R-methods 

%description
Clustering of high dimensional data with Hidden Markov Model on Variable
Blocks (HMM-VB) fitted via Baum-Welch algorithm. Clustering is performed
by the Modal Baum-Welch algorithm (MBW), which finds modes of the density
function. Lin Lin and Jia Li (2017)
<http://jmlr.org/papers/v18/16-342.html>.

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
%{rlibdir}/%{packname}/libs
