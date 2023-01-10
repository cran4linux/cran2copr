%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cencrne
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Consistent Estimation of the Number of Communities via Regularized Network Embedding

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 

%description
The network analysis plays an important role in numerous application
domains including biomedicine. Estimation of the number of communities is
a fundamental and critical issue in network analysis. Most existing
studies assume that the number of communities is known a priori, or lack
of rigorous theoretical guarantee on the estimation consistency. This
method proposes a regularized network embedding model to simultaneously
estimate the community structure and the number of communities in a
unified formulation. The proposed model equips network embedding with a
novel composite regularization term, which pushes the embedding vector
towards its center and collapses similar community centers with each
other. A rigorous theoretical analysis is conducted, establishing
asymptotic consistency in terms of community detection and estimation of
the number of communities. Reference: Ren, M., Zhang S. and Wang J.
(2022). "Consistent Estimation of the Number of Communities via
Regularized Network Embedding". Biometrics, <doi:10.1111/biom.13815>.

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
