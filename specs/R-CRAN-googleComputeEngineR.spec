%global __brp_check_rpaths %{nil}
%global packname  googleComputeEngineR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          4%{?dist}%{?buildtag}
Summary:          R Interface with Google Compute Engine

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-future >= 1.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-googleAuthR >= 0.7.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-future >= 1.2.0
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-googleAuthR >= 0.7.0
Requires:         R-CRAN-assertthat 
Requires:         R-utils 

%description
Interact with the 'Google Compute Engine' API in R. Lets you create, start
and stop instances in the 'Google Cloud'.  Support for preconfigured
instances, with templates for common R needs.

%prep
%setup -q -c -n %{packname}
find %{packname}/inst -type f -exec chmod a-x {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cloudconfig
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/dockerfiles
%doc %{rlibdir}/%{packname}/nginx
%doc %{rlibdir}/%{packname}/startupscripts
%{rlibdir}/%{packname}/INDEX
