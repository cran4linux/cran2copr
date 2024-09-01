%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baRulho
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Quantifying (Animal) Sound Degradation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-warbleR >= 1.1.32
BuildRequires:    R-CRAN-ohun >= 1.0.2
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-fftw 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-Sim.DiffProc 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-warbleR >= 1.1.32
Requires:         R-CRAN-ohun >= 1.0.2
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-fftw 
Requires:         R-methods 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-Sim.DiffProc 
Requires:         R-CRAN-png 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 

%description
Intended to facilitate acoustic analysis of (animal) sound transmission
experiments, which typically aim to quantify changes in signal structure
when transmitted in a given habitat by broadcasting and re-recording
animal sounds at increasing distances. The package offers a workflow with
functions to prepare the data set for analysis as well as to calculate and
visualize several degradation metrics, including blur ratio,
signal-to-noise ratio, excess attenuation and envelope correlation among
others (Dabelsteen et al 1993 <doi:10.1121/1.406682>).

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
