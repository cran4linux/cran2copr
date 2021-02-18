%global packname  NAEPirtparams
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          IRT Parameters for the National Assessment of Education Progress

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
This data package contains the Item Response Theory (IRT) parameters for
the National Center for Education Statistics (NCES) items used on the
National Assessment of Education Progress (NAEP) from 1990 to 2015. The
values in these tables are used along with NAEP data to turn student item
responses into scores and include information about item difficulty,
discrimination, and guessing parameter for 3 parameter logit (3PL) items.
Parameters for Generalized Partial Credit Model (GPCM) items are also
included. The adjustments table contains the information regarding the
treatment of items (e.g., deletion of an item or a collapsing of response
categories), when these items did not appear to fit the item response
models used to describe the NAEP data. Transformation constants change the
score estimates that are obtained from the IRT scaling program to the NAEP
reporting metric. Values from the years 2000 - 2013 were taken from the
NCES website <https://nces.ed.gov/nationsreportcard/> and values from 1990
- 1998 and 2015 were extracted from their NAEP data files. All subtest
names were reduced and homogenized to one word (e.g. "Reading to gain
information" became "information"). The various subtest names for
univariate transformation constants were all homogenized to "univariate".

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
