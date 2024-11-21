%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prnsamplr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Permanent Random Number Sampling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-stats >= 4.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
Requires:         R-stats >= 4.2
Requires:         R-CRAN-rlang >= 1.1.0

%description
Survey sampling using permanent random numbers (PRN's). A solution to the
problem of unknown overlap between survey samples, which leads to a low
precision in estimates when the survey is repeated or combined with other
surveys. The PRN solution is to supply the U(0, 1) random numbers to the
sampling procedure, instead of having the sampling procedure generate
them. In Lindblom (2014) <doi:10.2478/jos-2014-0047>, and therein cited
papers, it is shown how this is carried out and how it improves the
estimates. This package supports two common fixed-size sampling procedures
(simple random sampling and probability-proportional-to-size sampling) and
includes a function for transforming the PRN's in order to control the
sample overlap.

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
