%global __brp_check_rpaths %{nil}
%global packname  nosoi
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          A Forward Agent-Based Transmission Chain Simulator

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.5.2
BuildRequires:    R-methods >= 3.5.2
BuildRequires:    R-CRAN-raster >= 2.8.19
BuildRequires:    R-CRAN-data.table >= 1.12.0
Requires:         R-stats >= 3.5.2
Requires:         R-methods >= 3.5.2
Requires:         R-CRAN-raster >= 2.8.19
Requires:         R-CRAN-data.table >= 1.12.0

%description
The aim of 'nosoi' (pronounced no.si) is to provide a flexible agent-based
stochastic transmission chain/epidemic simulator (Lequime et al. bioRxiv
2020.03.03.973107). It is named after the daimones of plague, sickness and
disease that escaped Pandora's jar in the Greek mythology. 'nosoi' is able
to take into account the influence of multiple variable on the
transmission process (e.g. dual-host systems (such as arboviruses),
within-host viral dynamics, transportation, population structure), alone
or taken together, to create complex but relatively intuitive
epidemiological simulations.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
