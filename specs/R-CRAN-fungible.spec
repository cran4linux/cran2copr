%global packname  fungible
%global packver   1.95
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.95
Release:          1%{?dist}
Summary:          Psychometric Functions from the Waller Lab

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-Rcsdp 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-GPArotation 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-Rcsdp 
Requires:         R-CRAN-RSpectra 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Computes fungible coefficients and Monte Carlo data. Underlying theory for
these functions is described in the following publications: Waller, N.
(2008). Fungible Weights in Multiple Regression. Psychometrika, 73(4),
691-703, <DOI:10.1007/s11336-008-9066-z>. Waller, N. & Jones, J. (2009).
Locating the Extrema of Fungible Regression Weights. Psychometrika, 74(4),
589-602, <DOI:10.1007/s11336-008-9087-7>. Waller, N. G. (2016). Fungible
Correlation Matrices: A Method for Generating Nonsingular, Singular, and
Improper Correlation Matrices for Monte Carlo Research. Multivariate
Behavioral Research, 51(4), 554-568, <DOI:10.1080/00273171.2016.1178566>.
Jones, J. A. & Waller, N. G. (2015). The normal-theory and asymptotic
distribution-free (ADF) covariance matrix of standardized regression
coefficients: theoretical extensions and finite sample behavior.
Psychometrika, 80, 365-378, <DOI:10.1007/s11336-013-9380-y>. Waller, N. G.
(2018).  Direct Schmid-Leiman transformations and rank-deficient loadings
matrices.  Psychometrika, 83, 858-870. <DOI:10.1007/s11336-017-9599-0>.

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
%doc %{rlibdir}/%{packname}/news
%{rlibdir}/%{packname}/INDEX
