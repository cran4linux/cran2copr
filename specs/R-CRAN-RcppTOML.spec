%global packname  RcppTOML
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          2%{?dist}
Summary:          'Rcpp' Bindings to Parser for Tom's Obvious Markup Language

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-Rcpp >= 0.11.5

%description
The configuration format defined by 'TOML' (which expands to "Tom's
Obvious Markup Language") specifies an excellent format (described at
<https://github.com/toml-lang/toml>) suitable for both human editing as
well as the common uses of a machine-readable format. This package uses
'Rcpp' to connect the 'cpptoml' parser written by Chase Geigle (in modern
C++11) to R.

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
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/tinytest
%doc %{rlibdir}/%{packname}/toml
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
