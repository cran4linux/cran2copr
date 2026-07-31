%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psychnets
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Clean-Room Psychological Network Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-stats 

%description
Provides clean-room implementations for estimating psychometric network
models, including correlation and partial-correlation networks, Gaussian
graphical models with extended Bayesian information criterion (EBIC)
regularization, nonparanormal and stepwise selection variants,
information-filtering networks (the triangulated maximally filtered graph
and the local-global inverse covariance), relative-importance networks,
and Ising and mixed graphical models <doi:10.3758/s13428-017-0862-1>
<doi:10.1007/978-3-031-54464-4_19>. All methods are implemented from first
principles in base R without compiled dependencies and return consistent,
tidy outputs. Functions are designed to be transparent and report
optimization diagnostics where applicable. For Gaussian graphical models,
the graphical lasso stationarity (Karush-Kuhn-Tucker) residual quantifies
the deviation of the estimated solution from the optimum of the
corresponding convex optimization problem.

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
