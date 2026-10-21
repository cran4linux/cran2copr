%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DistributionalDDA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Distributional Data Analysis in Bayes Spaces

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-compositions 
Requires:         R-splines 
Requires:         R-CRAN-fda 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-grDevices 

%description
Statistical analysis of data sets whose observations are whole probability
distributions, using Bayes space calculus. Distributions (provided as
samples, histograms or density functions) are treated as elements of a
Hilbert space, so that operations such as mean, variance, distance,
principal component analysis and clustering carry over to densities.
Reference measures defining the geometry of the space can be chosen and
combined. The methodology was first published with peer review by van den
Boogaart, Egozcue and Pawlowsky-Glahn (2014) <doi:10.1111/anzs.12074>.

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
