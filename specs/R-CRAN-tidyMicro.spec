%global __brp_check_rpaths %{nil}
%global packname  tidyMicro
%global packver   1.47
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.47
Release:          1%{?dist}%{?buildtag}
Summary:          A Pipeline for Microbiome Analysis and Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-plotly >= 4.9.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-car >= 3.0.3
BuildRequires:    R-CRAN-vegan >= 2.5.5
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-tibble >= 2.1.0
BuildRequires:    R-CRAN-plyr >= 1.8.0
BuildRequires:    R-CRAN-ade4 >= 1.7.13
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyverse >= 1.3.0
BuildRequires:    R-CRAN-shapes >= 1.2.4
BuildRequires:    R-Matrix >= 1.2.17
BuildRequires:    R-CRAN-ThreeWay >= 1.1.3
BuildRequires:    R-CRAN-lme4 >= 1.1.21
BuildRequires:    R-CRAN-VGAM >= 1.1.2
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-factoextra >= 1.0.5
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-cowplot >= 0.9.4
BuildRequires:    R-CRAN-Evomorph >= 0.9
BuildRequires:    R-CRAN-ggrepel >= 0.8.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-broom >= 0.5.0
BuildRequires:    R-CRAN-lsr >= 0.5
BuildRequires:    R-CRAN-latex2exp >= 0.4.0
BuildRequires:    R-CRAN-scatterplot3d >= 0.3.41
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-png >= 0.1.7
Requires:         R-MASS >= 7.3.51.4
Requires:         R-CRAN-plotly >= 4.9.0
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-car >= 3.0.3
Requires:         R-CRAN-vegan >= 2.5.5
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-tibble >= 2.1.0
Requires:         R-CRAN-plyr >= 1.8.0
Requires:         R-CRAN-ade4 >= 1.7.13
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyverse >= 1.3.0
Requires:         R-CRAN-shapes >= 1.2.4
Requires:         R-Matrix >= 1.2.17
Requires:         R-CRAN-ThreeWay >= 1.1.3
Requires:         R-CRAN-lme4 >= 1.1.21
Requires:         R-CRAN-VGAM >= 1.1.2
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-factoextra >= 1.0.5
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-cowplot >= 0.9.4
Requires:         R-CRAN-Evomorph >= 0.9
Requires:         R-CRAN-ggrepel >= 0.8.1
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-broom >= 0.5.0
Requires:         R-CRAN-lsr >= 0.5
Requires:         R-CRAN-latex2exp >= 0.4.0
Requires:         R-CRAN-scatterplot3d >= 0.3.41
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-png >= 0.1.7

%description
A reliable alternative to popular microbiome analysis R packages. We
provide standard tools as well as novel extensions on standard analyses to
improve interpretability and the analyst’s ability to communicate results,
all while maintaining object malleability to encourage open source
collaboration.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
