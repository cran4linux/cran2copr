%global __brp_check_rpaths %{nil}
%global packname  RadioSonde
%global packver   4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Plotting Skew-T Diagrams and Wind Profiles

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-fields 

%description
A collection of programs for plotting SKEW-T,log p diagrams and wind
profiles for data collected by radiosondes (the typical weather
balloon-borne instrument). The format of this plot with companion lines to
assess atmospheric stability are both standard in meteorology and
difficult to create from basic graphics functions. Hence this package. One
novel feature is being able add several profiles to the same plot for
comparison. Use "help(ExampleSonde)" for an explanation of the variables
needed and how they should be named in a data frame. See
<https://github.com/dnychka/Radiosonde> for the package home page.

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
