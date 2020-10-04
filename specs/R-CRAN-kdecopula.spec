%global packname  kdecopula
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          3%{?dist}%{?buildtag}
Summary:          Kernel Smoothing for Bivariate Copula Densities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-qrng 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-lattice 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-qrng 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-quadprog 

%description
Provides fast implementations of kernel smoothing techniques for bivariate
copula densities, in particular density estimation and resampling, see
Nagler (2018) <doi:10.18637/jss.v084.i07>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/README-unnamed-chunk-10-1.png
%doc %{rlibdir}/%{packname}/README-unnamed-chunk-12-1.png
%doc %{rlibdir}/%{packname}/README-unnamed-chunk-3-1.png
%doc %{rlibdir}/%{packname}/README-unnamed-chunk-6-1.png
%doc %{rlibdir}/%{packname}/README-unnamed-chunk-7-1.png
%doc %{rlibdir}/%{packname}/README-unnamed-chunk-8-1.png
%doc %{rlibdir}/%{packname}/README-unnamed-chunk-9-1.png
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
