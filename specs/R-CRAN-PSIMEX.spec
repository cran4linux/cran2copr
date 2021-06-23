%global __brp_check_rpaths %{nil}
%global packname  PSIMEX
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          SIMEX Algorithm on Pedigree Structures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCglmm 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-pedigree 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-MCMCglmm 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-pedigree 
Requires:         R-CRAN-knitr 

%description
Generalization of the SIMEX algorithm from Cook & Stefanski (1994)
<doi:10.2307/2290994> for the calculation of inbreeding depression or
heritability on pedigree structures affected by missing or misassigned
paternities. It simulates errors and tracks the behavior of the estimate
as a function of the error proportion. It extrapolates back a true value
corresponding to the null error rate.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
