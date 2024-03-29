%global __brp_check_rpaths %{nil}
%global packname  mod2rm
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Moderation Analysis for Two-Instance Repeated Measures Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 

%description
Multiple moderation analysis for two-instance repeated measures designs,
with up to three simultaneous moderators (dichotomous and/or continuous)
with additive or multiplicative relationship. Includes analyses of simple
slopes and conditional effects at (automatically determined or manually
set) values of the moderator(s), as well as an implementation of the
Johnson-Neyman procedure for determining regions of significance in single
moderator models. Based on Montoya, A. K. (2018) "Moderation analysis in
two-instance repeated measures designs: Probing methods and multiple
moderator models" <doi:10.3758/s13428-018-1088-6> .

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
