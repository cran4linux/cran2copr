%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  comparer
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Compare Output and Run Time

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GauPro >= 0.2.7
BuildRequires:    R-CRAN-mixopt 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-GauPro >= 0.2.7
Requires:         R-CRAN-mixopt 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-R6 

%description
Quickly run experiments to compare the run time and output of code blocks.
The function mbc() can make fast comparisons of code, and will calculate
statistics comparing the resulting outputs. It can be used to compare
model fits to the same data or see which function runs faster. The R6
class ffexp$new() runs a function using all possible combinations of
selected inputs. This is useful for comparing the effect of different
parameter values. It can also run in parallel and automatically save
intermediate results, which is very useful for long computations.

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
