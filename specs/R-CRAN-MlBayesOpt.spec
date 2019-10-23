%global packname  MlBayesOpt
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Hyper Parameter Tuning for Machine Learning, Using BayesianOptimization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-e1071 >= 1.6.8
BuildRequires:    R-CRAN-rBayesianOptimization >= 1.1.0
BuildRequires:    R-CRAN-ranger >= 0.8.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-xgboost >= 0.6.4
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-e1071 >= 1.6.8
Requires:         R-CRAN-rBayesianOptimization >= 1.1.0
Requires:         R-CRAN-ranger >= 0.8.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-xgboost >= 0.6.4
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-Matrix 
Requires:         R-CRAN-foreach 

%description
Hyper parameter tuning using Bayesian optimization (Shahriari et al.
<doi:10.1109/JPROC.2015.2494218>) for support vector machine, random
forest, and extreme gradient boosting (Chen & Guestrin (2016)
<doi:10.1145/2939672.2939785>). Unlike already existing packages (e.g.
'mlr', 'rBayesianOptimization', or 'xgboost'), there is no need to change
in accordance with the package or method of machine learning. You just
prepare a data frame with feature vectors and the label column that has
any class ('character', 'factor', 'integer'). Moreover, to write a
optimization function, you have only to specify the data and the column
name of the label to classify.

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
