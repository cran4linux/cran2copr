%global packname  LPRelevance
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}
Summary:          Relevance-Integrated Statistical Inference Engine

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BayesGOF 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-locfdr 
BuildRequires:    R-CRAN-Bolstad2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-caret 
Requires:         R-stats 
Requires:         R-CRAN-BayesGOF 
Requires:         R-MASS 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-locfdr 
Requires:         R-CRAN-Bolstad2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-caret 

%description
A framework of methods to perform customized inference at individual level
by taking contextual covariates into account. Three main functions are
provided in this package: (i) LASER(): it generates specially-designed
artificial relevant samples for a given case; (ii) g2l.proc(): computes
customized fdr(z|x); and (iii) rEB.proc(): performs empirical Bayes
inference based on LASERs. The details can be found in Mukhopadhyay, S.,
and Wang, K (2020, Technical Report).

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
