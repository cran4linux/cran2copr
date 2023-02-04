%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smallsets
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Smallset Timeline Builder

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-reticulate 

%description
Data practitioners regularly use the 'R' and 'Python' programming
languages to prepare data for analyses. Thus, they encode data
preprocessing decisions in 'R' and 'Python' scripts. The 'smallsets'
package subsequently decodes these decisions into a Smallset Timeline, a
visualisation proposed in Lucchesi et al. (2022)
<doi:10.1145/3531146.3533175>. A Smallset Timeline is a series of small
data snapshots of different preprocessing steps. The 'smallsets' package
builds this figure from a user's dataset and 'R'/'Python' preprocessing
script, which contains structured comments with snapshot instructions.

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
