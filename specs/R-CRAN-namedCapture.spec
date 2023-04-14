%global __brp_check_rpaths %{nil}
%global packname  namedCapture
%global packver   2020.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Named Capture Regular Expressions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch

%description
User-friendly wrappers for named capture regular expressions. Introduction
and comparison in research paper by Hocking (2019), R Journal.
<doi:10.32614/RJ-2019-050> RE2 engine ('re2r' package)
<https://github.com/qinwf/re2r> was removed from CRAN in Mar 2020 so must
be installed from github.

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
