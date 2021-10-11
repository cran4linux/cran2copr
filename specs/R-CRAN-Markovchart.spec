%global __brp_check_rpaths %{nil}
%global packname  Markovchart
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Markov Chain-Based Cost-Optimal Control Charts

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-metR 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-optimParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-metR 

%description
Functions for cost-optimal control charts with a focus on health care
applications. Compared to assumptions in traditional control chart theory,
here, we allow random shift sizes, random repair and random sampling
times. The package focuses on X-bar charts with a sample size of 1
(representing the monitoring of a single patient at a time). The methods
are described in Zempleni et al. (2004) <doi:10.1002/asmb.521>, Dobi and
Zempleni (2019) <doi:10.1002/qre.2518> and Dobi and Zempleni (2019)
<http://ac.inf.elte.hu/Vol_049_2019/129_49.pdf>.

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
