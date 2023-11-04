%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  see
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model Visualisation Toolbox for 'easystats' and 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-datawizard >= 0.9.0
BuildRequires:    R-CRAN-effectsize >= 0.8.6
BuildRequires:    R-CRAN-modelbased >= 0.8.6
BuildRequires:    R-CRAN-correlation >= 0.8.4
BuildRequires:    R-CRAN-parameters >= 0.21.3
BuildRequires:    R-CRAN-insight >= 0.19.6
BuildRequires:    R-CRAN-bayestestR >= 0.13.1
BuildRequires:    R-CRAN-performance >= 0.10.8
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-datawizard >= 0.9.0
Requires:         R-CRAN-effectsize >= 0.8.6
Requires:         R-CRAN-modelbased >= 0.8.6
Requires:         R-CRAN-correlation >= 0.8.4
Requires:         R-CRAN-parameters >= 0.21.3
Requires:         R-CRAN-insight >= 0.19.6
Requires:         R-CRAN-bayestestR >= 0.13.1
Requires:         R-CRAN-performance >= 0.10.8
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Provides plotting utilities supporting packages in the 'easystats'
ecosystem (<https://github.com/easystats/easystats>) and some extra
themes, geoms, and scales for 'ggplot2'. Color scales are based on
<https://materialui.co/colors>. References: Lüdecke et al. (2021)
<doi:10.21105/joss.03393>.

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
