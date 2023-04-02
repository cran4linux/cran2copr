%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phenology
%global packver   9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Manage a Parametric Function that Describes Phenology and More

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-HelpersMG >= 5.9
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-optimx 
Requires:         R-CRAN-HelpersMG >= 5.9
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-CRAN-optimx 

%description
Functions used to fit and test the phenology of species based on counts.
Based on Girondot, M. (2010) <doi:10.3354/esr00292> for the phenology
function, Girondot, M. (2017) <doi:10.1016/j.ecolind.2017.05.063> for the
convolution of negative binomial, Girondot, M. and Rizzo, A. (2015)
<doi:10.2993/etbi-35-02-337-353.1> for Bayesian estimate, Pfaller JB, ...,
Girondot M (2019) <doi:10.1007/s00227-019-3545-x> for tag-loss estimate,
Hancock J, ..., Girondot M (2019) <doi:10.1016/j.ecolmodel.2019.04.013>
for nesting history, Laloe J-O, ..., Girondot M, Hays GC (2020)
<doi:10.1007/s00227-020-03686-x> for aggregating several seasons.

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
