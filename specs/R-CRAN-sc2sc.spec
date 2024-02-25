%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sc2sc
%global packver   0.0.1-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.12
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Transfer of Statistics among Spanish Census Sections

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Transfers/imputes statistics among Spanish spatial polygons (census
sections or postal code areas) from different moments in time (2001-2023)
without need of spatial files, just linking statistics to the ID codes of
the spatial units. The data available in the census sections of a
partition/division (cartography) into force in a moment of time is
transferred to the census sections of another partition/division employing
the geometric approach (also known as areal weighting or polygon overlay).
References: Goerlich (2022) <doi:10.12842/WPIVIE_0322>. Pavía and
Cantarino (2017a, b) <doi:10.1111/gean.12112>,
<doi:10.1016/j.apgeog.2017.06.021>. Acknowledgements: The authors wish to
thank Consellería de Educación, Universidades y Empleo, Generalitat
Valenciana (grant AICO/2021/257) and Ministerio de Economía e Innovación
(grant PID2021-128228NB-I00) for supporting this research.

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
