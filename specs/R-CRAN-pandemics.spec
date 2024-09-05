%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pandemics
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Monitoring a Developing Pandemic with Available Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Full dynamic system to describe and forecast the spread and the severity
of a developing pandemic, based on available data. These data are number
of infections, hospitalizations, deaths and recoveries notified each day.
The system consists of three transitions, infection-infection,
infection-hospital and hospital-death/recovery. The intensities of these
transitions are dynamic and estimated using non-parametric local linear
estimators. The package can be used to provide forecasts and survival
indicators such as the median time spent in hospital and the probability
that a patient who has been in hospital for a number of days can leave it
alive. Methods are described in Gámiz, Mammen, Martínez-Miranda, and
Nielsen (2024) <doi:10.48550/arXiv.2308.09918> and
<doi:10.48550/arXiv.2308.09919>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
