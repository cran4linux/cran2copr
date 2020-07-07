%global packname  LGEWIS
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Tests for Genetic Association/Gene-Environment Interaction inLongitudinal Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-SKAT 
BuildRequires:    R-CRAN-geeM 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-SKAT 
Requires:         R-CRAN-geeM 
Requires:         R-splines 
Requires:         R-CRAN-mvtnorm 

%description
Functions for genome-wide association studies (GWAS)/gene-environment-wide
interaction studies (GEWIS) with longitudinal outcomes and exposures. He
et al. (2017) "Set-Based Tests for Gene-Environment Interaction in
Longitudinal Studies" and He et al. (2017) "Rare-variant association tests
in longitudinal studies, with an application to the Multi-Ethnic Study of
Atherosclerosis (MESA)".

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
