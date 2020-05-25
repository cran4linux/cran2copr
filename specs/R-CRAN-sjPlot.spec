%global packname  sjPlot
%global packver   2.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.4
Release:          1%{?dist}
Summary:          Data Visualization for Statistics in Social Science

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-sjmisc >= 2.8.2
BuildRequires:    R-CRAN-sjlabelled >= 1.1.2
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-insight >= 0.8.0
BuildRequires:    R-CRAN-parameters >= 0.7.0
BuildRequires:    R-CRAN-bayestestR >= 0.6.0
BuildRequires:    R-CRAN-performance >= 0.4.3
BuildRequires:    R-CRAN-sjstats >= 0.17.8
BuildRequires:    R-CRAN-ggeffects >= 0.14.3
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-effectsize 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-sjmisc >= 2.8.2
Requires:         R-CRAN-sjlabelled >= 1.1.2
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-insight >= 0.8.0
Requires:         R-CRAN-parameters >= 0.7.0
Requires:         R-CRAN-bayestestR >= 0.6.0
Requires:         R-CRAN-performance >= 0.4.3
Requires:         R-CRAN-sjstats >= 0.17.8
Requires:         R-CRAN-ggeffects >= 0.14.3
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-effectsize 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
Collection of plotting and table output functions for data visualization.
Results of various statistical analyses (that are commonly used in social
sciences) can be visualized using this package, including simple and cross
tabulated frequencies, histograms, box plots, (generalized) linear models,
mixed effects models, principal component analysis and correlation
matrices, cluster analyses, scatter plots, stacked scales, effects plots
of regression models (including interaction terms) and much more. This
package supports labelled data.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
