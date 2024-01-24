%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fungible
%global packver   2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Psychometric Functions from the Waller Lab

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-MBESS >= 4.8.0
BuildRequires:    R-CRAN-GA >= 3.2.1
BuildRequires:    R-CRAN-sem >= 3.1.11
BuildRequires:    R-CRAN-crayon >= 1.4.1
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-Rcsdp 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-MBESS >= 4.8.0
Requires:         R-CRAN-GA >= 3.2.1
Requires:         R-CRAN-sem >= 3.1.11
Requires:         R-CRAN-crayon >= 1.4.1
Requires:         R-CRAN-clue 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MCMCpack 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-pbmcapply 
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
Behavioral Research, 51(4), 554-568. Jones, J. A. & Waller, N. G. (2015).
The normal-theory and asymptotic distribution-free (ADF) covariance matrix
of standardized regression coefficients: theoretical extensions and finite
sample behavior. Psychometrika, 80, 365-378,
<DOI:10.1007/s11336-013-9380-y>. Waller, N. G.  (2018).  Direct
Schmid-Leiman transformations and rank-deficient loadings matrices.
Psychometrika, 83, 858-870. <DOI:10.1007/s11336-017-9599-0>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
