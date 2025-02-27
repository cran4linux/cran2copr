%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tectonicr
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing the Orientation of Maximum Horizontal Stress

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat.geom >= 3.2.9
BuildRequires:    R-CRAN-spatstat.explore >= 3.2.7
BuildRequires:    R-CRAN-spatstat.utils >= 3.0.4
BuildRequires:    R-CRAN-spatstat.univar >= 2.0.3
BuildRequires:    R-CRAN-zoo >= 1.8.12
BuildRequires:    R-CRAN-smoothr >= 1.0.1
BuildRequires:    R-CRAN-circular >= 0.5.0
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-spatstat.geom >= 3.2.9
Requires:         R-CRAN-spatstat.explore >= 3.2.7
Requires:         R-CRAN-spatstat.utils >= 3.0.4
Requires:         R-CRAN-spatstat.univar >= 2.0.3
Requires:         R-CRAN-zoo >= 1.8.12
Requires:         R-CRAN-smoothr >= 1.0.1
Requires:         R-CRAN-circular >= 0.5.0
Requires:         R-CRAN-boot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-viridis 

%description
Models the direction of the maximum horizontal stress using relative plate
motion parameters. Statistical algorithms to evaluate the modeling results
compared with the observed data. Provides plots to visualize the results.
Methods described in Stephan et al. (2023)
<doi:10.1038/s41598-023-42433-2> and Wdowinski (1998)
<doi:10.1016/S0079-1946(98)00091-3>.

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
