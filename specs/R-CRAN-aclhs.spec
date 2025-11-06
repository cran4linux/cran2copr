%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aclhs
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Autocorrelated Conditioned Latin Hypercube Sampling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-graphics >= 4.5.1
BuildRequires:    R-stats >= 4.5.1
BuildRequires:    R-utils >= 4.5.1
BuildRequires:    R-CRAN-DEoptim >= 2.2.8
BuildRequires:    R-CRAN-geoR >= 1.9.6
Requires:         R-graphics >= 4.5.1
Requires:         R-stats >= 4.5.1
Requires:         R-utils >= 4.5.1
Requires:         R-CRAN-DEoptim >= 2.2.8
Requires:         R-CRAN-geoR >= 1.9.6

%description
Implementation of the autocorrelated conditioned Latin Hypercube Sampling
(acLHS) algorithm for 1D (time-series) and 2D (spatial) data. The acLHS
algorithm is an extension of the conditioned Latin Hypercube Sampling
(cLHS) algorithm that allows sampled data to have similar correlative and
statistical features of the original data. Only a properly formatted
dataframe needs to be provided to yield subsample indices from the primary
function. For more details about the cLHS algorithm, see Minasny and
McBratney (2006), <doi:10.1016/j.cageo.2005.12.009>. For acLHS, see Le and
Vargas (2024) <doi:10.1016/j.cageo.2024.105539>.

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
