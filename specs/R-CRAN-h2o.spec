%global packname  h2o
%global packver   3.28.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.28.0.2
Release:          1%{?dist}
Summary:          R Interface for the 'H2O' Scalable Machine Learning Platform

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz
Source1:          https://s3.amazonaws.com/h2o-release/h2o/rel-yu/2/Rjar/h2o.jar

Requires:         java
BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-jsonlite 

%description
R interface for 'H2O', the scalable open source machine learning platform
that offers parallelized implementations of many supervised and
unsupervised machine learning algorithms such as Generalized Linear
Models, Gradient Boosting Machines (including XGBoost), Random Forests,
Deep Neural Networks (Deep Learning), Stacked Ensembles, Naive Bayes, Cox
Proportional Hazards, K-Means, PCA, Word2Vec, as well as a fully automatic
machine learning algorithm (AutoML).

%prep
%setup -q -c -n %{packname}
cp %{SOURCE1} %{packname}/inst/java

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/branch.txt
%doc %{rlibdir}/%{packname}/buildnum.txt
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/source_code_repository_info.txt
%{rlibdir}/%{packname}/INDEX
