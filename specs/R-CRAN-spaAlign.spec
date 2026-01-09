%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spaAlign
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Stratigraphic Plug Alignment for Integrating Plug-Based and XRF Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements the Stratigraphic Plug Alignment (SPA) procedure for
integrating sparsely sampled plug-based measurements (e.g., total organic
carbon, porosity, mineralogy) with high-resolution X-ray fluorescence
(XRF) geochemical data. SPA uses linear interpolation via the base
approx() function with constrained extrapolation (rule = 1) to preserve
stratigraphic order and avoid estimation beyond observed depths. The
method aligns all datasets to a common depth grid, enabling
high-resolution multivariate analysis and stratigraphic interpretation of
core-based datasets such as those from the Utica and Point Pleasant
formations. See R Core Team (2025)
<https://stat.ethz.ch/R-manual/R-devel/library/stats/html/stats-package.html>
and Omodolor (2025)
<http://rave.ohiolink.edu/etdc/view?acc_num=case175262671767524> for
methodological background and geological context.

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
