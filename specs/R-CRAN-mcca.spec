%global packname  mcca
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Multi-Category Classification Accuracy

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nnet 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-caret 
Requires:         R-nnet 
Requires:         R-rpart 
Requires:         R-CRAN-e1071 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-caret 

%description
It contains six common multi-category classification accuracy evaluation
measures: Hypervolume Under Manifold (HUM), described in Li and Fine
(2008) <doi:10.1093/biostatistics/kxm050>. Correct Classification
Percentage (CCP), Integrated Discrimination Improvement (IDI), Net
Reclassification Improvement (NRI), R-Squared Value (RSQ), described in
Li, Jiang and Fine (2013) <doi:10.1093/biostatistics/kxs047>. Polytomous
Discrimination Index (PDI), described in Van Calster et al. (2012)
<doi:10.1007/s10654-012-9733-3>. Li et al. (2018)
<doi:10.1177/0962280217692830>. We described all these above measures and
our mcca package in Li, Gao and D'Agostino (2019) <doi:10.1002/sim.8103>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
