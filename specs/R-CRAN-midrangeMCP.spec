%global __brp_check_rpaths %{nil}
%global packname  midrangeMCP
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multiples Comparisons Procedures Based on Studentized Midrange and Range Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-SMR 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-tcltk 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-SMR 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-xtable 
Requires:         R-tcltk 

%description
Apply tests of multiple comparisons based on studentized 'midrange' and
'range' distributions. The tests are: Tukey Midrange ('TM' test),
Student-Newman-Keuls Midrange ('SNKM' test), Means Grouping Midrange
('MGM' test) and Means Grouping Range ('MGR' test). The first two tests
were published by Batista and Ferreira (2020)
<doi:10.1590/1413-7054202044008020>. The last two are being published.

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
