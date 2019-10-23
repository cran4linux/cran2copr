%global packname  iml
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Interpretable Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-yaImpute 
BuildRequires:    R-CRAN-prediction 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-yaImpute 
Requires:         R-CRAN-prediction 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gridExtra 

%description
Interpretability methods to analyze the behavior and predictions of any
machine learning model. Implemented methods are: Feature importance
described by Fisher et al. (2018) <arXiv:1801.01489>, accumulated local
effects plots described by Apley (2018) <arXiv:1612.08468>, partial
dependence plots described by Friedman (2001)
<http://www.jstor.org/stable/2699986>, individual conditional expectation
('ice') plots described by Goldstein et al. (2013)
<doi:10.1080/10618600.2014.907095>, local models (variant of 'lime')
described by Ribeiro et. al (2016) <arXiv:1602.04938>, the Shapley Value
described by Strumbelj et. al (2014) <doi:10.1007/s10115-013-0679-x>,
feature interactions described by Friedman et. al <doi:10.1214/07-AOAS148>
and tree surrogate models.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
