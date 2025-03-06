%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ebm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Explainable Boosting Machines

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 0.9.0
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-lattice 
Requires:         R-CRAN-ggplot2 >= 0.9.0
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-lattice 

%description
An interface to the 'Python' 'InterpretML' framework for fitting
explainable boosting machines (EBMs); see Nori et al. (2019)
<doi:10.48550/arXiv.1909.09223> for details. EBMs are a modern type of
generalized additive model that use tree-based, cyclic gradient boosting
with automatic interaction detection. They are often as accurate as
state-of-the-art blackbox models while remaining completely interpretable.

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
