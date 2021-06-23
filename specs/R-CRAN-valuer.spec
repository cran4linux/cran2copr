%global __brp_check_rpaths %{nil}
%global packname  valuer
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Pricing of Variable Annuities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildRequires:    R-CRAN-timeDate >= 3012.1
BuildRequires:    R-CRAN-R6 >= 2.1.2
BuildRequires:    R-CRAN-yuima >= 1.1.6
BuildRequires:    R-CRAN-orthopolynom >= 1.0.5
BuildRequires:    R-CRAN-RcppEigen >= 0.3.2.8.1
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-timeDate >= 3012.1
Requires:         R-CRAN-R6 >= 2.1.2
Requires:         R-CRAN-yuima >= 1.1.6
Requires:         R-CRAN-orthopolynom >= 1.0.5
Requires:         R-CRAN-RcppEigen >= 0.3.2.8.1
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 

%description
Pricing of variable annuity life insurance contracts by means of Monte
Carlo methods. Monte Carlo is used to price the contract in case the
policyholder cannot surrender while Least Squares Monte Carlo is used if
the insured can surrender. This package implements the pricing framework
and algorithm described in Bacinello et al. (2011)
<doi:10.1016/j.insmatheco.2011.05.003>. It also implements the
state-dependent fee structure discussed in Bernard et al. (2014)
<doi:10.1017/asb.2014.13> as well as a function which prices the contract
by resolving the partial differential equation described in MacKay et al.
(2017) <doi:10.1111/jori.12094>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
