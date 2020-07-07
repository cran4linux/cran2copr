%global packname  RadData
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Nuclear Decay Data for Dosimetric Calculations - ICRP 107

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch

%description
Nuclear Decay Data for Dosimetric Calculations from the International
Commission on Radiological Protection from ICRP Publication 107. Ann. ICRP
38 (3). Eckerman, Keith and Endo, Akira 2008
<doi:10.1016/j.icrp.2008.10.004>
<http://www.icrp.org/publication.asp?id=ICRP%20Publication%20107>. This is
a database of the physical data needed in calculations of
radionuclide-specific protection and operational quantities. The data is
prescribed by the ICRP, the international authority on radiation dose
standards, for estimating dose from the intake of or exposure to
radionuclides in the workplace and the environment. The database contains
information on the half-lives, decay chains, and yields and energies of
radiations emitted in nuclear transformations of 1252 radionuclides of 97
elements.

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
%doc %{rlibdir}/%{packname}/license.txt
%{rlibdir}/%{packname}/INDEX
