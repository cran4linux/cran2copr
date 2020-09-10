%global packname  radsafer
%global packver   2.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Radiation Safety

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RadData 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-ggthemes 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readr 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-RadData 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-ggthemes 

%description
Provides functions for radiation safety, also known as "radiation
protection" and "radiological control". The science of radiation
protection is called "health physics" and its engineering functions are
called "radiological engineering". Functions in this package cover many of
the computations needed by radiation safety professionals. Examples
include: obtaining updated calibration and source check values for
radiation monitors to account for radioactive decay in a reference source,
simulating instrument readings to better understand measurement
uncertainty, correcting instrument readings for geometry and ambient
atmospheric conditions. Many of these functions are described in Johnson
and Kirby (2011, ISBN-13: 978-1609134198). Utilities are also included for
developing inputs and processing outputs with radiation transport codes,
such as MCNP, a general-purpose Monte Carlo N-Particle code that can be
used for neutron, photon, electron, or coupled neutron/photon/electron
transport (Werner et. al. (2018) <doi:10.2172/1419730>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
