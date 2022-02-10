%global __brp_check_rpaths %{nil}
%global packname  dabestr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Analysis using Bootstrap-Coupled Estimation

License:          file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-effsize 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggbeeswarm 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-simpleboot 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 3.2
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-effsize 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggbeeswarm 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-simpleboot 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Data Analysis using Bootstrap-Coupled ESTimation. Estimation statistics is
a simple framework that avoids the pitfalls of significance testing. It
uses familiar statistical concepts: means, mean differences, and error
bars. More importantly, it focuses on the effect size of one's
experiment/intervention, as opposed to a false dichotomy engendered by P
values. An estimation plot has two key features: 1. It presents all
datapoints as a swarmplot, which orders each point to display the
underlying distribution. 2. It presents the effect size as a bootstrap 95%%
confidence interval on a separate but aligned axes. Estimation plots are
introduced in Ho et al., Nature Methods 2019, 1548-7105.
<doi:10.1038/s41592-019-0470-3>. The free-to-view PDF is located at
<https://rdcu.be/bHhJ4>.

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
