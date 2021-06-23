%global __brp_check_rpaths %{nil}
%global packname  remap
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regional Spatial Modeling with Continuous Borders

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-graphics >= 3.6.0
BuildRequires:    R-methods >= 3.6.0
BuildRequires:    R-parallel >= 3.6.0
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-utils >= 3.6.0
BuildRequires:    R-CRAN-sf >= 0.9.6
BuildRequires:    R-CRAN-units >= 0.6.7
Requires:         R-graphics >= 3.6.0
Requires:         R-methods >= 3.6.0
Requires:         R-parallel >= 3.6.0
Requires:         R-stats >= 3.6.0
Requires:         R-utils >= 3.6.0
Requires:         R-CRAN-sf >= 0.9.6
Requires:         R-CRAN-units >= 0.6.7

%description
Automatically creates separate regression models for different spatial
regions. The prediction surface is smoothed using a regional border
smoothing method. If regional models are continuous, the resulting
prediction surface is continuous across the spatial dimensions, even at
region borders. Methodology is described in Wagstaff (2021)
<https://digitalcommons.usu.edu/etd/8065/>.

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
