%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cardiovagal
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Equivalence Testing for Cross-Species Cardiovagal Homeostasis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-equivalence 
BuildRequires:    R-stats 
Requires:         R-CRAN-equivalence 
Requires:         R-stats 

%description
Automates cardiovagal state regulation mapping by translating raw, noisy
mammalian heart rate variability intervals into a standardized linear
index using fixed physiological anchors. The package incorporates natural
log data compression and utilizes two-one-sided tests (TOST) and Bayesian
Region of Practical Equivalence (ROPE) thresholds to mathematically verify
cross-species homeostatic synchronization. Methodologies for equivalence
testing and regional practical equivalence bounds follow Lakens (2017)
<doi:10.1177/1948550617697177> and Kruschke (2018)
<doi:10.1177/2515245918771304>.

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
