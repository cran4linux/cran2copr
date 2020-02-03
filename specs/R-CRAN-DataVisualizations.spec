%global packname  DataVisualizations
%global packver   1.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.10
Release:          1%{?dist}
Summary:          Visualizations of High-Dimensional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sp 

%description
Gives access to data visualisation methods that are relevant from the data
scientist's point of view. The flagship idea of 'DataVisualizations' is
the mirrored density plot (MD-plot) for either classified or
non-classified multivariate data presented in Thrun et al. (2019)
<arXiv:1908.06081>. The MD-plot outperforms the box-and-whisker diagram
(box plot), violin plot and bean plot. Furthermore, a collection of
various visualization methods for univariate data is provided. In the case
of exploratory data analysis, 'DataVisualizations' makes it possible to
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
<doi:10.1007/978-3-658-20540-9>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
