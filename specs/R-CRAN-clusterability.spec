%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clusterability
%global packver   0.2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Performs Tests for Cluster Tendency of a Data Set

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-sparsepca 
BuildRequires:    R-CRAN-elasticnet 
Requires:         R-CRAN-diptest 
Requires:         R-splines 
Requires:         R-CRAN-sparsepca 
Requires:         R-CRAN-elasticnet 

%description
Test for cluster tendency (clusterability) of a data set. The methods
implemented - reducing the data set to a single dimension using principal
component analysis or computing pairwise distances, and performing a
multimodality test like the Dip Test or Silverman's Critical Bandwidth
Test - are described in Adolfsson, Ackerman, and Brownstein (2019)
<doi:10.1016/j.patcog.2018.10.026>. Such methods can inform whether
clustering algorithms are appropriate for a data set.

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
