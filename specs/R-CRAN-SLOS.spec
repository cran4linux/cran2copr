%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SLOS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          ICU Length of Stay Prediction and Efficiency Evaluation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-CRAN-ems 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-caretEnsemble 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-MLmetrics 
Requires:         R-CRAN-ems 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-caretEnsemble 
Requires:         R-CRAN-ranger 

%description
Provides tools for predicting ICU length of stay and assessing ICU
efficiency. It is based on the methodologies proposed by Peres et al.
(2022, 2023), which utilize data-driven approaches for modeling and
validation, offering insights into ICU performance and patient outcomes.
References: Peres et al.
(2022)<https://pubmed.ncbi.nlm.nih.gov/35988701/>, Peres et al.
(2023)<https://pubmed.ncbi.nlm.nih.gov/37922007/>. More information:
<https://github.com/igor-peres/ICU-Length-of-Stay-Prediction>.

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
