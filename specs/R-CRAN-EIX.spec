%global packname  EIX
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Explain Interactions in 'XGBoost'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-DALEX 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggiraphExtra 
BuildRequires:    R-CRAN-iBreakDown 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-DALEX 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggiraphExtra 
Requires:         R-CRAN-iBreakDown 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-scales 

%description
Structure mining from 'XGBoost' and 'LightGBM' models. Key functionalities
of this package cover: visualisation of tree-based ensembles models,
identification of interactions, measuring of variable importance,
measuring of interaction importance, explanation of single prediction with
break down plots (based on 'xgboostExplainer' and 'iBreakDown' packages).
To download the 'LightGBM' use the following link:
<https://github.com/Microsoft/LightGBM>. 'EIX' is a part of the 'DrWhy.AI'
universe.

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
