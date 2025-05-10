%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sphereML
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Students' Performance Dataset in Physics Education Research (SPHERE) using Machine Learning (ML)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.50
Requires:         R-core >= 3.50
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-spheredata 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-semPlot 
BuildRequires:    R-CRAN-CTT 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-FSelectorRcpp 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-spheredata 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-semPlot 
Requires:         R-CRAN-CTT 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-FSelectorRcpp 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-readxl 

%description
A simple package facilitating ML based analysis for physics education
research (PER) purposes. The implemented machine learning technique is
random forest optimized by item response theory (IRT) for feature
selection and genetic algorithm (GA) for hyperparameter tuning. The data
analyzed here has been made available in the CRAN repository through the
'spheredata' package. The SPHERE stands for Students' Performance in
Physics Education Research (PER). The students are the eleventh graders
learning physics at the high school curriculum. We follow the stream of
multidimensional students' assessment as probed by some research based
assessments in PER. The goal is to predict the students' performance at
the end of the learning process. Three learning domains are measured
including conceptual understanding, scientific ability, and scientific
attitude. Furthermore, demographic backgrounds and potential variables
predicting students' performance on physics are also demonstrated.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
