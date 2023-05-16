%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weatherindices
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Weather Indices

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Weather indices represent the overall weekly effect of a weather variable
on crop yield throughout the cropping season. This package contains
functions that can convert the weekly weather data into yearly weighted
Weather indices with weights being the correlation coefficient between
weekly weather data over the years and crop yield over the years. This can
be done for an individual weather variable and for two weather variables
at a time as the interaction effect. This method was first devised by
Jain, RC, Agrawal R, and Jha, MP (1980), "Effect of climatic variables on
rice yield and its forecast",MAUSAM, 31(4), 591–596,
<doi:10.54302/mausam.v31i4.3477>. Later, the method have been used by
various researchers and the latest can found in Gupta, AK, Sarkar, KA,
Dhakre, DS, & Bhattacharya, D (2022), "Weather Based Potato Yield
Modelling using Statistical and Machine Learning Technique",Environment
and Ecology, 40(3B),
1444–1449,<https://www.environmentandecology.com/volume-40-2022>.

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
