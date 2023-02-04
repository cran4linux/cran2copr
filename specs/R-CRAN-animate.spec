%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  animate
%global packver   0.3.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Web-Based Graphics Device for Animated Visualisations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-R.utils 

%description
Implements a web-based graphics device for animated visualisations.
Modelled on the 'base' syntax, it extends the 'base' graphics functions to
support frame-by-frame animation and keyframes animation. The target use
cases are real-time animated visualisations, including agent-based models,
dynamical systems, and animated diagrams. The generated visualisations can
be deployed as GIF images / MP4 videos, as 'Shiny' apps (with
interactivity) or as HTML documents through embedding into R Markdown
documents.

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
