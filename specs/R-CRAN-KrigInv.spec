%global packname  KrigInv
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Kriging-Based Inversion for Deterministic and Noisy ComputerExperiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-anMC 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-anMC 
Requires:         R-CRAN-mvtnorm 

%description
Criteria and algorithms for sequentially estimating level sets of a
multivariate numerical function, possibly observed with noise.

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
