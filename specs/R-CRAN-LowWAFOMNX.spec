%global __brp_check_rpaths %{nil}
%global packname  LowWAFOMNX
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Low WAFOM Niederreiter-Xing Sequence

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RSQLite >= 2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-RSQLite >= 2.0
Requires:         R-CRAN-Rcpp >= 0.12.9

%description
Implementation of Low Walsh Figure of Merit (WAFOM) sequence based on
Niederreiter-Xing sequence <DOI:10.1007/978-3-642-56046-0_30>.

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
