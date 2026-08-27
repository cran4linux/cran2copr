%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sportsR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive Collection of Sports and Athletics Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Offers a rich and diverse collection of datasets focused on sports,
athletics, physical performance, and related disciplines. The package
includes professional and amateur sports data covering team sports such as
soccer, basketball, baseball, American football, volleyball, rugby,
cricket, hockey, and handball, as well as individual sports including
tennis, badminton, table tennis, golf, swimming, cycling, athletics,
gymnastics, wrestling, boxing, martial arts, weightlifting, triathlon,
rowing, canoeing, climbing, surfing, skiing, snowboarding, and
motorsports. Datasets cover player and team performance, match statistics,
tournament results, championship standings, Olympic and international
competitions, rankings, player demographics, coaching and training,
biomechanics, sports medicine, injuries, exercise physiology, fitness
assessment, sports nutrition, wearable sensor measurements, talent
identification, and sports analytics. Additional datasets include
historical competitions, referee decisions, fan engagement, economic
indicators, and sports management data obtained from public repositories,
official organizations, research publications, and educational resources.
Designed for sports scientists, coaches, analysts, researchers, educators,
students, and data scientists, this package facilitates exploratory data
analysis, statistical modeling, machine learning, visualization, and
sports analytics research.

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
