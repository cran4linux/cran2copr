%global __brp_check_rpaths %{nil}
%global packname  aGE
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          3%{?dist}%{?buildtag}
Summary:          Adaptive Set-Based Gene-Environment Interaction Test for RareVariants

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-stats 
Requires:         R-nlme 
Requires:         R-MASS 
Requires:         R-CRAN-survey 
Requires:         R-stats 

%description
Tests gene-environment interaction for rare genetic variants within the
framework of adaptive sum of powered score test. The package includes two
tests: adaptive gene-by-environment interaction test, and joint test for
genetic main effects and gene-environment interaction. See Yang et al
(2018) <doi:10.1002/sim.8037>.

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
