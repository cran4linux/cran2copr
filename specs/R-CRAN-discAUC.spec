%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  discAUC
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Linear and Non-Linear AUC for Discounting Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 

%description
Area under the curve (AUC; Myerson et al., 2001)
<doi:10.1901/jeab.2001.76-235> is a popular measure used in discounting
research. Although the calculation of AUC is standardized, there are
differences in AUC based on some assumptions. For example, Myerson et al.
(2001) <doi:10.1901/jeab.2001.76-235> assumed that (with delay discounting
data) a researcher would impute an indifference point at zero delay equal
to the value of the larger, later outcome. However, this practice is not
clearly followed. This imputed zero-delay indifference point plays an
important role in log and ordinal versions of AUC. Ordinal and log
versions of AUC are described by Borges et al.
(2016)<doi:10.1002/jeab.219>. The package can calculate all three versions
of AUC [and includes a new version: IHS(AUC)], impute indifference points
when x = 0, calculate ordinal AUC in the case of Halton sampling of
x-values, and account for probability discounting AUC.

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
