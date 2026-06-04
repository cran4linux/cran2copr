%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayprior
%global packver   0.2.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.12
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Prior Elicitation and Diagnostics for Clinical Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.1
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-rlang >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-shinycssloaders >= 1.0.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.7.6
BuildRequires:    R-CRAN-shinydashboard >= 0.7.2
BuildRequires:    R-CRAN-golem >= 0.4.1
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-DT >= 0.27
BuildRequires:    R-stats 
Requires:         R-CRAN-plotly >= 4.10.1
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-rlang >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-shinycssloaders >= 1.0.0
Requires:         R-CRAN-shinyWidgets >= 0.7.6
Requires:         R-CRAN-shinydashboard >= 0.7.2
Requires:         R-CRAN-golem >= 0.4.1
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-DT >= 0.27
Requires:         R-stats 

%description
A toolkit for constructing, validating, and justifying Bayesian priors in
clinical trial settings. Implements expert elicitation via quantile
matching, the roulette method, and moment matching across six distribution
families, linear and logarithmic expert pooling, prior-data conflict
diagnostics including the Box p-value, surprise index, information
divergence, and Mahalanobis distance, sensitivity analyses with tornado
and influence heatmap plots, sceptical, robust, and power priors, and
automated prior justification reports. Includes a fully modular 'Shiny'
application for interactive use. Methods based on O'Hagan et al. (2006,
ISBN:9780470029886), Box (1980) <doi:10.2307/2982063>, Oakley and O'Hagan
(2010) <https://tonyohagan.co.uk/shelf/>, Schmidli et al. (2014)
<doi:10.1111/biom.12242>, Ibrahim and Chen (2000)
<doi:10.1214/ss/1009212673>, Spiegelhalter et al. (1994)
<doi:10.2307/2983527>.

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
