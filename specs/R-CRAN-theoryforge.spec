%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  theoryforge
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Systematic Theory Development

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.3.8
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-yaml >= 2.3.8
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides a reproducible workflow for building, developing and testing
scientific theories represented as versioned, machine-checkable objects.
Functions read and validate theory objects, score them against a versioned
rigour checklist, screen constructs for redundancy, derive the conditional
independencies a causal theory implies, appraise amendments as
progressive, degenerating or neutral, write preregistration and audit
documents, compile 'lavaan' model syntax, simulate the construct network,
map a theory onto the themes of a literature corpus and write diagram
intermediate representations. A 'Python' package of the same name offers
the same functions. Both follow one specification, so they produce the
same verdicts and the same diagram intermediate representations.

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
