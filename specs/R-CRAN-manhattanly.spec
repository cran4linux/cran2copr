%global __brp_check_rpaths %{nil}
%global packname  manhattanly
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Q-Q and Manhattan Plots Using 'plotly.js'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 

%description
Create interactive manhattan, Q-Q and volcano plots that are usable from
the R console, in 'Dash' apps, in the 'RStudio' viewer pane, in 'R
Markdown' documents, and in 'Shiny' apps. Hover the mouse pointer over a
point to show details or drag a rectangle to zoom. A manhattan plot is a
popular graphical method for visualizing results from high-dimensional
data analysis such as a (epi)genome wide association study (GWAS or EWAS),
in which p-values, Z-scores, test statistics are plotted on a scatter plot
against their genomic position. Manhattan plots are used for visualizing
potential regions of interest in the genome that are associated with a
phenotype. Interactive manhattan plots allow the inspection of specific
value (e.g. rs number or gene name) by hovering the mouse over a cell, as
well as zooming into a region of the genome (e.g. a chromosome) by
dragging a rectangle around the relevant area. This work is based on the
'qqman' package and the 'plotly.js' engine. It produces similar manhattan
and Q-Q plots as the 'manhattan' and 'qq' functions in the 'qqman'
package, with the advantage of including extra annotation information and
interactive web-based visualizations directly from R. Once uploaded to a
'plotly' account, 'plotly' graphs (and the data behind them) can be viewed
and modified in a web browser.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
