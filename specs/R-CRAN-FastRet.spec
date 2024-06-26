%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FastRet
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Retention Time Prediction in Liquid Chromatography

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-rcdk 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-shinyhelper 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-xlsx 
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-rcdk 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-shinyhelper 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-xlsx 

%description
A framework for predicting retention times in liquid chromatography. Users
can train custom models for specific chromatography columns, predict
retention times using existing models, or adjust existing models to
account for altered experimental conditions. The provided functionalities
can be accessed either via the R console or via a graphical user
interface. Related work: Bonini et al. (2020)
<doi:10.1021/acs.analchem.9b05765>.

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
