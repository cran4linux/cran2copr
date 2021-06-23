%global __brp_check_rpaths %{nil}
%global packname  gwfa
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Geographically Weighted Fractal Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-methods 
Requires:         R-CRAN-sp 

%description
Performs Geographically Weighted Fractal Analysis (GWFA) to calculate the
local fractal dimension of a set of points. GWFA mixes the Sandbox
multifractal algorithm and the Geographically Weighted Regression. Unlike
fractal box-counting algorithm, the sandbox algorithm avoids border
effects because the boxes are adjusted on the set of points. The
Geographically Weighted approach consists in applying a kernel that
describes the way the neighbourhood of each estimated point is taken into
account to estimate its fractal dimension. GWFA can be used to
discriminate built patterns of a city, a region, or a whole country.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
