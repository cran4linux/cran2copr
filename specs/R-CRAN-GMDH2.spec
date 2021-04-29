%global packname  GMDH2
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Binary Classification via GMDH-Type Neural Network Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-e1071 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-xtable 

%description
Performs binary classification via Group Method of Data Handling (GMDH) -
type neural network algorithms. There exist two main algorithms available
in GMDH() and dceGMDH() functions. GMDH() performs classification via GMDH
algorithm for a binary response and returns important variables. dceGMDH()
performs classification via diverse classifiers ensemble based on GMDH
(dce-GMDH) algorithm. Also, the package produces a well-formatted table of
descriptives for a binary response. Moreover, it produces confusion
matrix, its related statistics and scatter plot (2D and 3D) with
classification labels of binary classes to assess the prediction
performance. All 'GMDH2' functions are designed for a binary response (Dag
et al., 2019,
<https://download.atlantis-press.com/article/125911202.pdf>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
