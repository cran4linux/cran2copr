%global packname  translateR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Bindings for the Google and Microsoft Translation APIs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-textcat 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-textcat 
Requires:         R-parallel 
Requires:         R-CRAN-httr 

%description
translateR provides easy access to the Google and Microsoft APIs. The
package is easy to use with the related R package "stm" for the estimation
of multilingual topic models.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
