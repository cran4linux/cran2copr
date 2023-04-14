%global __brp_check_rpaths %{nil}
%global packname  bindrcpp
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          An 'Rcpp' Interface to Active Bindings

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-bindr >= 0.1.1
BuildRequires:    R-CRAN-plogr 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-bindr >= 0.1.1

%description
Provides an easy way to fill an environment with active bindings that call
a C++ function.

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
