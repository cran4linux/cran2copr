%global __brp_check_rpaths %{nil}
%global packname  modelROC
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Based ROC Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-do 
BuildRequires:    R-CRAN-tmcn 
BuildRequires:    R-CRAN-ROCit 
BuildRequires:    R-CRAN-survivalROC 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-do 
Requires:         R-CRAN-tmcn 
Requires:         R-CRAN-ROCit 
Requires:         R-CRAN-survivalROC 

%description
The ROC curve method is one of the most important and commonly used
methods for model accuracy assessment, which is one of the most important
elements of model evaluation. The 'modelROC' package is a model-based ROC
assessment tool, which directly works for ROC analysis of regression
results for logistic regression of binary variables, including the glm()
and lrm() commands, and COX regression for survival analysis, including
the cph() and coxph() commands. The most important feature of 'modelROC'
is that both the model and the independent variables can be analysed
simultaneously, and for survival analysis multiple time points and area
under the curve analysis are supported. Still, flexible visualisation is
possible with the 'ggplot2' package. Reference are Kelly H. Zou (1998)
<doi:10.1002/(sici)1097-0258(19971015)16:19%%3C2143::aid-sim655%%3E3.0.co;2-3>
and P J Heagerty (2000) <doi:10.1111/j.0006-341x.2000.00337.x>.

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
