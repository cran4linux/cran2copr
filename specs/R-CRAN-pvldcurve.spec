%global __brp_check_rpaths %{nil}
%global packname  pvldcurve
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Simplifies the Analysis of Pressure Volume and Leaf Drying Curves

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
Simplifies the manufacturing, analysis and display of pressure volume and
leaf drying curves. From the progression of the curves turgor loss point,
osmotic potential, apoplastic fraction as well as minimum conductance and
stomatal closure can be derived. Methods adapted from Bartlett, Scoffoni,
Sack (2012) <doi:10.1111/j.1461-0248.2012.01751.x> and Sack, Scoffoni,
PrometheusWikiContributors (2011)
<http://prometheuswiki.org/tiki-index.php?page=Minimum+epidermal+conductance+%%28gmin%%2C+a.k.a.+cuticular+conductance%%29>.

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
