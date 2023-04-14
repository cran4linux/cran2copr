%global __brp_check_rpaths %{nil}
%global packname  cmaesr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Covariance Matrix Adaptation Evolution Strategy

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ParamHelpers >= 1.8
BuildRequires:    R-CRAN-BBmisc >= 1.6
BuildRequires:    R-CRAN-smoof >= 1.4
BuildRequires:    R-CRAN-checkmate >= 1.1
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ParamHelpers >= 1.8
Requires:         R-CRAN-BBmisc >= 1.6
Requires:         R-CRAN-smoof >= 1.4
Requires:         R-CRAN-checkmate >= 1.1
Requires:         R-CRAN-ggplot2 

%description
Pure R implementation of the Covariance Matrix Adaptation - Evolution
Strategy (CMA-ES) with optional restarts (IPOP-CMA-ES).

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
