%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bipl5
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Construct Reactive Calibrated Axes Biplots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.2
BuildRequires:    R-CRAN-htmlwidgets >= 1.6.2
BuildRequires:    R-CRAN-crayon >= 1.5.2
BuildRequires:    R-CRAN-knitr >= 1.43
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-methods 
Requires:         R-CRAN-plotly >= 4.10.2
Requires:         R-CRAN-htmlwidgets >= 1.6.2
Requires:         R-CRAN-crayon >= 1.5.2
Requires:         R-CRAN-knitr >= 1.43
Requires:         R-CRAN-cluster 
Requires:         R-methods 

%description
A modern view on the principal component analysis biplot with calibrated
axes. Create principal component analysis biplots rendered in HTML with
significant reactivity embedded within the plot. Furthermore, the
traditional biplot view is enhanced by translated axes with inter-class
kernel densities superimposed. For more information on biplots, see Gower,
J.C., Lubbe, S. and le Roux, N.J. (2011, ISBN: 978-0-470-01255-0).

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
