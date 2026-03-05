%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  alsi
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Aggregated Latent Space Index for Binary, Ordinal, and Continuous Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-homals 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-homals 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Provides three stability-validated pipelines for computing an Aggregated
Latent Space Index (ALSI): a binary MCA pipeline (alsi_workflow()), an
ordinal pipeline using homals alternating least squares optimal scaling
(alsi_workflow_ordinal()), and a continuous ipsatized SVD pipeline
(calsi_workflow()).  All three pipelines share a common bootstrap
dual-criterion stability framework (principal angles and Tucker congruence
phi) for determining the number of dimensions to retain before index
construction.  The package is designed to complement Segmented Profile
Analysis (SEPA) and is intended for psychometric scale construction and
dimensional reduction in survey and clinical research.

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
