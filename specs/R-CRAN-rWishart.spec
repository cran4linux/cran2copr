%global __brp_check_rpaths %{nil}
%global packname  rWishart
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Random Wishart Matrix Generation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lazyeval 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-lazyeval 

%description
An expansion of R's 'stats' random wishart matrix generation. This package
allows the user to generate singular, Uhlig and Harald (1994)
<doi:10.1214/aos/1176325375>, and pseudo wishart, Diaz-Garcia, et
al.(1997) <doi:10.1006/jmva.1997.1689>, matrices. In addition the user can
generate wishart matrices with fractional degrees of freedom, Adhikari
(2008) <doi:10.1061/(ASCE)0733-9399(2008)134:12(1029)>, commonly used in
volatility modeling. Users can also use this package to create random
covariance matrices.

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
