%global packname  crunchy
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Shiny Apps on Crunch

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi >= 0.4
BuildRequires:    R-CRAN-crunch 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-httpcache 
BuildRequires:    R-CRAN-miniUI 
Requires:         R-CRAN-rstudioapi >= 0.4
Requires:         R-CRAN-crunch 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-httpcache 
Requires:         R-CRAN-miniUI 

%description
To facilitate building custom dashboards on the Crunch data platform
<https://crunch.io/>, the 'crunchy' package provides tools for working
with 'shiny'. These tools include utilities to manage authentication and
authorization automatically and custom stylesheets to help match the look
and feel of the Crunch web application. The package also includes several
gadgets for use in 'RStudio'.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example_apps
%doc %{rlibdir}/%{packname}/extra.css
%doc %{rlibdir}/%{packname}/extra.js
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
