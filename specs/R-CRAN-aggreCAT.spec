%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aggreCAT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mathematically Aggregating Expert Judgments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-GoFKernel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-precrec 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-MLmetrics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-GoFKernel 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-precrec 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-MLmetrics 

%description
The use of structured elicitation to inform decision making has grown
dramatically in recent decades, however, judgements from multiple experts
must be aggregated into a single estimate. Empirical evidence suggests
that mathematical aggregation provides more reliable estimates than
enforcing behavioural consensus on group estimates. 'aggreCAT' provides
state-of-the-art mathematical aggregation methods for elicitation data
including those defined in Hanea, A. et al. (2021)
<doi:10.1371/journal.pone.0256919>. The package also provides functions to
visualise and evaluate the performance of your aggregated estimates on
validation data.

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
