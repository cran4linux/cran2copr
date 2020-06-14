%global packname  planor
%global packver   1.5-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          2%{?dist}
Summary:          Generation of Regular Factorial Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-conf.design 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-conf.design 
Requires:         R-utils 
Requires:         R-CRAN-bit64 

%description
Automatic generation of regular factorial designs, including fractional
designs, orthogonal block designs, row-column designs and split-plots.
See: Kobilinsky, Monod and Bailey (2017) Computational Statistics and Data
Analysis 113, 311-329, <doi:10.1016/j.csda.2016.09.003>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
