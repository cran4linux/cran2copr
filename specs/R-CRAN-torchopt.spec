%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  torchopt
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Optimizers for Torch

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-torch 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-torch 

%description
Optimizers for 'torch' deep learning library. These functions include
recent results published in the literature and are not part of the
optimizers offered in 'torch'. Prospective users should test these
optimizers with their data, since performance depends on the specific
problem being solved.  The packages includes the following optimizers: (a)
'adabelief' by Zhuang et al (2020), <arXiv:2010.07468>; (b) 'adabound' by
Luo et al.(2019), <arXiv:1902.09843>; (c) 'adahessian' by Yao et al.(2021)
<arXiv:2006.00719>; (d) 'adamw' by Loshchilov & Hutter (2019),
<arXiv:1711.05101>; (e) 'madgrad' by Defazio and Jelassi (2021),
<arXiv:2101.11075>; (f) 'nadam' by Dozat (2019),
<https://openreview.net/pdf/OM0jvwB8jIp57ZJjtNEZ.pdf>; (g) 'qhadam' by Ma
and Yarats(2019), <arXiv:1810.06801>; (h) 'radam' by Liu et al. (2019),
<arXiv:1908.03265>; (i) 'swats' by Shekar and Sochee (2018),
<arXiv:1712.07628>; (j) 'yogi' by Zaheer et al.(2019),
<https:://papers.nips.cc/paper/8186-adaptive-methods-for-nonconvex-optimization>.

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
