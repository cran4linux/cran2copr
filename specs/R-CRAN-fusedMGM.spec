%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fusedMGM
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of Fused MGM to Infer 2-Class Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-bigalgebra 
BuildRequires:    R-CRAN-biganalytics 
Requires:         R-CRAN-fastDummies 
Requires:         R-parallel 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-bigalgebra 
Requires:         R-CRAN-biganalytics 

%description
Implementation of fused Markov graphical model (FMGM; Park and Won, 2022).
The functions include building mixed graphical model (MGM) objects from
data, inference of networks using FMGM, stable edge-specific penalty
selection (StEPS) for the determination of penalization parameters, and
the visualization. For details, please refer to Park and Won (2022)
<doi:10.48550/arXiv.2208.14959>.

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
