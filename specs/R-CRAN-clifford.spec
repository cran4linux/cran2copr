%global packname  clifford
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Arbitrary Dimensional Clifford Algebras

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.5

%description
A suite of routines for Clifford algebras, using the 'Map' class of the
Standard Template Library.  Canonical reference: Hestenes (1987, ISBN
90-277-1673-0, "Clifford algebra to geometric calculus").  Special cases
including Lorentz transforms, quaternion multiplication, and Grassman
algebra, are discussed. Conformal geometric algebra theory is implemented.

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
%doc %{rlibdir}/%{packname}/conformal_algebra.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/linear_algebra.Rmd
%doc %{rlibdir}/%{packname}/lorentz_clifford.Rmd
%doc %{rlibdir}/%{packname}/quaternion_clifford.Rmd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
