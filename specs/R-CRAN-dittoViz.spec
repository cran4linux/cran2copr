%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dittoViz
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          User Friendly Data Visualization

License:          MIT + file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggridges 
Requires:         R-stats 

%description
A comprehensive visualization toolkit built with coders of all skill
levels and color-vision impaired audiences in mind. It allows creation of
finely-tuned, publication-quality figures from single function calls.
Visualizations include scatter plots, compositional bar plots, violin,
box, and ridge plots, and more. Customization ranges from size and title
adjustments to discrete-group circling and labeling, hidden data overlay
upon cursor hovering via ggplotly() conversion, and many more, all with
simple, discrete inputs. Color blindness friendliness is powered by legend
adjustments (enlarged keys), and by allowing the use of shapes or
letter-overlay in addition to the carefully selected dittoColors().

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
