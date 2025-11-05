%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  roclab
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          ROC-Optimizing Binary Classifiers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-pROC 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-pROC 

%description
Implements ROC (Receiver Operating Characteristic)–Optimizing Binary
Classifiers, supporting both linear and kernel models. Both model types
provide a variety of surrogate loss functions. In addition, linear models
offer multiple regularization penalties, whereas kernel models support a
range of kernel functions. Scalability for large datasets is achieved
through approximation-based options, which accelerate training and make
fitting feasible on large data. Utilities are provided for model training,
prediction, and cross-validation. The implementation builds on the
ROC-Optimizing Support Vector Machines. For more information, see
Hernàndez-Orallo, José, et al. (2004) <doi:10.1145/1046456.1046489>,
presented in the ROC Analysis in AI Workshop (ROCAI-2004).

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
