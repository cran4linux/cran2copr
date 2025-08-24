%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DImodelsVis
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Visualising and Interpreting Statistical Models Fit to Compositional Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DImodels >= 1.3.3
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-ggtext >= 0.1.2
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-CRAN-PieGlyph 
BuildRequires:    R-CRAN-plotwidgets 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-DImodels >= 1.3.3
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-ggtext >= 0.1.2
Requires:         R-CRAN-cli 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggfortify 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-CRAN-insight 
Requires:         R-methods 
Requires:         R-CRAN-metR 
Requires:         R-CRAN-PieGlyph 
Requires:         R-CRAN-plotwidgets 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Statistical models fit to compositional data are often difficult to
interpret due to the sum to 1 constraint on data variables. 'DImodelsVis'
provides novel visualisations tools to aid with the interpretation of
models fit to compositional data. All visualisations in the package are
created using the 'ggplot2' plotting framework and can be extended like
every other 'ggplot' object.

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
