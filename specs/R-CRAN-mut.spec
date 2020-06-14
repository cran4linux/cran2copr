%global packname  mut
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Pairwise Likelihood Ratios

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Familias 
BuildRequires:    R-CRAN-paramlink 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-IBDsim 
Requires:         R-CRAN-Familias 
Requires:         R-CRAN-paramlink 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-IBDsim 

%description
Main function LR2 calculates likelihood ratio for non-inbred relationships
accounting for mutation, silent alleles and theta correction. Egeland,
Pinto and Amorim (2017) <DOI:10.1016/j.fsigen.2017.04.018>.

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
