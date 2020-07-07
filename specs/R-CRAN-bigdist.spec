%global packname  bigdist
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}
Summary:          Store Distance Matrices on Disk

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bigstatsr >= 0.9.1
BuildRequires:    R-CRAN-proxy >= 0.4.21
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-furrr >= 0.1.0
BuildRequires:    R-utils 
Requires:         R-CRAN-bigstatsr >= 0.9.1
Requires:         R-CRAN-proxy >= 0.4.21
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-furrr >= 0.1.0
Requires:         R-utils 

%description
Provides utilities to compute, store and access distance matrices on disk
as file-backed matrices provided by the 'bigstatsr' package. File-backed
distance matrices are stored as a symmetric matrix to facilitate
out-of-memory operations on file-backed matrix while the in-memory 'dist'
object stores only the lower diagonal elements. 'disto' provides an
unified interface to work with in-memory and disk-based distance matrices.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
