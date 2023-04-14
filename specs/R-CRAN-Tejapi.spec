%global __brp_check_rpaths %{nil}
%global packname  Tejapi
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          API Wrapper for Taiwan Economic Journal Data Service

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9.14
BuildRequires:    R-CRAN-httr >= 0.6.1
Requires:         R-CRAN-jsonlite >= 0.9.14
Requires:         R-CRAN-httr >= 0.6.1

%description
Functions for interacting directly with the Taiwan Economic Journal API to
offer data in R. For more information go to <https://api.tej.com.tw>.

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
