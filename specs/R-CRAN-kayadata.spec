%global packname  kayadata
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          2%{?dist}
Summary:          Kaya Identity Data for Nations and Regions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-scales >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.8
BuildRequires:    R-CRAN-tidyr >= 0.8
BuildRequires:    R-CRAN-forcats >= 0.3
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-scales >= 1.0
Requires:         R-CRAN-dplyr >= 0.8
Requires:         R-CRAN-tidyr >= 0.8
Requires:         R-CRAN-forcats >= 0.3

%description
Provides data for Kaya identity variables (population, gross domestic
product, primary energy consumption, and energy-related CO2 emissions) for
the world and for individual nations, and utility functions for looking up
data, plotting trends of Kaya variables, and plotting the fuel mix for a
given country or region. The Kaya identity (Yoichi Kaya and Keiichi
Yokobori, "Environment, Energy, and Economy: Strategies for
Sustainability" (United Nations University Press, 1998) and
<https://en.wikipedia.org/wiki/Kaya_identity>) expresses a nation's or
region's greenhouse gas emissions in terms of its population, per-capita
Gross Domestic Product, the energy intensity of its economy, and the
carbon-intensity of its energy supply.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
