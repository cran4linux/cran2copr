%global __brp_check_rpaths %{nil}
%global packname  garray
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Generalized Array Arithmetic for Ragged Arrays with NamedMargins

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch

%description
Organize a so-called ragged array as generalized arrays, which is simply
an array with sub-dimensions denoting the subdivision of dimensions
(grouping of members within dimensions). By the margins (names of
dimensions and sub-dimensions) in generalized arrays, operators and
utility functions provided in this package automatically match the
margins, doing map-reduce style parallel computation along margins.
Generalized arrays are also cooperative to R's native functions that work
on simple arrays.

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
