%global __brp_check_rpaths %{nil}
%global packname  prodest
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Production Function Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-parallel 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-AER 
Requires:         R-CRAN-dplyr 
Requires:         R-parallel 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-AER 

%description
Implements the methods proposed by Olley, G.S. and Pakes, A. (1996)
<doi:10.2307/2171831>, Levinsohn, J. and Petrin, A. (2003)
<doi:10.1111/1467-937X.00246>, Ackerberg, D.A. and Caves, K. and Frazer,
G. (2015) <doi:10.3982/ECTA13408> and Wooldridge, J.M. (2009)
<doi:10.1016/j.econlet.2009.04.026> for structural productivity estimation
.

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
