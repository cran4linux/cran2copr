%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rosetta
%global packver   0.3.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.12
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Use of Statistical Packages in Teaching

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car >= 3.0.2
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-psych >= 1.8.4
BuildRequires:    R-CRAN-pwr >= 1.2.2
BuildRequires:    R-CRAN-lme4 >= 1.1.19
BuildRequires:    R-CRAN-ggrepel >= 0.8
BuildRequires:    R-CRAN-lavaan >= 0.6.5
BuildRequires:    R-CRAN-pander >= 0.6.3
BuildRequires:    R-CRAN-rmdpartials >= 0.5.8
BuildRequires:    R-CRAN-ufs >= 0.5.2
BuildRequires:    R-CRAN-multcompView >= 0.1
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-sjstats 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
Requires:         R-CRAN-car >= 3.0.2
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-psych >= 1.8.4
Requires:         R-CRAN-pwr >= 1.2.2
Requires:         R-CRAN-lme4 >= 1.1.19
Requires:         R-CRAN-ggrepel >= 0.8
Requires:         R-CRAN-lavaan >= 0.6.5
Requires:         R-CRAN-pander >= 0.6.3
Requires:         R-CRAN-rmdpartials >= 0.5.8
Requires:         R-CRAN-ufs >= 0.5.2
Requires:         R-CRAN-multcompView >= 0.1
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-sjstats 
Requires:         R-stats 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 

%description
When teaching statistics, it can often be desirable to uncouple the
content from specific software packages. To ease such efforts, the Rosetta
Stats website (<https://rosettastats.com>) allows comparing analyses in
different packages. This package is the companion to the Rosetta Stats
website, aiming to provide functions that produce output that is similar
to output from other statistical packages, thereby facilitating
'software-agnostic' teaching of statistics.

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
