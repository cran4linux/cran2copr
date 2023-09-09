%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mousetRajectory
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mouse Trajectory Analyses for Behavioural Scientists

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-signal >= 0.7
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-signal >= 0.7
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-utils 

%description
Helping psychologists and other behavioural scientists to analyze mouse
movement (and other 2-D trajectory) data. Bundles together several
functions that compute spatial measures (e.g., maximum absolute deviation,
area under the curve, sample entropy) or provide a shorthand for
procedures that are frequently used (e.g., time normalization, linear
interpolation, extracting initiation and movement times). For more
information on these dependent measures, see Wirth et al. (2020)
<doi:10.3758/s13428-020-01409-0>.

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
