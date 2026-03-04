%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  r4subprofile
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regulatory Submission Profiles for Clinical Submission Readiness

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-r4subcore 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-r4subcore 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Defines submission profiles per regulatory authority with
authority-specific pillar weights, decision thresholds, indicator
requirements, and risk configuration. Supports the U.S. Food and Drug
Administration (FDA), European Medicines Agency (EMA), Pharmaceuticals and
Medical Devices Agency (PMDA), Health Canada, Therapeutic Goods
Administration (TGA), and Medicines and Healthcare products Regulatory
Agency (MHRA). Integrates with 'r4subscore' and 'r4subrisk' configuration
systems.

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
