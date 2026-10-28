%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  radiatR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analyse and Visualise Headings and Trajectories on the Unit Disk

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-circular 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 

%description
A complete pipeline for analysing directional data -- headings and
trajectories on the unit disk. Supply a table of angles directly, or
reconstruct headings from movement trajectories imported from tracking
tools ('EthoVision', 'DeepLabCut', 'SLEAP', 'TRex', 'ANY-maze',
'TrackMate', 'idtracker.ai', and others) via a unified dialect-based
loader system, including multi-bodypart pose estimation with
likelihood-weighted centroid. Derives per-trial heading directions using
multiple rules (ring-crossing, distal point, pose body-axis,
velocity-based, and more). Computes circular statistics including mean
direction, resultant length, von Mises and wrapped Cauchy parametric fits,
circular correlation (circular-linear and circular-circular),
circular-linear regression (Fisher and Lee (1992) <doi:10.2307/2532334>),
model selection among orientation models (Fitak and Johnsen (2017)
<doi:10.1242/jeb.167056>), and uniformity and multi-sample hypothesis
tests (Rayleigh, Watson-Williams, Hermans-Rasson (Landler, Ruxton and
Malkemper (2019) <doi:10.1186/s12898-019-0246-8>), and others) with
multiple-comparison correction. Path tortuosity follows Benhamou (2004)
<doi:10.1016/j.jtbi.2004.03.016>. Renders publication-quality 'ggplot2'
radial plots with overlaid rose diagrams, parametric density curves,
non-parametric kernel density estimates, and circular boxplots
(Buttarazzi, Pandolfo and Porzio (2018) <doi:10.1111/biom.12889>).
Includes a browser-based 'shiny' graphical interface requiring no R coding
via launch_app().

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
