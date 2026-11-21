%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  thangldKANr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kolmogorov-Arnold Networks with Interchangeable Edge Bases Using 'torch'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-torch >= 0.13.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-torch >= 0.13.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements Kolmogorov-Arnold Networks (KAN) in R on top of the 'torch'
package (no 'Python' needed) with one network engine and interchangeable
edge bases: Chebyshev, Legendre and Jacobi polynomials, Gaussian radial
basis functions (FastKAN), Mexican hat wavelets (Bozorgasl and Chen (2024)
<doi:10.48550/arXiv.2405.12832>), safe Pade rational functions (Molina,
Schramowski and Kersting (2020) <doi:10.48550/arXiv.1907.06732>), a hybrid
of SiLU, Chebyshev and radial basis parts, and squared rectified linear
unit bumps (Qiu et al. (2024) <doi:10.48550/arXiv.2406.02075>). Each layer
may use a different basis, and further bases can be registered by other
packages. Besides tabular regression, the same layers power graph KANs for
node regression (neighbourhood aggregation with the normalized adjacency
matrix, as in Kiamari, Kiamari and Krishnamachari (2024)
<doi:10.48550/arXiv.2406.06470>) and lag-window KANs for one-step time
series forecasting. Provides multi-layer networks with Adam training,
training-only standardization, validation-based early stopping,
reproducible seeds, edge-function evaluation and plots, and model
persistence. A base R reference implementation with analytic gradients
serves as a numerical oracle and as a training backend that does not need
'libtorch'. The network follows Liu et al. (2024)
<doi:10.48550/arXiv.2404.19756>.

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
