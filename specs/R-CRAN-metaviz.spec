%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaviz
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Plots, Funnel Plots, and Visual Funnel Plot Inference for Meta-Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-gridExtra >= 2.2.1
BuildRequires:    R-CRAN-metafor >= 1.9.9
BuildRequires:    R-CRAN-scales >= 1.4.0
BuildRequires:    R-CRAN-ggpattern >= 1.1.4
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-DescTools >= 0.99.54
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-ggbeeswarm >= 0.7.2
BuildRequires:    R-CRAN-ggnewscale >= 0.5.1
BuildRequires:    R-CRAN-gtable >= 0.3.6
BuildRequires:    R-CRAN-nullabor >= 0.3.5
BuildRequires:    R-CRAN-moments >= 0.14.1
BuildRequires:    R-CRAN-ggpubr >= 0.1.6
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-gridExtra >= 2.2.1
Requires:         R-CRAN-metafor >= 1.9.9
Requires:         R-CRAN-scales >= 1.4.0
Requires:         R-CRAN-ggpattern >= 1.1.4
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-DescTools >= 0.99.54
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-ggbeeswarm >= 0.7.2
Requires:         R-CRAN-ggnewscale >= 0.5.1
Requires:         R-CRAN-gtable >= 0.3.6
Requires:         R-CRAN-nullabor >= 0.3.5
Requires:         R-CRAN-moments >= 0.14.1
Requires:         R-CRAN-ggpubr >= 0.1.6
Requires:         R-CRAN-magrittr 

%description
A compilation of functions to create visually appealing and
information-rich plots of meta-analytic data using 'ggplot2'. Provides
functions to create forest plots, funnel plots, and many of their
variants, including rainforest plots, thick forest plots, additional
evidence contour funnel plots, and sunset funnel plots. In addition,
functionalities for visual inference with funnel plots in the context of
meta-analysis are provided. Further functionalities include plots for
comparing fixed-effect and random-effects models and dedicated
visualizations for three-level meta-analysis.

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
