%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sulcimap
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Mapping Cortical Folding Patterns

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-cowplot 
Requires:         R-grid 
Requires:         R-grDevices 

%description
Visualizes sulcal morphometry data derived from 'BrainVisa'
<https://brainvisa.info/> including width, depth, surface area, and
length. The package enables mapping of statistical group results or
subject-level values onto cortical surface maps, with options to focus on
all sulci or only selected regions of interest. Users can display all four
measures simultaneously or restrict plots to chosen measures, creating
composite, publication-quality brain visualizations in R to support the
analysis and interpretation of sulcal morphology.

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
