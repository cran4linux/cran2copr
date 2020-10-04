%global packname  vaersNDvax
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Non-Domestic Vaccine Adverse Event Reporting System (VAERS)Vaccine Data for Present

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch

%description
Non-Domestic VAERS vaccine data for 01/01/2016 - 06/14/2016. If you want
to explore the full VAERS data for 1990 - Present (data, symptoms, and
vaccines), then check out the 'vaersND' package from the URL below. The
URL and BugReports below correspond to the 'vaersND' package, of which
'vaersNDvax' is a small subset (2016 only). 'vaersND' is not hosted on
CRAN due to the large size of the data set. To install the Suggested
'vaers' and 'vaersND' packages, use the following R code:
'devtools::install_git("https://gitlab.com/iembry/vaers.git",
build_vignettes = TRUE)' and
'devtools::install_git("https://gitlab.com/iembry/vaersND.git",
build_vignettes = TRUE)'. "VAERS is a national vaccine safety surveillance
program co-sponsored by the US Centers for Disease Control and Prevention
(CDC) and the US Food and Drug Administration (FDA). VAERS is a
post-marketing safety surveillance program, collecting information about
adverse events (possible side effects) that occur after the administration
of vaccines licensed for use in the United States." For more information
about the data, visit <https://vaers.hhs.gov/index>. For information about
vaccination/immunization hazards, visit
<http://www.questionuniverse.com/rethink.html/#vaccine>.

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
%doc %{rlibdir}/%{packname}/DISCLAIMER
%{rlibdir}/%{packname}/INDEX
