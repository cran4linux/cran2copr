%global __brp_check_rpaths %{nil}
%global packname  NonParRolCor
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          a Non-Parametric Statistical Significance Test for Rolling Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-scales 

%description
Estimates and plots (as a heat map) the statistical significance of
rolling window correlation coefficients, which is carried out through a
non-parametric computing-intensive method. This method addresses the
effects due to the multiple testing (inflation of the Type I error) when
the statistical significance is estimated for the rolling window
correlation coefficients. The method is based on Monte Carlo simulations
by permuting one of the variables (dependent) under analysis and keeping
fixed the other variable (independent). We improve the computational
efficiency of this method to reduce the computation time through parallel
computing. The 'NonParRolCor' package also provides examples with
synthetic and real-life ecological time series to exemplify its use.
Methods derived from R. Telford (2013)
<https://quantpalaeo.wordpress.com/2013/01/04/> and J.M. Polanco-Martinez
(2020) <doi:10.1016/j.ecoinf.2020.101163>.

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
