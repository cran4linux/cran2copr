%global packname  matlib
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          2%{?dist}
Summary:          Matrix Functions for Teaching and Learning Linear Algebra andMultivariate Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-methods 
Requires:         R-CRAN-xtable 
Requires:         R-MASS 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-car 
Requires:         R-methods 

%description
A collection of matrix functions for teaching and learning matrix linear
algebra as used in multivariate statistical methods. These functions are
mainly for tutorial purposes in learning matrix algebra ideas using R. In
some cases, functions are provided for concepts available elsewhere in R,
but where the function call or name is not obvious. In other cases,
functions are provided to show or demonstrate an algorithm. In addition, a
collection of functions are provided for drawing vector diagrams in 2D and
3D.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
