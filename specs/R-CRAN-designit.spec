%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  designit
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Blocking and Randomization for Experimental Design

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-data.table 
Requires:         R-stats 

%description
Intelligently assign samples to batches in order to reduce batch effects.
Batch effects can have a significant impact on data analysis, especially
when the assignment of samples to batches coincides with the contrast
groups being studied. By defining a batch container and a scoring function
that reflects the contrasts, this package allows users to assign samples
in a way that minimizes the potential impact of batch effects on the
comparison of interest. Among other functionality, we provide an
implementation for OSAT score by Yan et al. (2012,
<doi:10.1186/1471-2164-13-689>).

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
