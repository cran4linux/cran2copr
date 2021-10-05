%global __brp_check_rpaths %{nil}
%global packname  latentcor
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Computation of Latent Correlations for Mixed Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-fMultivar 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-chebpol 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-heatmaply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-doRNG 
Requires:         R-stats 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-fMultivar 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-chebpol 
Requires:         R-CRAN-Matrix 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-heatmaply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-graphics 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-future 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-doRNG 

%description
The first stand-alone R package for computation of latent correlation that
takes into account all variable types
(continuous/binary/ordinal/zero-inflated), comes with an optimized memory
footprint, and is computationally efficient, essentially making latent
correlation estimation almost as fast as rank-based correlation
estimation. The estimation is based on latent copula Gaussian models. For
continuous/binary types, see Fan, J., Liu, H., Ning, Y., and Zou, H.
(2017) <doi:10.1111/rssb.12168>. For ternary type, see Quan X., Booth J.G.
and Wells M.T. (2018) <arXiv:1809.06255>. For truncated type or
zero-inflated type, see Yoon G., Carroll R.J. and Gaynanova I. (2020)
<doi:10.1093/biomet/asaa007>. For approximation method of computation, see
Yoon G., Müller C.L. and Gaynanova I. (2021)
<doi:10.1080/10618600.2021.1882468>.

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
