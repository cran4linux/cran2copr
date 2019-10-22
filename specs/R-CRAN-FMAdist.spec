%global packname  FMAdist
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Frequentist Model Averaging Distribution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-STAR 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-STAR 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-extraDistr 
Requires:         R-MASS 
Requires:         R-CRAN-quadprog 

%description
Creation of an input model (fitted distribution) via the frequentist model
averaging (FMA) approach and generate random-variates from the
distribution specified by "myfit" which is the fitted input model via the
FMA approach. See W. X. Jiang and B. L. Nelson (2018), "Better Input
Modeling via Model Averaging," Proceedings of the 2018 Winter Simulation
Conference, IEEE Press, 1575-1586.

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
