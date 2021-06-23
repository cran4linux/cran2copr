%global __brp_check_rpaths %{nil}
%global packname  rminer
%global packver   1.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Data Mining Classification and Regression Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-lattice 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-adabag 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-methods 
Requires:         R-CRAN-plotrix 
Requires:         R-lattice 
Requires:         R-nnet 
Requires:         R-CRAN-kknn 
Requires:         R-CRAN-pls 
Requires:         R-MASS 
Requires:         R-CRAN-mda 
Requires:         R-rpart 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-adabag 
Requires:         R-CRAN-party 
Requires:         R-CRAN-Cubist 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-xgboost 

%description
Facilitates the use of data mining algorithms in classification and
regression (including time series forecasting) tasks by presenting a short
and coherent set of functions. Versions: 1.4.6 / 1.4.5 / 1.4.4 new
automated machine learning (AutoML) and ensembles, via improved fit(),
mining() and mparheuristic() functions, and new categorical preprocessing,
via improved delevels() function; 1.4.3 new metrics (e.g., macro
precision, explained variance), new "lssvm" model and improved
mparheuristic() function; 1.4.2 new "NMAE" metric, "xgboost" and
"cv.glmnet" models (16 classification and 18 regression models); 1.4.1 new
tutorial and more robust version; 1.4 - new classification and regression
models, with a total of 14 classification and 15 regression methods,
including: Decision Trees, Neural Networks, Support Vector Machines,
Random Forests, Bagging and Boosting; 1.3 and 1.3.1 - new classification
and regression metrics; 1.2 - new input importance methods via improved
Importance() function; 1.0 - first version.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
