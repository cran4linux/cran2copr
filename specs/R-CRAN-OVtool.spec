%global packname  OVtool
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Omitted Variable Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-CRAN-varhandle 
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-metR 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-survey 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-twang 
Requires:         R-CRAN-varhandle 

%description
This tool was designed to assess the sensitivity of research findings to
omitted variables when estimating causal effects using propensity score
(PS) weighting. This tool produces graphics and summary results that will
enable a researcher to quantify the impact an omitted variable would have
on their results. Burgette et al. (2021) describe the methodology behind
the primary function in this package, ov_sim. The method is demonstrated
in Griffin et al. (2020) <doi:10.1016/j.jsat.2020.108075>.

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
