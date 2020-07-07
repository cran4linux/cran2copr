%global packname  RTextTools
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          3%{?dist}
Summary:          Automatic Text Classification via Supervised Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-tree 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-tau 
Requires:         R-CRAN-SparseM 
Requires:         R-methods 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-tree 
Requires:         R-nnet 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ipred 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-tau 

%description
A machine learning package for automatic text classification that makes it
simple for novice users to get started with machine learning, while
allowing experienced users to easily experiment with different settings
and algorithm combinations. The package includes eight algorithms for
ensemble classification (svm, slda, boosting, bagging, random forests,
glmnet, decision trees, neural networks), comprehensive analytics, and
thorough documentation.

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/THANKS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
