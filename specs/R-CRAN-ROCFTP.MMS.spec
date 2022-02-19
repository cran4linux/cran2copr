%global __brp_check_rpaths %{nil}
%global packname  ROCFTP.MMS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Perfect Sampling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-vctrs >= 0.3.8
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-vctrs >= 0.3.8

%description
The algorithm provided in this package generates perfect sample for
unimodal or multimodal posteriors. Read Once Coupling From The Past, with
Metropolis-Multishift is used to generate a perfect sample for a given
posterior density based on the two extreme starting paths, minimum and
maximum of the most interest range of the posterior. It uses the monotone
random operation of multishift coupler which allows to sandwich all of the
state space in one point. It means both Markov Chains starting from the
maximum and minimum will be coalesced. The generated sample is independent
from the starting points. It is useful for mixture distributions too. The
output of this function is a real value as an exact draw from the
posterior distribution.

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
