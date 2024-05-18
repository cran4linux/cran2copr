%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mgwrhw
%global packver   1.1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Displays GWR (Geographically Weighted Regression) and Mixed GWR Output and Map

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-spgwr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-spgwr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
Display processing results using the GWR (Geographically Weighted
Regression) method, display maps, and show the results of the Mixed GWR
(Mixed Geographically Weighted Regression) model which automatically
selects global variables based on variability between regions. This
function refers to Yasin, & Purhadi. (2012). "Mixed Geographically
Weighted Regression Model (Case Study the Percentage of Poor Households in
Mojokerto 2008)". European Journal of Scientific Research, 188-196.
<https://www.researchgate.net/profile/Hasbi-Yasin-2/publication/289689583_Mixed_geographically_weighted_regression_model_case_study_The_percentage_of_poor_households_in_Mojokerto_2008/links/58e46aa40f7e9bbe9c94d641/Mixed-geographically-weighted-regression-model-case-study-The-percentage-of-poor-households-in-Mojokerto-2008.pdf>.

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
