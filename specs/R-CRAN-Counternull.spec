%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Counternull
%global packver   0.2.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.12
Release:          1%{?dist}%{?buildtag}
Summary:          Randomization-Based Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-effsize 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-randomizr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-effsize 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-randomizr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
Randomization-Based Inference for customized experiments. Computes
Fisher-Exact P-Values alongside null randomization distributions.
Retrieves counternull sets and generates counternull distributions.
Computes Fisher Intervals and Fisher-Adjusted P-Values. Package includes
visualization of randomization distributions and Fisher Intervals. Users
can input custom test statistics and their own methods for randomization.
Rosenthal and Rubin (1994) <doi:10.1111/j.1467-9280.1994.tb00281.x>.

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
