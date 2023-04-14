%global __brp_check_rpaths %{nil}
%global packname  EurosarcBayes
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Single Arm Sample Size Calculation Software

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-clinfun 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-CRAN-clinfun 

%description
Bayesian sample size calculation software and examples for EuroSARC
clinical trials which utilise Bayesian methodology. These trials rely on
binomial based endpoints so the majority of programs found here relate to
this sort of endpoint. Developed as part of the EuroSARC FP7 grant.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
