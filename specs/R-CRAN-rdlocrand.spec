%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdlocrand
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Local Randomization Methods for RD Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-sandwich 

%description
The regression discontinuity (RD) design is a popular quasi-experimental
design for causal inference and policy evaluation. Under the local
randomization approach, RD designs can be interpreted as randomized
experiments inside a window around the cutoff. This package provides tools
to perform randomization inference for RD designs under local
randomization: rdrandinf() to perform hypothesis testing using
randomization inference, rdwinselect() to select a window around the
cutoff in which randomization is likely to hold, rdsensitivity() to assess
the sensitivity of the results to different window lengths and null
hypotheses and rdrbounds() to construct Rosenbaum bounds for sensitivity
to unobserved confounders. See Cattaneo, Titiunik and Vazquez-Bare (2016)
<https://rdpackages.github.io/references/Cattaneo-Titiunik-VazquezBare_2016_Stata.pdf>
for further methodological details.

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
