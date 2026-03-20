%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  starburst
%global packver   0.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.8
Release:          1%{?dist}%{?buildtag}
Summary:          Seamless AWS Cloud Bursting for Parallel R Workloads

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.33.0
BuildRequires:    R-CRAN-globals 
BuildRequires:    R-CRAN-paws.compute 
BuildRequires:    R-CRAN-paws.storage 
BuildRequires:    R-CRAN-paws.management 
BuildRequires:    R-CRAN-paws.security.identity 
BuildRequires:    R-CRAN-qs2 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-processx 
Requires:         R-CRAN-future >= 1.33.0
Requires:         R-CRAN-globals 
Requires:         R-CRAN-paws.compute 
Requires:         R-CRAN-paws.storage 
Requires:         R-CRAN-paws.management 
Requires:         R-CRAN-paws.security.identity 
Requires:         R-CRAN-qs2 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-processx 

%description
A 'future' backend that enables seamless execution of parallel R workloads
on 'Amazon Web Services' ('AWS', <https://aws.amazon.com>), including
'EC2' and 'Fargate'. 'staRburst' handles environment synchronization, data
transfer, quota management, and worker orchestration automatically,
allowing users to scale from local execution to 100+ cloud workers with a
single line of code change.

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
