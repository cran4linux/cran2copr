%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SwPcIndex
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Survey Weighted PC Based Composite Index

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
An index is created using a mathematical model that transforms
multi-dimensional variables into a single value. These variables are often
correlated, and while PCA-based indices can address the issue of
multicollinearity, they typically do not account for survey weights, which
can lead to inaccurate rankings of survey units such as households,
districts, or states. To resolve this, the current package facilitates the
development of a principal component analysis-based composite index by
incorporating survey weights for each sample observation. This ensures the
generation of a survey-weighted principal component-based normalized
composite index. Additionally, the package provides a normalized principal
component-based composite index and ranks the sample observations based on
the values of the composite indices. For method details see, Skinner, C.
J., Holmes, D. J. and Smith, T. M. F. (1986)
<DOI:10.1080/01621459.1986.10478336>, Singh, D., Basak, P., Kumar, R. and
Ahmad, T. (2023) <DOI:10.3389/fams.2023.1274530>.

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
