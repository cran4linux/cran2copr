%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CompExpDes
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Computer Experiment Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
In computer experiments space-filling designs are having great impact.
Most popularly used space-filling designs are Uniform designs (UDs), Latin
hypercube designs (LHDs) etc. For further references one can see Mckay
(1979) <DOI:10.1080/00401706.1979.10489755> and Fang (1980)
<https://cir.nii.ac.jp/crid/1570291225616774784>. In this package, we have
provided algorithms for generate efficient LHDs and UDs. Here, generated
LHDs are efficient as they possess lower value of Maxpro measure, Phi_p
value and Maximum Absolute Correlation (MAC) value based on the weightage
given to each criterion. On the other hand, the produced UDs are having
good space-filling property as they always attain the lower bound of
Discrete Discrepancy measure. Further, some useful functions added in this
package for adding more value to this package.

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
