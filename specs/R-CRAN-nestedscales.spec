%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nestedscales
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nested Scales and Multi-Dimensional Indexes for Modeling

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-S7 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides multi-level discrete representations of data dimensions for
modeling, data processing and visualization. A nested scale records its
finest units (atoms) and their membership in coarser levels (frames),
including nested, cross-cutting and partially covered relationships.
Recasts tabular data between levels using explicit, direction-aware rules
for sums, means, standard deviations, copying and within-parent shares.
Also supports labeling, subsetting, combining scales into
multi-dimensional indexes, clustering units and storing data with its
scale metadata. Members may carry attributes (a calorific value, an
emission factor) and aliases, resolved along the hierarchy and applied row
by row, and a scale is exchanged as a language-neutral definition file: a
'JSON' header with inline, 'Arrow' or 'CSV' tables ('YAML' accepted), with
a catalogue of the definitions installed packages ship. Forms the
dimension-agnostic core of 'timescales'
<https://github.com/optimal2050/timescales> (calendars) and 'geoscales'
<https://github.com/optimal2050/geoscales> (regions), designed for
optimization and simulation models.

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
