%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  brsim
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Brainerd-Robinson Similarity Coefficient Matrix

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 4.0.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-RcmdrMisc >= 2.7.0
BuildRequires:    R-CRAN-cluster >= 2.1.4
BuildRequires:    R-CRAN-corrplot >= 0.92
Requires:         R-grDevices >= 4.0.0
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-RcmdrMisc >= 2.7.0
Requires:         R-CRAN-cluster >= 2.1.4
Requires:         R-CRAN-corrplot >= 0.92

%description
Provides the facility to calculate the Brainerd-Robinson similarity
coefficient for the rows of an input table, and to calculate the
significance of each coefficient based on a permutation approach; a
heatmap is produced to visually represent the similarity matrix.
Optionally, hierarchical agglomerative clustering can be performed and the
silhouette method is used to identify an optimal number of clusters; the
results of the clustering can be optionally used to sort the heatmap.

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
