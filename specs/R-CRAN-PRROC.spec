%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PRROC
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Precision-Recall and ROC Curves for Weighted and Unweighted Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-rlang 

%description
Computes the areas under the precision-recall (PR) and ROC curve for
weighted (e.g., soft-labeled) and unweighted data. In contrast to other
implementations, the interpolation between points of the PR curve is done
by a non-linear piecewise function. In addition to the areas under the
curves, the curves themselves can also be computed and plotted by a
specific S3-method. References: Davis and Goadrich (2006)
<doi:10.1145/1143844.1143874>; Keilwagen et al. (2014)
<doi:10.1371/journal.pone.0092209>; Grau et al. (2015)
<doi:10.1093/bioinformatics/btv153>.

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
