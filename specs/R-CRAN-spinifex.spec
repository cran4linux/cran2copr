%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spinifex
%global packver   0.3.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Manual Tours, Manual Control of Dynamic Projections of Numeric Multivariate Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tourr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-Rdimtools 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-tourr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-Rdimtools 
Requires:         R-CRAN-magrittr 

%description
Data visualization tours animates linear projection of multivariate data
as its basis (ie. orientation) changes. The 'spinifex' packages generates
paths for manual tours by manipulating the contribution of a single
variable at a time Cook & Buja (1997)
<doi:10.1080/10618600.1997.10474754>. Other types of tours, such as grand
(random walk) and guided (optimizing some objective function) are
available in the 'tourr' package Wickham et al.
<doi:10.18637/jss.v040.i02>. 'spinifex' builds on 'tourr' and can render
tours with 'gganimate' and 'plotly' graphics, and allows for exporting as
an .html widget and as an .gif, respectively. This work is fully discussed
in Spyrison & Cook (2020) <doi:10.32614/RJ-2020-027>.

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
