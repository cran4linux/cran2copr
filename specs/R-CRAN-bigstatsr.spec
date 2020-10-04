%global packname  bigstatsr
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Tools for Filebacked Big Matrices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-bigparallelr >= 0.2.3
BuildRequires:    R-CRAN-rmio >= 0.1.3
BuildRequires:    R-CRAN-bigassertr >= 0.1.1
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-bigparallelr >= 0.2.3
Requires:         R-CRAN-bigassertr >= 0.1.1
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RSpectra 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Easy-to-use, efficient, flexible and scalable statistical tools. Package
bigstatsr provides and uses Filebacked Big Matrices via memory-mapping. It
provides for instance matrix operations, Principal Component Analysis,
sparse linear supervised models, utility functions and more
<doi:10.1093/bioinformatics/bty185>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/testdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
