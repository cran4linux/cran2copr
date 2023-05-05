%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MSclust
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple-Scaled Clustering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GGally 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GGally 

%description
Model based clustering using the multivariate multiple Scaled t (MST) and
multivariate multiple scaled contaminated normal (MSCN) distributions. The
MST is an extension of the multivariate Student-t distribution to include
flexible tail behaviors, Forbes, F. & Wraith, D. (2014)
<doi:10.1007/s11222-013-9414-4>. The MSCN represents a heavy-tailed
generalization of the multivariate normal (MN) distribution to model
elliptical contoured scatters in the presence of mild outliers (also
referred to as "bad" points) and automatically detect bad points, Punzo,
A. & Tortora, C. (2021) <doi:10.1177/1471082X19890935>.

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
