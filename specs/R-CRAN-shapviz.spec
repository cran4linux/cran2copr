%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shapviz
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          SHAP Visualizations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-ggfittext >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-gggenes 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-ggfittext >= 0.8.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-gggenes 
Requires:         R-CRAN-ggrepel 
Requires:         R-grid 
Requires:         R-CRAN-patchwork 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xgboost 

%description
Visualizations for SHAP (SHapley Additive exPlanations), such as waterfall
plots, force plots, various types of importance plots, dependence plots,
and interaction plots.  These plots act on a 'shapviz' object created from
a matrix of SHAP values and a corresponding feature dataset. Wrappers for
the R packages 'xgboost', 'lightgbm', 'fastshap', 'shapr', 'h2o',
'treeshap', 'DALEX', and 'kernelshap' are added for convenience.  By
separating visualization and computation, it is possible to display factor
variables in graphs, even if the SHAP values are calculated by a model
that requires numerical features. The plots are inspired by those provided
by the 'shap' package in Python, but there is no dependency on it.

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
