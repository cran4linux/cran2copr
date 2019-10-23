%global packname  RFmarkerDetector
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Multivariate Analysis of Metabolomics Data using Random Forests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AUCRF 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-UsingR 
BuildRequires:    R-CRAN-WilcoxCV 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-methods 
Requires:         R-CRAN-AUCRF 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-UsingR 
Requires:         R-CRAN-WilcoxCV 
Requires:         R-CRAN-ROCR 
Requires:         R-methods 

%description
A collection of tools for multivariate analysis of metabolomics data,
which includes several preprocessing methods (normalization, scaling) and
various exploration and data visualization techniques (Principal
Components Analysis and Multi Dimensional Scaling). The core of the
package is the Random Forest algorithm used for the construction,
optimization and validation of classification models with the aim of
identifying potentially relevant biomarkers.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
