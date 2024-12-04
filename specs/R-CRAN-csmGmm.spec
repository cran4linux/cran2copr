%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  csmGmm
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditionally Symmetric Multidimensional Gaussian Mixture Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 

%description
Implements the conditionally symmetric multidimensional Gaussian mixture
model (csmGmm) for large-scale testing of composite null hypotheses in
genetic association applications such as mediation analysis, pleiotropy
analysis, and replication analysis. In such analyses, we typically have J
sets of K test statistics where K is a small number (e.g. 2 or 3) and J is
large (e.g. 1 million). For each one of the J sets, we want to know if we
can reject all K individual nulls. Please see the vignette for a
quickstart guide. The paper describing these methods is "Testing a Large
Number of Composite Null Hypotheses Using Conditionally Symmetric
Multidimensional Gaussian Mixtures in Genome-Wide Studies" by Sun R, McCaw
Z, & Lin X (2024, <doi:10.1080/01621459.2024.2422124>). The paper is
accepted and published online (but not yet in print) in the Journal of the
American Statistical Association as of Dec 1 2024.

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
