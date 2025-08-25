%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DataVisualizations
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizations of High-Dimensional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-RcppParallel >= 5.1.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-RcppParallel >= 5.1.4
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-reshape2 

%description
Gives access to data visualisation methods that are relevant from the data
scientist's point of view. The flagship idea of 'DataVisualizations' is
the mirrored density plot (MD-plot) for either classified or
non-classified multivariate data published in Thrun, M.C. et al.:
"Analyzing the Fine Structure of Distributions" (2020), PLoS ONE,
<DOI:10.1371/journal.pone.0238835>. The MD-plot outperforms the
box-and-whisker diagram (box plot), violin plot and bean plot and
geom_violin plot of ggplot2. Furthermore, a collection of various
visualization methods for univariate data is provided. In the case of
exploratory data analysis, 'DataVisualizations' makes it possible to
inspect the distribution of each feature of a dataset visually through a
combination of four methods. One of these methods is the Pareto density
estimation (PDE) of the probability density function (pdf). Additionally,
visualizations of the distribution of distances using PDE, the
scatter-density plot using PDE for two variables as well as the Shepard
density plot and the Bland-Altman plot are presented here. Pertaining to
classified high-dimensional data, a number of visualizations are
described, such as f.ex. the heat map and silhouette plot. A political map
of the world or Germany can be visualized with the additional information
defined by a classification of countries or regions. By extending the
political map further, an uncomplicated function for a Choropleth map can
be used which is useful for measurements across a geographic area. For
categorical features, the Pie charts, slope charts and fan plots, improved
by the ABC analysis, become usable. More detailed explanations are found
in the book by Thrun, M.C.: "Projection-Based Clustering through
Self-Organization and Swarm Intelligence" (2018)
<DOI:10.1007/978-3-658-20540-9>.

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
