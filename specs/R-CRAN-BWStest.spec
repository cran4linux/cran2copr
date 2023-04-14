%global __brp_check_rpaths %{nil}
%global packname  BWStest
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Baumgartner Weiss Schindler Test of Equal Distributions

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-memoise 

%description
Performs the 'Baumgartner-Weiss-Schindler' two-sample test of equal
probability distributions, <doi:10.2307/2533862>. Also performs similar
rank-based tests for equal probability distributions due to Neuhauser
<doi:10.1080/10485250108832874> and Murakami
<doi:10.1080/00949655.2010.551516>.

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
