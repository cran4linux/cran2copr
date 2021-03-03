%global packname  flowr
%global packver   0.9.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.11
Release:          1%{?dist}%{?buildtag}
Summary:          Streamlining Design and Deployment of Complex Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-params >= 0.7
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-params >= 0.7
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-whisker 
Requires:         R-tools 
Requires:         R-CRAN-readr 

%description
This framework allows you to design and implement complex pipelines, and
deploy them on your institution's computing cluster. This has been built
keeping in mind the needs of bioinformatics workflows. However, it is
easily extendable to any field where a series of steps (shell commands)
are to be executed in a (work)flow.

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
