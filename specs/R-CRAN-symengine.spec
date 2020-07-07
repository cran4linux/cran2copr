%global packname  symengine
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}
Summary:          Interface to the 'SymEngine' Library

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cmake
BuildRequires:    gmp-devel
BuildRequires:    mpfr-devel
BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Provides an R interface to 'SymEngine' <https://github.com/symengine/>, a
standalone 'C++' library for fast symbolic manipulation. The package has
functionalities for symbolic computation like calculating exact
mathematical expressions, solving systems of linear equations and code
generation.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
