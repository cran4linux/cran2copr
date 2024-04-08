%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggcorset
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Corset Plot

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gghalves 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gghalves 

%description
Corset plots are a visualization technique used strictly to visualize
repeat measures at 2 time points (such as pre- and post- data). The
distribution of measurements are visualized at each time point, whilst the
trajectories of individual change are visualized by connecting the pre-
and post- values linearly. These lines can be coloured to represent the
magnitude of change, or other user-defined value. This method of
visualization is ideal for showing the heterogeneity of data, including
differences by sub-groups. The package relies on 'ggplot2' allowing for
easy integration so that users can customize their visualizations as
required. Users can create corset plots using data in either wide or long
format using the functions gg_corset() or gg_corset_elongated(),
respectively.

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
