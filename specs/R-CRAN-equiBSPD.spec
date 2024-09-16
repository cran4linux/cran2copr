%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  equiBSPD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Equivalent Estimation Balanced Split Plot Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
In agricultural, post-harvest and processing, engineering and industrial
experiments factors are often differentiated with ease with which they can
change from experimental run to experimental run. This is due to the fact
that one or more factors may be expensive or time consuming to change i.e.
hard-to-change factors. These factors restrict the use of complete
randomization as it may make the experiment expensive and time consuming.
Split plot designs can be used for such situations. In general model
estimation of split plot designs require the use of generalized least
squares (GLS). However for some split-plot designs ordinary least squares
(OLS) estimates are equivalent to generalized least squares (GLS)
estimates. These types of designs are known in literature as
equivalent-estimation split-plot design. For method details see, Macharia,
H. and Goos, P.(2010) <doi:10.1080/00224065.2010.11917833>.Balanced split
plot designs are designs which have an equal number of subplots within
every whole plot. This package used to construct equivalent estimation
balanced split plot designs for different experimental set ups along with
different statistical criteria to measure the performance of these
designs. It consist of the function equivalent_BSPD().

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
