%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  panelPomp
%global packver   1.7.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inference for Panel Partially Observed Markov Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-pomp >= 4.5
BuildRequires:    R-methods 
Requires:         R-CRAN-pomp >= 4.5
Requires:         R-methods 

%description
Data analysis based on panel partially-observed Markov process (PanelPOMP)
models. To implement such models, simulate them and fit them to panel
data, 'panelPomp' extends some of the facilities provided for time series
data by the 'pomp' package. Implemented methods include filtering (panel
particle filtering) and maximum likelihood estimation (Panel Iterated
Filtering) as proposed in Breto, Ionides and King (2020) "Panel Data
Analysis via Mechanistic Models" <doi:10.1080/01621459.2019.1604367>.

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
