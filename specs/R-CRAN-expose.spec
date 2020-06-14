%global packname  expose
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          2%{?dist}
Summary:          Multiple Effect Estimation of Chemicals in EnvironmentalEpidemiology

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-repmis 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-Matrix 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-repmis 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-gam 
Requires:         R-splines 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmnet 
Requires:         R-Matrix 
Requires:         R-nnet 
Requires:         R-CRAN-polspline 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Estimate individual and average joint effects of chemical mixtures,
dose-response relationships, and potential interactions in environmental
epidemiology. The visualization of interactions and the plotting of all
the objects. For more information please, check next work: Youssef
Oulhote, Marie-Abele Bind, Brent Coull, Chirag, Patel, Philippe Grandjean
(2017)
<https://www.biorxiv.org/content/early/2017/06/30/147413.article-info>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
