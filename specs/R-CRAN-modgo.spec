%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modgo
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mock Data Generation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-psych >= 2.2.9
BuildRequires:    R-CRAN-GLDEX >= 2.0.0.9.2
BuildRequires:    R-CRAN-Matrix >= 1.6.1.1
BuildRequires:    R-CRAN-patchwork >= 1.1.2
BuildRequires:    R-CRAN-gp >= 1.0
BuildRequires:    R-CRAN-wesanderson >= 0.3.6.9000
BuildRequires:    R-CRAN-ggcorrplot >= 0.1.4.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-psych >= 2.2.9
Requires:         R-CRAN-GLDEX >= 2.0.0.9.2
Requires:         R-CRAN-Matrix >= 1.6.1.1
Requires:         R-CRAN-patchwork >= 1.1.2
Requires:         R-CRAN-gp >= 1.0
Requires:         R-CRAN-wesanderson >= 0.3.6.9000
Requires:         R-CRAN-ggcorrplot >= 0.1.4.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-survival 

%description
Generation of synthetic data from a real dataset using the combination of
rank normal inverse transformation with the calculation of correlation
matrix <doi:10.1055/a-2048-7692>. Completely artificial data may be
generated through the use of Generalized Lambda Distribution and
Generalized Poisson Distribution <doi:10.1201/9781420038040>.
Quantitative, binary, ordinal categorical, and survival data may be
simulated. Functionalities are offered to generate synthetic data sets
according to user's needs.

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
