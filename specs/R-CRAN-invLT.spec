%global packname  invLT
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Inversion of Laplace-Transformed Functions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides two functions for the numerical inversion of Laplace-Transformed
functions, returning the value of the standard (time) domain function at a
specified value.  The first algorithm is the first optimum contour
algorithm described by Evans and Chung (2000)[1]. The second algorithm
uses the Bromwich contour as per the definition of the inverse Laplace
Transform.  The latter is unstable for numerical inversion and mainly
included for comparison or interest.  There are also some additional
functions provided for utility, including plotting and some simple Laplace
Transform examples, for which there are known analytical solutions.
Polar-cartesian conversion functions are included in this package and are
used by the inversion functions. [1] Evans & Chung, 2000: Laplace
transform inversions using optimal contours in the complex plane;
International Journal of Computer Mathematics v73 pp531-543.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
