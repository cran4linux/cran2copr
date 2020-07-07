%global packname  AHM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Additive Heredity Model: Method for the Mixture-of-MixturesExperiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mixexp 
BuildRequires:    R-CRAN-plgp 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mixexp 
Requires:         R-CRAN-plgp 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-Matrix 

%description
An implementation of the additive heredity model for the
mixture-of-mixtures experiments of Shen et al. (2019) in Technometrics
<doi:10.1080/00401706.2019.1630010>. The additive heredity model considers
an additive structure to inherently connect the major components with the
minor components. The additive heredity model has a meaningful
interpretation for the estimated model because of the hierarchical and
heredity principles applied and the nonnegative garrote technique used for
variable selection.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
