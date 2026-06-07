%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AIGRA
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Agentic Item Generation, Review, and Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-reticulate 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Provides tools for validating, generating, reviewing, reporting, and
visualising assessment item generation workflows. The package supports
tabular item-bank templates, item-bank validation, 'Python'-backed agentic
generation workflows, multimodal diagram generation, quality summaries,
and 'HTML' reporting. External artificial intelligence services and
related 'API' calls require user-supplied credentials and are not called
during package checks. The workflow is informed by automatic item
generation methods described by Gierl and Haladyna (2013,
ISBN:9780415897518) and evidence-centered assessment design described by
Mislevy et al. (2003) <doi:10.1002/j.2333-8504.2003.tb01908.x>.

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
