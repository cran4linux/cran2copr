%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  r2dictionary
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Mini-Dictionary for 'R', 'shiny' and 'rmarkdown' Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel > 3.6
Requires:         R-core > 3.6
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 

%description
Despite the predominant use of R for data manipulation and various robust
statistical calculations, in recent years, more people from various
disciplines are beginning to use R for other purposes. In doing this
seemlessly, further tools are needed users to easily and freely write in R
for all kinds of purposes. The r2dictionary introduces a means for users
to directly search for definitions of terms within the R environment.

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
