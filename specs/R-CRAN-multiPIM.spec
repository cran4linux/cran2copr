%global packname  multiPIM
%global packver   1.4-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          3%{?dist}
Summary:          Variable Importance Analysis with Population Intervention Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lars >= 0.9.8
BuildRequires:    R-CRAN-penalized 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-rpart 
Requires:         R-CRAN-lars >= 0.9.8
Requires:         R-CRAN-penalized 
Requires:         R-CRAN-polspline 
Requires:         R-rpart 

%description
Performs variable importance analysis using a causal inference approach.
This is done by fitting Population Intervention Models. The default is to
use a Targeted Maximum Likelihood Estimator (TMLE). The other available
estimators are Inverse Probability of Censoring Weighted (IPCW),
Double-Robust IPCW (DR-IPCW), and Graphical Computation (G-COMP)
estimators. Inference can be obtained from the influence curve (plug-in)
or by bootstrapping.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
