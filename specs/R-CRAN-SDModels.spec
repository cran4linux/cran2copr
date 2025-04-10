%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SDModels
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Spectrally Deconfounded Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GPUmatrix 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-locatexec 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-grplasso 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GPUmatrix 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-locatexec 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-grplasso 
Requires:         R-CRAN-rlang 

%description
Screen for and analyze non-linear sparse direct effects in the presence of
unobserved confounding using the spectral deconfounding techniques (Ćevid,
Bühlmann, and Meinshausen (2020)<jmlr.org/papers/v21/19-545.html>, Guo,
Ćevid, and Bühlmann (2022) <doi:10.1214/21-AOS2152>). These methods have
been shown to be a good estimate for the true direct effect if we observe
many covariates, e.g., high-dimensional settings, and we have fairly dense
confounding. Even if the assumptions are violated, it seems like there is
not much to lose, and the deconfounded models will, in general, estimate a
function closer to the true one than classical least squares optimization.
'SDModels' provides functions SDAM() for Spectrally Deconfounded Additive
Models (Scheidegger, Guo, and Bühlmann (2025) <doi:10.1145/3711116>) and
SDForest() for Spectrally Deconfounded Random Forests (Ulmer, Scheidegger,
and Bühlmann (2025) <doi:10.48550/arXiv.2502.03969>).

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
