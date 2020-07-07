%global packname  ingredients
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          2%{?dist}
Summary:          Effects and Importances of Model Ingredients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 

%description
Collection of tools for assessment of feature importance and feature
effects. Key functions are: feature_importance() for assessment of global
level feature importance, ceteris_paribus() for calculation of the what-if
plots, partial_dependence() for partial dependence plots,
conditional_dependence() for conditional dependence plots,
accumulated_dependence() for accumulated local effects plots,
aggregate_profiles() and cluster_profiles() for aggregation of ceteris
paribus profiles, generic print() and plot() for better usability of
selected explainers, generic plotD3() for interactive, D3 based
explanations, and generic describe() for explanations in natural language.
The package 'ingredients' is a part of the 'DrWhy.AI' universe (Biecek
2018) <arXiv:1806.08915>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
