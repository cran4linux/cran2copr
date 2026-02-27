%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ACTCD
%global packver   1.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Asymptotic Classification Theory for Cognitive Diagnosis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-GDINA 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R.methodsS3 
Requires:         R-CRAN-GDINA 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-R.methodsS3 

%description
Cluster analysis for cognitive diagnosis based on the Asymptotic
Classification Theory (Chiu, Douglas & Li, 2009;
<doi:10.1007/s11336-009-9125-0>). Given the sample statistic of
sum-scores, cluster analysis techniques can be used to classify examinees
into latent classes based on their attribute patterns. In addition to the
algorithms used to classify data, three labeling approaches are proposed
to label clusters so that examinees' attribute profiles can be obtained.

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
