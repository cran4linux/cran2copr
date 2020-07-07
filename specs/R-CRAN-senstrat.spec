%global packname  senstrat
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Sensitivity Analysis for Stratified Observational Studies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BiasedUrn 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-BiasedUrn 
Requires:         R-MASS 

%description
Sensitivity analysis in unmatched observational studies, with or without
strata.  The main functions are sen2sample() and senstrat().  See
Rosenbaum, P. R. and Krieger, A. M. (1990), JASA, 85, 493-498,
<doi:10.1080/01621459.1990.10476226> and Gastwirth, Krieger and Rosenbaum
(2000), JRSS-B, 62, 545–555 <doi:10.1111/1467-9868.00249> .

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
