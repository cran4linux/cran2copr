%global __brp_check_rpaths %{nil}
%global packname  tablerDash
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          'Tabler' API for 'Shiny'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-knitr 

%description
'R' interface to the 'Tabler' HTML template. See more here
<https://tabler.io>. 'tablerDash' is a light 'Bootstrap 4' dashboard
template. There are different layouts available such as a one page
dashboard or a multi page template, where the navigation menu is contained
in the navigation bar. A fancy example is available at
<https://dgranjon.shinyapps.io/shinyMons/>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bootstrap-4.0.0
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/tablerDash-0.1.0
%{rlibdir}/%{packname}/INDEX
