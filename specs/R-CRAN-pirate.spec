%global packname  pirate
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Generated Effect Modifier

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-plyr 
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 

%description
An implementation of the generated effect modifier (GEM) method. This
method constructs composite variables by linearly combining pre-treatment
scalar patient characteristics to create optimal treatment effect
modifiers in linear models. The optimal linear combination is called a
GEM. Treatment is assumed to have been assigned at random. For reference,
see E Petkova, T Tarpey, Z Su, and RT Ogden. Generated effect modifiers
(GEMs) in randomized clinical trials. Biostatistics (First published
online: July 27, 2016, <doi:10.1093/biostatistics/kxw035>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
