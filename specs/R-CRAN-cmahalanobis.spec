%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cmahalanobis
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate the Mahalanobis Distance for a Given List of Data Frames with Factors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
It provides a function that calculates the Mahalanobis distance between
each pair of species in a list of data frames. Each data frame contains
the observations of a species with some factors. Mahalanobis distance is a
measure of dissimilarity between two vectors of multivariate random
variables, based on the covariance matrix. This distance is useful for
statistical matching or fusion of data, that is the integration of two
data sources that refer to the same target population and that share some
variables. - "Fisher, R.A. (1922) On the mathematical foundations of
theoretical statistics. <doi:10.1098/rsta.1922.0009>". - "Mahalanobis,
P.C. (1936) On the generalized distance in statistics.
<doi:10.1007/s13171-019-00164-5>".

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
