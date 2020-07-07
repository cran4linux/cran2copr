%global packname  TANDEM
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          A Two-Stage Approach to Maximize Interpretability of DrugResponse Models Based on Multiple Molecular Data Types

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 3.0
BuildRequires:    R-Matrix 
Requires:         R-CRAN-glmnet >= 3.0
Requires:         R-Matrix 

%description
A two-stage regression method that can be used when various input data
types are correlated, for example gene expression and methylation in drug
response prediction. In the first stage it uses the upstream features
(such as methylation) to predict the response variable (such as drug
response), and in the second stage it uses the downstream features (such
as gene expression) to predict the residuals of the first stage. In our
manuscript (Aben et al., 2016, <doi:10.1093/bioinformatics/btw449>), we
show that using TANDEM prevents the model from being dominated by gene
expression and that the features selected by TANDEM are more
interpretable.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
