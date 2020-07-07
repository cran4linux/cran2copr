%global packname  isqg
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          In Silico Quantitative Genetics

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rdpack 

%description
Accomplish high performance simulations in quantitative genetics. The
molecular genetic components are represented by R6/C++ classes and
methods. The core computational algorithm is implemented using bitsets
according to <doi:10.1534/g3.119.400373>. A mix between low and high level
interfaces provides great flexibility and allows user defined extensions
and a wide range of applications.

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

%files
%{rlibdir}/%{packname}
