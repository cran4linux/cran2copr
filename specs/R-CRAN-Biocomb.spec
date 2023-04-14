%global __brp_check_rpaths %{nil}
%global packname  Biocomb
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Feature Selection and Classification with the EmbeddedValidation Procedures for Biomedical Data Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-pamr 
BuildRequires:    R-class 
BuildRequires:    R-nnet 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-FSelector 
BuildRequires:    R-CRAN-RWeka 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-rgl 
Requires:         R-MASS 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-pamr 
Requires:         R-class 
Requires:         R-nnet 
Requires:         R-rpart 
Requires:         R-CRAN-FSelector 
Requires:         R-CRAN-RWeka 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains functions for the data analysis with the emphasis on biological
data, including several algorithms for feature ranking, feature selection,
classification algorithms with the embedded validation procedures. The
functions can deal with numerical as well as with nominal features.
Includes also the functions for calculation of feature AUC (Area Under the
ROC Curve) and HUM (hypervolume under manifold) values and construction
2D- and 3D- ROC curves. Provides the calculation of Area Above the RCC
(AAC) values and construction of Relative Cost Curves (RCC) to estimate
the classifier performance under unequal misclassification costs problem.
There exists the special function to deal with missing values, including
different imputing schemes.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
