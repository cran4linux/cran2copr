%global packname  bigstep
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Stepwise Selection for Large Data Sets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-speedglm 
Requires:         R-stats 
Requires:         R-utils 

%description
Selecting linear and generalized linear models for large data sets using
modified stepwise procedure and modern selection criteria (like
modifications of Bayesian Information Criterion). Selection can be
performed on data which exceed RAM capacity.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
