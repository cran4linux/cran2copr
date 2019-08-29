%global packname  InformativeCensoring
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Multiple Imputation for Informative Censoring

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-survival >= 2.36.1
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-boot 
BuildRequires:    R-parallel 
Requires:         R-survival >= 2.36.1
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-boot 
Requires:         R-parallel 

%description
Multiple Imputation for Informative Censoring. This package implements two
methods. Gamma Imputation from Jackson et al. (2014)
<DOI:10.1002/sim.6274> and Risk Score Imputation from Hsu et al. (2009)
<DOI:10.1002/sim.3480>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/validation
%{rlibdir}/%{packname}/INDEX
