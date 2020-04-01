%global packname  zcurve
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          An Implementation of Z-Curves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-evmix 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-nleqslv 
Requires:         R-stats 
Requires:         R-CRAN-evmix 
Requires:         R-graphics 
Requires:         R-CRAN-Rdpack 

%description
An implementation of z-curves - a method for estimating expected discovery
and replicability rates on the bases of test-statistics of published
studies. The package provides functions for fitting the new density and EM
version (Bartoš & Schimmack, 2020, <doi:10.31234/osf.io/urgtn>) as well as
the original density z-curve (Brunner & Schimmack, 2017,
<doi:10.31219/osf.io/wr93f>). Furthermore, the package provides
summarizing and plotting functions for the fitted z-curve objects. See the
aforementioned articles for more information about the z-curves, expected
discovery and replicability rates, validation studies, and limitations.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
