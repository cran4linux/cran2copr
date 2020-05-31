%global packname  Rdtq
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Density Tracking by Quadrature

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-Rcpp >= 0.12.4

%description
Implementation of density tracking by quadrature (DTQ) algorithms for
stochastic differential equations (SDEs).  DTQ algorithms numerically
compute the density function of the solution of an SDE with user-specified
drift and diffusion functions.  The calculation does not require
generation of sample paths, but instead proceeds in a deterministic
fashion by repeatedly applying quadrature to the Chapman-Kolmogorov
equation associated with a discrete-time approximation of the SDE.  The
DTQ algorithm is provably convergent.  For several practical problems of
interest, we have found the DTQ algorithm to be fast, accurate, and easy
to use.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/libs
