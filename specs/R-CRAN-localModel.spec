%global packname  localModel
%global packver   0.3.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.12
Release:          3%{?dist}
Summary:          LIME-Based Explanations with Interpretable Inputs Based onCeteris Paribus Profiles

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-ingredients 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-ingredients 

%description
Local explanations of machine learning models describe, how features
contributed to a single prediction. This package implements an explanation
method based on LIME (Local Interpretable Model-agnostic Explanations, see
Tulio Ribeiro, Singh, Guestrin (2016) <doi:10.1145/2939672.2939778>) in
which interpretable inputs are created based on local rather than global
behaviour of each original feature.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
