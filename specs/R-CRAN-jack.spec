%global packname  jack
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Jack, Zonal, and Schur Polynomials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-mvp 
BuildRequires:    R-CRAN-multicool 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-mvp 
Requires:         R-CRAN-multicool 

%description
Symbolic calculation and evaluation of the Jack polynomials, zonal
polynomials, and Schur polynomials. Mainly based on Demmel & Koev's paper
(2006) <doi:10.1090/S0025-5718-05-01780-1>. Zonal polynomials and Schur
polynomials are particular cases of Jack polynomials. Zonal polynomials
appear in random matrix theory. Schur polynomials appear in the field of
combinatorics.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
