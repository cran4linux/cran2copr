%global __brp_check_rpaths %{nil}
%global packname  mvQuad
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Multivariate Quadrature

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-statmod 
Requires:         R-methods 

%description
Provides methods to construct multivariate grids, which can be used for
multivariate quadrature. This grids can be based on different quadrature
rules like Newton-Cotes formulas (trapezoidal-, Simpson's- rule, ...) or
Gauss quadrature (Gauss-Hermite, Gauss-Legendre, ...). For the
construction of the multidimensional grid the product-rule or the
combination- technique can be applied.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
