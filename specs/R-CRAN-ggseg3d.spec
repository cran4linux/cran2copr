%global __brp_check_rpaths %{nil}
%global packname  ggseg3d
%global packver   1.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tri-Surface Mesh Plots for Brain Atlases

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Mainly contains a plotting function ggseg3d(), and data of two standard
brain atlases (Desikan-Killiany and aseg). By far, the largest bit of the
package is the data for each of the atlases. The functions and data enable
users to plot tri-surface mesh plots of brain atlases, and customise these
by projecting colours onto the brain segments based on values in their own
data sets. Functions are wrappers for 'plotly'. Mowinckel & Vidal-Piñeiro
(2020) <doi:10.1177/2515245920928009>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
