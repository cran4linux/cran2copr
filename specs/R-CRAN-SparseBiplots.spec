%global packname  SparseBiplots
%global packver   4.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.0
Release:          1%{?dist}
Summary:          'HJ-Biplot' using Different Ways of Penalization Plotting with'ggplot2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sparsepca 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-sparsepca 
Requires:         R-CRAN-testthat 

%description
'HJ-Biplot' is a multivariate method that allow represent multivariate
data on a subspace of low dimension, in such a way that most of the
variability of the information is captured in a few dimensions. This
package implements three new techniques and constructs in each case the
'HJ-Biplot', adapting restrictions to reduce weights and / or produce zero
weights in the dimensions, based on the regularization theories. It
implements three methods of regularization: Ridge, LASSO and Elastic Net.

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
