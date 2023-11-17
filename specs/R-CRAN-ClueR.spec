%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClueR
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-e1071 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
CLUster Evaluation (CLUE) is a computational method for identifying
optimal number of clusters in a given time-course dataset clustered by
cmeans or kmeans algorithms and subsequently identify key kinases or
pathways from each cluster. Its implementation in R is called ClueR. See
README on <https://github.com/PYangLab/ClueR> for more details. P Yang et
al. (2015) <doi:10.1371/journal.pcbi.1004403>.

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
