%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClassificationEnsembles
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatically Builds 20 Classification Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-CRAN-MachineShop 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-reactablefmtr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tree 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-car 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-ipred 
Requires:         R-CRAN-MachineShop 
Requires:         R-CRAN-magrittr 
Requires:         R-parallel 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-reactablefmtr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tree 

%description
Automatically builds 20 classification models from data. The package
returns 26 plots, 5 tables and a summary report. The package automatically
builds 12 individual classification models, including error (RMSE) and
predictions. That data is used to create an ensemble, which is then
modeled using 8 methods. The process is repeated as many times as the user
requests. The mean of the results are presented in a summary table. The
package returns the confusion matrices for all 20 models, tables of the
correlation of the numeric data, the results of the variance inflation
process, the head of the ensemble and the head of the data frame.

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
