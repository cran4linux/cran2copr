%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AugmentedPooledRCBD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Augmented Pooled Randomized Complete Block Design Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-rlang 

%description
Augmented randomized complete block designs (augmented RCBDs) are useful
for researchers to evaluate large numbers of unreplicated test entries
with limited replicated checks. This R and 'Shiny'-based statistical
package provides methods for the analysis of augmented randomized complete
block designs (augmented RCBDs) across multiple environments. The package
performs environment-wise augmented RCBD analysis and pooled analysis
across environments, including analysis of variance (ANOVA), testing for
homogeneity of error variances across environments, adjusted treatment
means, treatment sum-of-squares partitioning, standard error of the mean
(SEM), critical difference (CD), and treatment ranking. For pooled
analysis, environment-specific error variances are assessed for
homogeneity and used for appropriate transformation where required,
followed by a general linear model incorporating environment, block nested
within environment, treatment, and environment x treatment interaction.
This 'Shiny' interface provides a user-friendly platform that enables
researchers and plant breeders to perform these analyses without requiring
extensive programming knowledge. For method details see, Federer, W. T.
(1961) <doi:10.2307/2527837>. It consists of the function
augmentedPooledRCBD() which launches the application interface.

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
