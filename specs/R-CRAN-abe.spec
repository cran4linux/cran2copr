%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  abe
%global packver   5.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Augmented Backward Elimination

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-survival >= 3.4.0
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-CRAN-tidytext >= 0.4.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-survival >= 3.4.0
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-reshape2 >= 1.4.0
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-tidytext >= 0.4.0

%description
Performs augmented backward elimination and checks the stability of the
obtained model. Augmented backward elimination combines significance or
information based criteria with the change in estimate to either select
the optimal model for prediction purposes or to serve as a tool to obtain
a practically sound, highly interpretable model. More details can be found
in Dunkler et al. (2014) <doi:10.1371/journal.pone.0113677>.

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
