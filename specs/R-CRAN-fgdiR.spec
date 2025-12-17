%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fgdiR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Gait Deviation Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-refund 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-refund 

%description
A typical gait analysis requires the examination of the motion of nine
joint angles on the left-hand side and six joint angles on the right-hand
side across multiple subjects. Due to the quantity and complexity of the
data, it is useful to calculate the amount by which a subject’s gait
deviates from an average normal profile and to represent this deviation as
a single number. Such a measure can quantify the overall severity of a
condition affecting walking, monitor progress, or evaluate the outcome of
an intervention prescribed to improve the gait pattern. This R package
provides tools for computing the Functional Gait Deviation Index, a novel
index for quantifying gait pathology using multivariate functional
principal component analysis. The package supports analysis at the level
of both legs combined, individual legs, and individual joints/planes. It
includes functions for functional data preprocessing, multivariate
functional principal component decomposition, FGDI computation, and
visualisation of gait abnormality scores. Further details can be found in
Minhas, S. K., Sangeux, M., Polak, J., & Carey, M. (2025). The Functional
Gait Deviation Index. Journal of Applied Statistics
<doi:10.1080/02664763.2025.2514150>.

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
