%global packname  RespirAnalyzer
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis Functions of Respiratory Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-signal 
Requires:         R-CRAN-pracma 

%description
Provides functions for the complete analysis of respiratory data. Consists
of a set of functions that allow to preprocessing respiratory data,
calculate both regular statistics and nonlinear statistics, conduct group
comparison and visualize the results. Especially, Power Spectral Density
('PSD') (A. Eke (2000) <doi:10.1007/s004249900135>), 'MultiScale
Entropy(MSE)' ('Madalena Costa(2002)' <doi:10.1103/PhysRevLett.89.068102>)
and 'MultiFractal Detrended Fluctuation Analysis(MFDFA)' ('Jan
W.Kantelhardt' (2002) <doi:10.1016/S0378-4371(02)01383-3>) were applied
for the analysis of respiratory data.

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
