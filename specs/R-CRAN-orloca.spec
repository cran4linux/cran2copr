%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  orloca
%global packver   5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Operations Research LOCational Analysis Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-png 
Requires:         R-CRAN-ucminf 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 

%description
Objects and methods to handle and solve the min-sum location problem, also
known as Fermat-Weber problem. The min-sum location problem search for a
point such that the weighted sum of the distances to the demand points are
minimized. See "The Fermat-Weber location problem revisited" by Brimberg,
Mathematical Programming, 1, pg. 71-76, 1995. <DOI:10.1007/BF01592245>.
General global optimization algorithms are used to solve the problem,
along with the adhoc Weiszfeld method, see "Sur le point pour lequel la
Somme des distances de n points donnes est minimum", by Weiszfeld, Tohoku
Mathematical Journal, First Series, 43, pg. 355-386, 1937 or "On the point
for which the sum of the distances to n given points is minimum", by E.
Weiszfeld and F. Plastria, Annals of Operations Research, 167, pg. 7-41,
2009. <DOI:10.1007/s10479-008-0352-z>.

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
