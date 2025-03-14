%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fucom
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Full Consistency Method (FUCOM)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-stats 
Requires:         R-CRAN-nloptr 
Requires:         R-stats 

%description
Full Consistency Method (FUCOM) for multi-criteria decision-making (MCDM),
developed by Dragam Pamucar in 2018 (<doi:10.3390/sym10090393>). The goal
of the method is to determine the weights of criteria such that the
deviation from full consistency is minimized. Users provide a character
vector specifying the ranking of each criterion according to its
significance, starting from the criterion expected to have the highest
weight to the least significant one. Additionally, users provide a numeric
vector specifying the priority values for each criterion. The comparison
is made with respect to the first-ranked (most significant) criterion. The
function returns the optimized weights for each criterion (summing to 1),
the comparative priority (Phi) values, the mathematical transitivity
condition (w) value, and the minimum deviation from full consistency
(DFC).

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
