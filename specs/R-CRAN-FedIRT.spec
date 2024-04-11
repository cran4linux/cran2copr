%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FedIRT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Federated Item Response Theory Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinyjs 

%description
Integrate Item Response Theory (IRT) and Federated Learning to estimate
traditional IRT models, including the 2-Parameter Logistic (2PL) and the
Graded Response Models, with enhanced privacy. It allows for the
estimation in a distributed manner without compromising accuracy. A
user-friendly 'shiny' application is included. For more details, see
Biying Zhou, Feng Ji (2024) "'FedIRT': An R package and 'shiny' app for
estimating federated item response theory models"
<https://github.com/Feng-Ji-Lab/FedIRT/blob/main/paper/paper.pdf>.

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
