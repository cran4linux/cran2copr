%global packname  ProfoundData
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Downloading and Exploring Data from the PROFOUND Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.3.2
BuildRequires:    R-CRAN-RNetCDF >= 1.9.1
BuildRequires:    R-CRAN-zoo >= 1.7.14
BuildRequires:    R-CRAN-RSQLite >= 1.1.2
BuildRequires:    R-CRAN-DBI >= 0.5.1
BuildRequires:    R-CRAN-sqldf >= 0.4.10
BuildRequires:    R-CRAN-settings >= 0.2.4
BuildRequires:    R-tcltk 
Requires:         R-methods >= 3.3.2
Requires:         R-CRAN-RNetCDF >= 1.9.1
Requires:         R-CRAN-zoo >= 1.7.14
Requires:         R-CRAN-RSQLite >= 1.1.2
Requires:         R-CRAN-DBI >= 0.5.1
Requires:         R-CRAN-sqldf >= 0.4.10
Requires:         R-CRAN-settings >= 0.2.4
Requires:         R-tcltk 

%description
Provides an R interface for the PROFOUND database
<doi:10.5880/PIK.2019.008>. The PROFOUND database contains a wide range of
data to evaluate vegetation models and simulate climate impacts at the
forest stand scale. It includes 9 forest sites across Europe, and provides
for them a site description as well as soil, climate, CO2, Nitrogen
deposition, tree-level, forest stand-level and remote sensing data.
Moreover, for a subset of 5 sites, also time series of carbon fluxes,
energy balances and soil water are available.

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
