%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vecmatch
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Propensity Score Estimation and Matching for Multiple Groups

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-brglm2 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpp 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matching 
BuildRequires:    R-CRAN-mclogit 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-optmatch 
BuildRequires:    R-CRAN-productplots 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-brglm2 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpp 
Requires:         R-CRAN-ggpubr 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matching 
Requires:         R-CRAN-mclogit 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-optmatch 
Requires:         R-CRAN-productplots 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstatix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-withr 

%description
Implements the Vector Matching algorithm to match multiple treatment
groups based on previously estimated generalized propensity scores. The
package includes tools for visualizing initial confounder imbalances,
estimating treatment assignment probabilities using various methods,
defining the common support region, performing matching across multiple
groups, and evaluating matching quality. For more details, see Lopez and
Gutman (2017) <doi:10.1214/17-STS612>.

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
