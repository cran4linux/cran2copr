%global packname  traineR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Predictive Models Homologator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-nnet >= 7.3.12
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-rpart >= 4.1.13
BuildRequires:    R-CRAN-ada >= 2.0.5
BuildRequires:    R-CRAN-e1071 >= 1.7.0.1
BuildRequires:    R-CRAN-dummies >= 1.5.6
BuildRequires:    R-CRAN-neuralnet >= 1.44.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-kknn >= 1.3.1
BuildRequires:    R-CRAN-xgboost >= 0.81.0.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
Requires:         R-nnet >= 7.3.12
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-rpart >= 4.1.13
Requires:         R-CRAN-ada >= 2.0.5
Requires:         R-CRAN-e1071 >= 1.7.0.1
Requires:         R-CRAN-dummies >= 1.5.6
Requires:         R-CRAN-neuralnet >= 1.44.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-kknn >= 1.3.1
Requires:         R-CRAN-xgboost >= 0.81.0.1
Requires:         R-CRAN-dplyr >= 0.8.0.1

%description
Methods to unify the different ways of creating predictive models and
their different predictive formats. It includes methods such as K-Nearest
Neighbors, Decision Trees, ADA Boosting, Extreme Gradient Boosting, Random
Forest, Neural Networks, Deep Learning, Support Vector Machines and
Bayesian Methods.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
