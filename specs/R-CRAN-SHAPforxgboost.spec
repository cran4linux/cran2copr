%global packname  SHAPforxgboost
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          2%{?dist}
Summary:          SHAP Plots for 'XGBoost'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-xgboost >= 0.81.0.0
BuildRequires:    R-CRAN-ggExtra >= 0.8
BuildRequires:    R-CRAN-ggforce >= 0.2.1.9000
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-BBmisc 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-xgboost >= 0.81.0.0
Requires:         R-CRAN-ggExtra >= 0.8
Requires:         R-CRAN-ggforce >= 0.2.1.9000
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-BBmisc 

%description
The aim of 'SHAPforxgboost' is to aid in visual data investigations using
SHAP (SHapley Additive exPlanation) visualization plots for 'XGBoost'. It
provides summary plot, dependence plot, interaction plot, and force plot.
It relies on the 'dmlc/xgboost' package to produce SHAP values. Please
refer to 'slundberg/shap' for the original implementation of SHAP in
'Python'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
