%global packname  IsingFit
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Fitting Ising Models Using the ELasso Method

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-qgraph 
Requires:         R-Matrix 
Requires:         R-CRAN-glmnet 

%description
This network estimation procedure eLasso, which is based on the Ising
model, combines l1-regularized logistic regression with model selection
based on the Extended Bayesian Information Criterion (EBIC). EBIC is a fit
measure that identifies relevant relationships between variables. The
resulting network consists of variables as nodes and relevant
relationships as edges. Can deal with binary data.

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
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
