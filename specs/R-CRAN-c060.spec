%global packname  c060
%global packver   0.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Extended Inference for Lasso and Elastic-Net Regularized Cox andGeneralized Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-survival 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mlegp 
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-CRAN-peperr 
BuildRequires:    R-CRAN-penalizedSVM 
BuildRequires:    R-lattice 
Requires:         R-CRAN-glmnet 
Requires:         R-survival 
Requires:         R-parallel 
Requires:         R-CRAN-mlegp 
Requires:         R-CRAN-tgp 
Requires:         R-CRAN-peperr 
Requires:         R-CRAN-penalizedSVM 
Requires:         R-lattice 

%description
c060 provides additional functions to perform stability selection, model
validation and parameter tuning for glmnet models

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
