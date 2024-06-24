%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CerioliOutlierDetection
%global packver   1.1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.15
Release:          1%{?dist}%{?buildtag}
Summary:          Outlier Detection Using the Iterated RMCD Method of Cerioli (2010)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase >= 0.91.1
Requires:         R-CRAN-robustbase >= 0.91.1

%description
Implements the iterated RMCD method of Cerioli (2010) for multivariate
outlier detection via robust Mahalanobis distances. Also provides the
finite-sample RMCD method discussed in the paper, as well as the methods
provided in Hardin and Rocke (2005) <doi:10.1198/106186005X77685> and
Green and Martin (2017)
<https://christopherggreen.github.io/papers/hr05_extension.pdf>. See also
Chapter 2 of Green (2017)
<https://digital.lib.washington.edu/researchworks/handle/1773/40304>.

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
