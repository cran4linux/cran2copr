%global __brp_check_rpaths %{nil}
%global packname  chemmodlab
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Cheminformatics Modeling Laboratory for Fitting and Assessing Machine Learning Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.45
BuildRequires:    R-CRAN-class >= 7.3.14
BuildRequires:    R-CRAN-nnet >= 7.3.12
BuildRequires:    R-CRAN-caret >= 6.0.71
BuildRequires:    R-CRAN-randomForest >= 4.6.12
BuildRequires:    R-CRAN-rpart >= 4.1.10
BuildRequires:    R-CRAN-pls >= 2.5.0
BuildRequires:    R-CRAN-pROC >= 1.8
BuildRequires:    R-CRAN-e1071 >= 1.6.7
BuildRequires:    R-CRAN-lars >= 1.2
BuildRequires:    R-CRAN-elasticnet >= 1.1
BuildRequires:    R-CRAN-tree >= 1.0.37
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-MSQC 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-MASS >= 7.3.45
Requires:         R-CRAN-class >= 7.3.14
Requires:         R-CRAN-nnet >= 7.3.12
Requires:         R-CRAN-caret >= 6.0.71
Requires:         R-CRAN-randomForest >= 4.6.12
Requires:         R-CRAN-rpart >= 4.1.10
Requires:         R-CRAN-pls >= 2.5.0
Requires:         R-CRAN-pROC >= 1.8
Requires:         R-CRAN-e1071 >= 1.6.7
Requires:         R-CRAN-lars >= 1.2
Requires:         R-CRAN-elasticnet >= 1.1
Requires:         R-CRAN-tree >= 1.0.37
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-MSQC 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 

%description
Contains a set of methods for fitting models and methods for validating
the resulting models. The statistical methodologies comprise a
comprehensive collection of approaches whose validity and utility have
been accepted by experts in the Cheminformatics field. As promising new
methodologies emerge from the statistical and data-mining communities,
they will be incorporated into the laboratory. These methods are aimed at
discovering quantitative structure-activity relationships (QSARs).
However, the user can directly input their own choices of descriptors and
responses, so the capability for comparing models is effectively
unlimited.

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
