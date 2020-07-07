%global packname  helminthR
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}
Summary:          Access London Natural History Museum Host-Helminth RecordDatabase

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-utils 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 

%description
Access to large host-parasite data is often hampered by the availability
of data and difficulty in obtaining it in a programmatic way to encourage
analyses. 'helminthR' provides a programmatic interface to the London
Natural History Museum's host-parasite database, one of the largest
host-parasite databases existing currently
<http://www.nhm.ac.uk/research-curation/scientific-resources/taxonomy-systematics/host-parasites/>.
The package allows the user to query by host species, parasite species,
and geographic location.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
