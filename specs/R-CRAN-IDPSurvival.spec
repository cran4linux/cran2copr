%global packname  IDPSurvival
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Imprecise Dirichlet Process for Survival Analysis

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-survival 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-gtools 
Requires:         R-survival 

%description
Functions to perform robust nonparametric survival analysis with right
censored data using a prior near-ignorant Dirichlet Process. Mangili, F.,
Benavoli, A., de Campos, C.P., Zaffalon, M. (2015)
<doi:10.1002/bimj.201500062>.

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
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
