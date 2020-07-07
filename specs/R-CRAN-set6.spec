%global packname  set6
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}
Summary:          R6 Mathematical Sets Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-R6 
Requires:         R-utils 

%description
An object-oriented package for mathematical sets, upgrading the current
gold-standard {sets}. Many forms of mathematical sets are implemented,
including (countably finite) sets, tuples, intervals (countably infinite
or uncountable), and fuzzy variants. Wrappers extend functionality by
allowing symbolic representations of complex operations on sets, including
unions, (cartesian) products, exponentiation, and differences (asymmetric
and symmetric).

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
