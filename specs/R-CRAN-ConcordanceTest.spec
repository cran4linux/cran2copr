%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ConcordanceTest
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          An Alternative to the Kruskal-Wallis Based on the Kendall Tau Distance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rglpk 
Requires:         R-stats 
Requires:         R-graphics 

%description
The Concordance Test is a non-parametric method for testing whether two o
more samples originate from the same distribution. It extends the Kendall
Tau correlation coefficient when there are only two groups. For details,
see Alcaraz J., Anton-Sanchez L., Monge J.F. (2022) The Concordance Test,
an Alternative to Kruskal-Wallis Based on the Kendall-tau Distance: An R
Package. The R Journal 14, 26–53 <doi:10.32614/RJ-2022-039>.

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
