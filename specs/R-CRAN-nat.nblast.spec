%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nat.nblast
%global packver   1.6.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.7
Release:          1%{?dist}%{?buildtag}
Summary:          NeuroAnatomy Toolbox ('nat') Extension for Assessing Neuron Similarity and Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-nat >= 1.5.12
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-dendroextras 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-spam 
Requires:         R-CRAN-nat >= 1.5.12
Requires:         R-CRAN-rgl 
Requires:         R-methods 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-dendroextras 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-spam 

%description
Extends package 'nat' (NeuroAnatomy Toolbox) by providing a collection of
NBLAST-related functions for neuronal morphology comparison (Costa et al.
(2016) <doi: 10.1016/j.neuron.2016.06.012>).

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
