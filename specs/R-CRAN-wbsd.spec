%global __brp_check_rpaths %{nil}
%global packname  wbsd
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Wild Bootstrap Size Diagnostics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 

%description
Implements the diagnostic "theta" developed in Poetscher and
Preinerstorfer (2020) "How Reliable are Bootstrap-based Heteroskedasticity
Robust Tests?" <arXiv:2005.04089>. This diagnostic can be used to detect
and weed out bootstrap-based procedures that provably have size equal to
one for a given testing problem. The implementation covers a large variety
of bootstrap-based procedures, cf. the above mentioned article for
details. A function for computing bootstrap p-values is provided.

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
%{rlibdir}/%{packname}
