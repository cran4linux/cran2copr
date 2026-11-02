%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggvolc
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Volcano Plots for Differential Gene Expression Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-patchwork 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 

%description
Creates customizable volcano plots for differential gene expression
results from RNA-seq analyses. Accepts result objects or tables from
'DESeq2', 'edgeR', and 'limma' directly, with automatic column detection.
Labels the most significant or chosen genes, colors gene sets, compares
several contrasts side by side, offers colorblind-safe color presets, and
can produce interactive plots with 'ggiraph'. Gene tables are rendered
with 'gt' and composed with 'patchwork'.

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
