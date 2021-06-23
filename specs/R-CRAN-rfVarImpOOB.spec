%global __brp_check_rpaths %{nil}
%global packname  rfVarImpOOB
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unbiased Variable Importance for Random Forests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-binaryLogic 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-titanic 
BuildRequires:    R-CRAN-prob 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-binaryLogic 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-titanic 
Requires:         R-CRAN-prob 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-magrittr 

%description
Computes a novel variable importance for random forests: Impurity
reduction importance scores for out-of-bag (OOB) data complementing the
existing inbag Gini importance, see also <doi:
10.1080/03610926.2020.1764042>. The Gini impurities for inbag and OOB data
are combined in three different ways, after which the information gain is
computed at each split. This gain is aggregated for each split variable in
a tree and averaged across trees.

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
