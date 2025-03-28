%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  valorate
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Velocity and Accuracy of the LOg-RAnk TEst

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-survival 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 

%description
The algorithm implemented in this package was designed to quickly
estimates the distribution of the log-rank especially for heavy unbalanced
groups. VALORATE estimates the null distribution and the p-value of the
log-rank test based on a recent formulation. For a given number of
alterations that define the size of survival groups, the estimation
involves a weighted sum of distributions that are conditional on a
co-occurrence term where mutations and events are both present. The
estimation of conditional distributions is quite fast allowing the
analysis of large datasets in few minutes
<https://bioinformatics.mx/index.php/bioinfo-tools/>.

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
