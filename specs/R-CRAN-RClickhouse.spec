%global __brp_check_rpaths %{nil}
%global packname  RClickhouse
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          3%{?dist}%{?buildtag}
Summary:          A 'DBI' Interface to the 'Yandex Clickhouse' Database ProvidingBasic 'dplyr' Support

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-methods >= 3.3.2
BuildRequires:    R-CRAN-dbplyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-DBI >= 0.6.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-bit64 
Requires:         R-methods >= 3.3.2
Requires:         R-CRAN-dbplyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-DBI >= 0.6.0
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-bit64 

%description
'Yandex Clickhouse' (<https://clickhouse.yandex/>) is a high-performance
relational column-store database to enable big data exploration and
'analytics' scaling to petabytes of data. Methods are provided that enable
working with 'Yandex Clickhouse' databases via 'DBI' methods and using
'dplyr'/'dbplyr' idioms.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
