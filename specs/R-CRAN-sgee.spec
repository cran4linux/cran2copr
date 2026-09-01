%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sgee
%global packver   0.6-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Stagewise Generalized Estimating Equations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-copula 
Requires:         R-stats 
Requires:         R-utils 

%description
Stagewise techniques implemented with Generalized Estimating Equations to
handle individual, group, bi-level, and interaction selection. Stagewise
approaches start with an empty model and slowly build the model over
several iterations, which yields a 'path' of candidate models from which
model selection can be performed. This 'slow brewing' approach gives
stagewise techniques a unique flexibility that allows simple incorporation
of Generalized Estimating Equations; see Vaughan, G., Aseltine, R., Chen,
K., Yan, J., (2017) <doi:10.1111/biom.12669> for details.

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
