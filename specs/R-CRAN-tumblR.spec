%global packname  tumblR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Access to Tumblr v2 API

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl >= 1.95.4.3
BuildRequires:    R-CRAN-RJSONIO >= 1.3.0
BuildRequires:    R-CRAN-stringr >= 0.6.2
BuildRequires:    R-CRAN-httr >= 0.4
Requires:         R-CRAN-RCurl >= 1.95.4.3
Requires:         R-CRAN-RJSONIO >= 1.3.0
Requires:         R-CRAN-stringr >= 0.6.2
Requires:         R-CRAN-httr >= 0.4

%description
Provides an R-interface to the Tumblr web API (see Tumblr v2 API on
https://www.tumblr.com/docs/en/api/v2). Tumblr is a microblogging platform
and social networking website (https://www.tumblr.com).

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
