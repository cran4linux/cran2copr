%global packname  rrecsys
%global packver   0.9.7.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7.3.1
Release:          1%{?dist}
Summary:          Environment for Evaluating Recommender Systems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-registry 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-registry 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Processes standard recommendation datasets (e.g., a user-item rating
matrix) as input and generates rating predictions and lists of recommended
items. Standard algorithm implementations which are included in this
package are the following: Global/Item/User-Average baselines, Weighted
Slope One, Item-Based KNN, User-Based KNN, FunkSVD, BPR and weighted ALS.
They can be assessed according to the standard offline evaluation
methodology (Shani, et al. (2011) <doi:10.1007/978-0-387-85820-3_8>) for
recommender systems using measures such as MAE, RMSE, Precision, Recall,
F1, AUC, NDCG, RankScore and coverage measures. The package (Coba, et
al.(2017) <doi: 10.1007/978-3-319-60042-0_36>) is intended for rapid
prototyping of recommendation algorithms and education purposes.

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
