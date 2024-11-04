%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crew
%global packver   0.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Distributed Worker Launcher Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.1.0
BuildRequires:    R-CRAN-mirai >= 1.3.0
BuildRequires:    R-CRAN-nanonext >= 1.3.0
BuildRequires:    R-CRAN-autometric >= 0.1.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-getip 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-ps 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.1.0
Requires:         R-CRAN-mirai >= 1.3.0
Requires:         R-CRAN-nanonext >= 1.3.0
Requires:         R-CRAN-autometric >= 0.1.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-getip 
Requires:         R-CRAN-later 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-ps 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-tools 
Requires:         R-utils 

%description
In computationally demanding analysis projects, statisticians and data
scientists asynchronously deploy long-running tasks to distributed
systems, ranging from traditional clusters to cloud services. The
'NNG'-powered 'mirai' R package by Gao (2023) <doi:10.5281/zenodo.7912722>
is a sleek and sophisticated scheduler that efficiently processes these
intense workloads. The 'crew' package extends 'mirai' with a unifying
interface for third-party worker launchers. Inspiration also comes from
packages. 'future' by Bengtsson (2021) <doi:10.32614/RJ-2021-048>, 'rrq'
by FitzJohn and Ashton (2023) <https://github.com/mrc-ide/rrq>,
'clustermq' by Schubert (2019) <doi:10.1093/bioinformatics/btz284>), and
'batchtools' by Lang, Bischel, and Surmann (2017)
<doi:10.21105/joss.00135>.

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
