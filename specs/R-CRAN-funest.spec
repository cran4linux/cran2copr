%global packname  funest
%global packver   0.0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.3
Release:          2%{?dist}
Summary:          Functional Ensemble Survival Tree for Dynamic Prediction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MFPCA 
BuildRequires:    R-CRAN-funData 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-tdROC 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-MFPCA 
Requires:         R-CRAN-funData 
Requires:         R-CRAN-ranger 
Requires:         R-survival 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-tdROC 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-purrr 

%description
A fast implementation of functional ensemble survival tree is provided to
facilitate dynamic prediction with right-censored data. Multiple
time-varying covariates can be accommodated via multivariate principal
component analysis. These extracted features along with baseline
covariates are nested within the ensemble survival tree where dynamic
prediction can be done under user-specified sliding windows. Prediction
accuracy measures, Area under the receiver operating characteristic (ROC)
curve and Brier score, are provided in this package.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
