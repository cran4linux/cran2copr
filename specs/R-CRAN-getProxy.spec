%global __brp_check_rpaths %{nil}
%global packname  getProxy
%global packver   1.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12
Release:          3%{?dist}%{?buildtag}
Summary:          Get Free Proxy IP and Port

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr 

%description
Allows get address and port of the free proxy server, from one of two
services <http://gimmeproxy.com/> or <https://getproxylist.com/>. And it's
easy to redirect your Internet connection through a proxy server.

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
%{rlibdir}/%{packname}/INDEX
