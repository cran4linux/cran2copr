%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyLPA
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Carry Out Latent Profile Analysis (LPA) Using Open-Source or Commercial Software

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.1
BuildRequires:    R-CRAN-tidySEM >= 0.2.10
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 4.0.1
Requires:         R-CRAN-tidySEM >= 0.2.10
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 

%description
Easily carry out latent profile analysis ("LPA"), determine the correct
number of classes based on best practices, and tabulate and plot the
results. Provides functionality to estimate commonly-specified models with
free means, variances, and covariances for each profile. Follows a tidy
approach, in that output is in the form of a data frame that can
subsequently be computed on. Models can be estimated using the free open
source 'R' packages 'Mclust' and 'OpenMx', or using the commercial program
'MPlus', via the 'MplusAutomation' package.

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
