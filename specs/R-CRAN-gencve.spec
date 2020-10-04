%global packname  gencve
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          General Cross Validation Engine

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-plus 
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-rpart 
BuildRequires:    R-MASS 
BuildRequires:    R-class 
BuildRequires:    R-nnet 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-plus 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-e1071 
Requires:         R-rpart 
Requires:         R-MASS 
Requires:         R-class 
Requires:         R-nnet 

%description
Engines for cross-validation of many types of regression and class
prediction models are provided. These engines include built-in support for
'glmnet', 'lars', 'plus', 'MASS', 'rpart', 'C50' and 'randomforest'. It is
easy for the user to add other regression or classification algorithms.
The 'parallel' package is used to improve speed. Several data generation
algorithms for problems in regression and classification are provided.

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
