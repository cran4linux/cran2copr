%global packname  manhattanly
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Interactive Q-Q and Manhattan Plots Using 'plotly.js'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.5.6
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-magrittr >= 1.0.1
BuildRequires:    R-stats 
Requires:         R-CRAN-plotly >= 4.5.6
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-magrittr >= 1.0.1
Requires:         R-stats 

%description
Create interactive Q-Q, manhattan and volcano plots that are usable from
the R console, in the 'RStudio' viewer pane, in 'R Markdown' documents,
and in 'Shiny' apps. Hover the mouse pointer over a point to show details
or drag a rectangle to zoom. A manhattan plot is a popular graphical
method for visualizing results from high-dimensional data analysis such as
a (epi)genome wide association study (GWAS or EWAS), in which p-values,
Z-scores, test statistics are plotted on a scatter plot against their
genomic position. Manhattan plots are used for visualizing potential
regions of interest in the genome that are associated with a phenotype.
Interactive manhattan plots allow the inspection of specific value (e.g.
rs number or gene name) by hovering the mouse over a cell, as well as
zooming into a region of the genome (e.g. a chromosome) by dragging a
rectangle around the relevant area. This work is based on the 'qqman'
package by Stephen Turner and the 'plotly.js' engine. It produces similar
manhattan and Q-Q plots as the 'manhattan' and 'qq' functions in the
'qqman' package, with the advantage of including extra annotation
information and interactive web-based visualizations directly from R. Once
uploaded to a 'plotly' account, 'plotly' graphs (and the data behind them)
can be viewed and modified in a web browser.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
