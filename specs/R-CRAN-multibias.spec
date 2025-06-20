%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multibias
%global packver   1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Bias Analysis in Causal Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-dplyr >= 1.1.3
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-broom >= 1.0.5
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-dplyr >= 1.1.3
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-broom >= 1.0.5
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-purrr >= 1.0.0

%description
Quantify the causal effect of a binary exposure on a binary outcome with
adjustment for multiple biases. The functions can simultaneously adjust
for any combination of uncontrolled confounding, exposure/outcome
misclassification, and selection bias. The underlying method generalizes
the concept of combining inverse probability of selection weighting with
predictive value weighting. Simultaneous multi-bias analysis can be used
to enhance the validity and transparency of real-world evidence obtained
from observational, longitudinal studies. Based on the work from Paul
Brendel, Aracelis Torres, and Onyebuchi Arah (2023)
<doi:10.1093/ije/dyad001>.

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
