%global packname  Rlibeemd
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Ensemble Empirical Mode Decomposition (EEMD) and Its CompleteVariant (CEEMDAN)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
Requires:         gsl
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 

%description
An R interface for libeemd (Luukko, Helske, Räsänen, 2016)
<doi:10.1007/s00180-015-0603-9>, a C library of highly efficient
parallelizable functions for performing the ensemble empirical mode
decomposition (EEMD), its complete variant (CEEMDAN), the regular
empirical mode decomposition (EMD), and bivariate EMD (BEMD). Due to the
possible portability issues CRAN version no longer supports OpenMP, you
can install OpenMP-supported version from GitHub:
<https://github.com/helske/Rlibeemd/>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
