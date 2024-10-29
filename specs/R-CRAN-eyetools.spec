%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eyetools
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyse Eye Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-hdf5r 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-rdist 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-hdf5r 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-rdist 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Enables the automation of actions across the pipeline, including initial
steps of transforming binocular data and gap repair to event-based
processing such as fixations, saccades, and entry/duration in Areas of
Interest (AOIs). It also offers visualisation of eye movement and AOI
entries. These tools take relatively raw (trial, time, x, and y form) data
and can be used to return fixations, saccades, and AOI entries and time
spent in AOIs. As the tools rely on this basic data format, the functions
can work with data from any eye tracking device. Implements fixation and
saccade detection using methods proposed by Salvucci and Goldberg (2000)
<doi:10.1145/355017.355028>.

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
