%global packname  seqMeta
%global packver   1.6.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.7
Release:          3%{?dist}
Summary:          Meta-Analysis of Region-Based Tests of Rare DNA Variants

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-coxme >= 2.2.4
BuildRequires:    R-methods 
BuildRequires:    R-survival 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-CompQuadForm 
Requires:         R-CRAN-coxme >= 2.2.4
Requires:         R-methods 
Requires:         R-survival 
Requires:         R-Matrix 
Requires:         R-CRAN-CompQuadForm 

%description
Computes necessary information to meta analyze region-based tests for rare
genetic variants (e.g. SKAT, T1) in individual studies, and performs meta
analysis.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
