%global packname  iDINGO
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Integrative Differential Network Analysis in Genomics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-GGMridge 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-glasso 
Requires:         R-parallel 
Requires:         R-CRAN-GGMridge 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-scales 

%description
Fits covariate dependent partial correlation matrices for integrative
models to identify differential networks between two groups. The methods
are described in Class et. al., (2018) <doi:10.1093/bioinformatics/btx750>
and Ha et. al., (2015) <doi:10.1093/bioinformatics/btv406>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
