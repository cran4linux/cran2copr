%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crew.cluster
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Crew Launcher Plugins for Traditional High-Performance Computing Clusters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-crew >= 1.1.0
BuildRequires:    R-CRAN-ps 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-crew >= 1.1.0
Requires:         R-CRAN-ps 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-yaml 

%description
In computationally demanding analysis projects, statisticians and data
scientists asynchronously deploy long-running tasks to distributed
systems, ranging from traditional clusters to cloud services. The
'crew.cluster' package extends the 'mirai'-powered 'crew' package with
worker launcher plugins for traditional high-performance computing
systems. Inspiration also comes from packages 'mirai' by Gao (2023)
<https://github.com/r-lib/mirai>, 'future' by Bengtsson (2021)
<doi:10.32614/RJ-2021-048>, 'rrq' by FitzJohn and Ashton (2023)
<https://github.com/mrc-ide/rrq>, 'clustermq' by Schubert (2019)
<doi:10.1093/bioinformatics/btz284>), and 'batchtools' by Lang, Bischl,
and Surmann (2017). <doi:10.21105/joss.00135>.

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
