%global packname  rmgarch
%global packver   1.3-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          2%{?dist}
Summary:          Multivariate GARCH Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.34
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-Bessel 
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-spd 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-methods 
Requires:         R-CRAN-rugarch 
Requires:         R-parallel 
Requires:         R-CRAN-Rsolnp 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-Bessel 
Requires:         R-CRAN-ff 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-spd 
Requires:         R-CRAN-Rcpp >= 0.10.6
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-corpcor 

%description
Feasible multivariate GARCH models including DCC, GO-GARCH and
Copula-GARCH. See Boudt, Galanos, Payseur and Zivot (2019) for a review of
multivariate GARCH models <doi:10.1016/bs.host.2019.01.001>.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
