%global __brp_check_rpaths %{nil}
%global packname  ebmc
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ensemble-Based Methods for Class Imbalance Problem

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-smotefamily 
Requires:         R-methods 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-smotefamily 

%description
Four ensemble-based methods (SMOTEBoost, RUSBoost, UnderBagging, and
SMOTEBagging) for class imbalance problem are implemented for binary
classification. Such methods adopt ensemble methods and data re-sampling
techniques to improve model performance in presence of class imbalance
problem. One special feature offers the possibility to choose multiple
supervised learning algorithms to build weak learners within ensemble
models. References: Nitesh V. Chawla, Aleksandar Lazarevic, Lawrence O.
Hall, and Kevin W. Bowyer (2003) <doi:10.1007/978-3-540-39804-2_12>, Chris
Seiffert, Taghi M. Khoshgoftaar, Jason Van Hulse, and Amri Napolitano
(2010) <doi:10.1109/TSMCA.2009.2029559>, R. Barandela, J. S. Sanchez, R.
M. Valdovinos (2003) <doi:10.1007/s10044-003-0192-z>, Shuo Wang and Xin
Yao (2009) <doi:10.1109/CIDM.2009.4938667>, Yoav Freund and Robert E.
Schapire (1997) <doi:10.1006/jcss.1997.1504>.

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
