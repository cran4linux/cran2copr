%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ISCA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compare Heterogeneous Social Groups

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 5.1.3
BuildRequires:    R-stats >= 4.3.1
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-plyr >= 1.8.9
BuildRequires:    R-CRAN-e1071 >= 1.7.16
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-tidyselect >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.16.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-broom >= 1.0.7
Requires:         R-CRAN-Hmisc >= 5.1.3
Requires:         R-stats >= 4.3.1
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-plyr >= 1.8.9
Requires:         R-CRAN-e1071 >= 1.7.16
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-tidyselect >= 1.2.1
Requires:         R-CRAN-data.table >= 1.16.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-broom >= 1.0.7

%description
The Inductive Subgroup Comparison Approach ('ISCA') offers a way to
compare groups that are internally differentiated and heterogeneous. It
starts by identifying the social structure of a reference group against
which a minority or another group is to be compared, yielding empirical
subgroups to which minority members are then matched based on how similar
they are. The modelling of specific outcomes then occurs within specific
subgroups in which majority and minority members are matched. 'ISCA' is
characterized by its data-driven, probabilistic, and iterative approach
and combines fuzzy clustering, Monte Carlo simulation, and regression
analysis. ISCA_random_assignments() assigns subjects probabilistically to
subgroups. ISCA_clustertable() provides summary statistics of each cluster
across iterations. ISCA_modeling() provides Ordinary Least Squares
regression results for each cluster across iterations. For further details
please see Drouhot (2021) <doi:10.1086/712804>.

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
