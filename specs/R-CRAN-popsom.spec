%global packname  popsom
%global packver   4.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.0
Release:          1%{?dist}
Summary:          Functions for Constructing and Evaluating Self-Organizing Maps

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-som 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-som 
Requires:         R-class 
Requires:         R-CRAN-fields 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 

%description
A self-organizing map package with three distinguishing features: (1)
Automatic cluster centroid detection and visualization using starbursts
(2) Convergence index, a statistical quality measure based on the linear
combination of map embedding and estimated topographic accuracy (3) A very
efficient stochastic training algorithm based on ideas from tensor
algebra.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
