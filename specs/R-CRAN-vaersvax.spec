%global packname  vaersvax
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          US Vaccine Adverse Event Reporting System (VAERS) Vaccine Datafor Present

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch

%description
US VAERS vaccine data for 01/01/2018 - 06/14/2018. If you want to explore
the full VAERS data for 1990 - Present (data, symptoms, and vaccines),
then check out the 'vaers' package from the URL below. The URL and
BugReports below correspond to the 'vaers' package, of which 'vaersvax' is
a small subset (2018 only). 'vaers' is not hosted on CRAN due to the large
size of the data set. To install the Suggested 'vaers' and 'vaersND'
packages, use the following R code:
'devtools::install_git("<https://gitlab.com/iembry/vaers.git>",
build_vignettes = TRUE)' and
'devtools::install_git("<https://gitlab.com/iembry/vaersND.git>",
build_vignettes = TRUE)'. "The Vaccine Adverse Event Reporting System
(VAERS) is a national early warning system to detect possible safety
problems in U.S.-licensed vaccines. VAERS is co-managed by the Centers for
Disease Control and Prevention (CDC) and the U.S. Food and Drug
Administration (FDA)." For more information about the data, visit
<https://vaers.hhs.gov/>. For information about vaccination/immunization
hazards, visit <http://www.questionuniverse.com/rethink.html#vaccine>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
