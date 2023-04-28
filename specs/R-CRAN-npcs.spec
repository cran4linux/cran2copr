%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npcs
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Neyman-Pearson Classification via Cost-Sensitive Learning

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-smotefamily 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-nnet 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-smotefamily 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-nnet 

%description
We connect the multi-class Neyman-Pearson classification (NP) problem to
the cost-sensitive learning (CS) problem, and propose two algorithms
(NPMC-CX and NPMC-ER) to solve the multi-class NP problem through
cost-sensitive learning tools. Under certain conditions, the two
algorithms are shown to satisfy multi-class NP properties. More details
are available in the paper "Neyman-Pearson Multi-class Classification via
Cost-sensitive Learning" (Ye Tian and Yang Feng, 2021).

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
