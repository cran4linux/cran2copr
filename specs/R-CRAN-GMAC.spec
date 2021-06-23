%global __brp_check_rpaths %{nil}
%global packname  GMAC
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Genomic Mediation Analysis with Adaptive Confounding Adjustment

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
Requires:         R-parallel 

%description
Performs genomic mediation analysis with adaptive confounding adjustment
(GMAC) proposed by Yang et al. (2017) <doi:10.1101/078683>. It implements
large scale mediation analysis and adaptively selects potential
confounding variables to adjust for each mediation test from a pool of
candidate confounders. The package is tailored for but not limited to
genomic mediation analysis (e.g., cis-gene mediating trans-gene regulation
pattern where an eQTL, its cis-linking gene transcript, and its trans-gene
transcript play the roles as treatment, mediator and the outcome,
respectively), restricting to scenarios with the presence of
cis-association (i.e., treatment-mediator association) and random eQTL
(i.e., treatment).

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
%{rlibdir}/%{packname}/INDEX
