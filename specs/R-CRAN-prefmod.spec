%global __brp_check_rpaths %{nil}
%global packname  prefmod
%global packver   0.8-35
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.35
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities to Fit Paired Comparison Models for Preferences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-gnm >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-gnm >= 1.0.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-colorspace 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 

%description
Generates design matrix for analysing real paired comparisons and derived
paired comparison data (Likert type items/ratings or rankings) using a
loglinear approach. Fits loglinear Bradley-Terry model (LLBT) exploiting
an eliminate feature. Computes pattern models for paired comparisons,
rankings, and ratings. Some treatment of missing values (MCAR and MNAR).
Fits latent class (mixture) models for paired comparison, rating and
ranking patterns using a non-parametric ML approach.

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
