%global __brp_check_rpaths %{nil}
%global packname  GFD
%global packver   0.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Tests for General Factorial Designs

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.43
BuildRequires:    R-CRAN-plotrix >= 3.5.12
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-magic >= 1.5.6
BuildRequires:    R-CRAN-Matrix >= 1.2.2
BuildRequires:    R-methods 
Requires:         R-CRAN-MASS >= 7.3.43
Requires:         R-CRAN-plotrix >= 3.5.12
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-magic >= 1.5.6
Requires:         R-CRAN-Matrix >= 1.2.2
Requires:         R-methods 

%description
Implemented are the Wald-type statistic, a permuted version thereof as
well as the ANOVA-type statistic for general factorial designs, even with
non-normal error terms and/or heteroscedastic variances, for crossed
designs with an arbitrary number of factors and nested designs with up to
three factors. Friedrich et al. (2017) <doi:10.18637/jss.v079.c01>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
