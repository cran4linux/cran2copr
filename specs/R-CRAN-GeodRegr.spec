%global __brp_check_rpaths %{nil}
%global packname  GeodRegr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geodesic Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.6.2
BuildRequires:    R-CRAN-zipfR >= 0.6.66
Requires:         R-stats >= 3.6.2
Requires:         R-CRAN-zipfR >= 0.6.66

%description
Provides a gradient descent algorithm to find a geodesic relationship
between real-valued independent variables and a manifold-valued dependent
variable (i.e. geodesic regression). Available manifolds are Euclidean
space, the sphere, and Kendall's 2-dimensional shape space. Besides the
standard least-squares loss, the least absolute deviations, Huber, and
Tukey biweight loss functions can also be used to perform robust geodesic
regression. Functions to help choose appropriate cutoff parameters to
maintain high efficiency for the Huber and Tukey biweight estimators are
included. The k-sphere is a k-dimensional manifold: we represent it as a
sphere of radius 1 and center 0 embedded in (k+1)-dimensional space.
Kendall's 2D shape space with K landmarks is of real dimension 2K-4;
preshapes are represented as complex K-vectors with mean 0 and magnitude
1. Details are described in Shin, H.-Y. and Oh, H.-S. (2020)
<arXiv:2007.04518>. Also see Fletcher, P. T. (2013)
<doi:10.1007/s11263-012-0591-y> and Kim, H. J., Adluru, N., Collins, M.
D., Chung, M. K., Bendin, B. B., Johnson, S. C., Davidson, R. J. and
Singh, V. (2014) <doi:10.1109/CVPR.2014.352>.

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
