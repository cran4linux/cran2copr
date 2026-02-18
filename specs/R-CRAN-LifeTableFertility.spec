%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LifeTableFertility
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' Application for Life Table and Fertility Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a 'shiny' application to construct age-specific life tables and
fertility schedules from individual female daily egg records. The
application computes age-specific survival and fertility functions and
estimates key demographic parameters including the net reproductive rate,
mean generation time, intrinsic rate of increase, finite rate of increase
and doubling time. Optional confidence intervals can be obtained using
percentile bootstrap or delete-1 jackknife resampling at the female level.
Methods and definitions follow Stevens (2009)
<doi:10.1007/978-0-387-89882-7> and Rossini et al. (2024)
<doi:10.1371/journal.pone.0299598>.

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
