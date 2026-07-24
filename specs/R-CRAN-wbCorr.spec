%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wbCorr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bivariate Within- and Between-Cluster Correlations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-writexl 
Requires:         R-methods 
Requires:         R-CRAN-writexl 

%description
Separates supplied variables into within- and between-cluster components
and calculates bivariate correlations for each level separately. For
Pearson correlations, the centered-score decomposition corresponds to
commonly used between- and within-cluster correlations reviewed by Tu et
al. (2025) <doi:10.1002/sim.10326>. The package's descriptive Spearman
option is distinct from the clustered rank parameters introduced in that
paper. The package is also motivated by the distinction between within-
and between-person variation described by Curran and Bauer (2011)
<doi:10.1146/annurev.psych.093008.100356> and by Hamaker (2024)
<doi:10.1080/00273171.2022.2155930>. The package is intended for
longitudinal or otherwise clustered data where researchers need
transparent correlation matrices before fitting more complex multilevel
models.

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
