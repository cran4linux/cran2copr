%global packname  rTorch
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Bindings to 'PyTorch'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-reticulate >= 1.10
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-reticulate >= 1.10
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-utils 
Requires:         R-methods 

%description
'R' implementation and interface of the Machine Learning platform
'PyTorch' <https://pytorch.org/> developed in 'Python'. It requires a
'conda' environment with 'torch' and 'torchvision' Python packages to
provide 'PyTorch' functions, methods and classes. The key object in
'PyTorch' is the tensor which is in essence a multidimensional array.
These tensors are fairly flexible in performing calculations in CPUs as
well as 'GPUs' to accelerate tensor operations.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
