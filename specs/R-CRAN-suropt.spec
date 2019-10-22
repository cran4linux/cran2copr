%global packname  suropt
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Surrogate-Based Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-DiceOptim 
BuildRequires:    R-CRAN-GPareto 
BuildRequires:    R-CRAN-emoa 
BuildRequires:    R-CRAN-mco 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-GenSA 
Requires:         R-methods 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-DiceOptim 
Requires:         R-CRAN-GPareto 
Requires:         R-CRAN-emoa 
Requires:         R-CRAN-mco 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-GenSA 

%description
Multi-Objective optimization based on surrogate models. Important
functions: build_surmodel, train_hego, train_mego, train_sme.

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
