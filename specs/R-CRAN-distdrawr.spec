%global packname  distdrawr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Download Occurrence Data of Vascular Plants in Germany from theFLORKART Database

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch

%description
Download data from the FlorKart database of the floristic field mapping in
Germany in a convenient way. The database incorporates distribution data
for plants in Germany on the basis of quadrants on a topographical map
with a resolution of 1 : 25000 (TK 25). The data is owned and provided by
the German Federal Agency for Nature Conservation (BfN) and the Network
Phytodiversity in Germany (NetPhyD). For further information please visit
<http://www.floraweb.de/pflanzenarten/hintergrundtexte_florkart_organisation.html>.
The author of this package is in no way associated with the BfN or
NetPhyD.

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
%{rlibdir}/%{packname}/INDEX
