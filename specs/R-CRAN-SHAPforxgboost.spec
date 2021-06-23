%global __brp_check_rpaths %{nil}
%global packname  SHAPforxgboost
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          SHAP Plots for 'XGBoost'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-xgboost >= 0.81.0.0
BuildRequires:    R-CRAN-ggExtra >= 0.8
BuildRequires:    R-CRAN-ggforce >= 0.2.1.9000
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-BBmisc 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-xgboost >= 0.81.0.0
Requires:         R-CRAN-ggExtra >= 0.8
Requires:         R-CRAN-ggforce >= 0.2.1.9000
Requires:         R-stats 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-BBmisc 

%description
Aid in visual data investigations using SHAP (SHapley Additive
exPlanation) visualization plots for 'XGBoost' and 'LightGBM'. It provides
summary plot, dependence plot, interaction plot, and force plot and relies
on the SHAP implementation provided by 'XGBoost' and 'LightGBM'. Please
refer to 'slundberg/shap' for the original implementation of SHAP in
'Python'.

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
