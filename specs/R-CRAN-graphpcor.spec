%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  graphpcor
%global packver   0.1.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.24
Release:          1%{?dist}%{?buildtag}
Summary:          Models for Correlation Matrices Based on Graphs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-INLAtools >= 0.0.8
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-INLAtools >= 0.0.8
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Implement some models for correlation/covariance matrices including two
approaches to model correlation matrices from a graphical structure. One
use latent parent variables as proposed in Sterrantino et. al. (2024)
<doi:10.1007/s10260-025-00788-y>. The other uses a graph to specify
conditional relations between the variables. The graphical structure makes
correlation matrices interpretable and avoids the quadratic increase of
parameters as a function of the dimension. In the first approach a natural
sequence of simpler models along with a complexity penalization is used.
The second penalizes deviations from a base model. These can be used as
prior for model parameters, considering C code through the 'cgeneric'
interface for the 'INLA' package (<https://www.r-inla.org>). This allows
one to use these models as building blocks combined and to other latent
Gaussian models in order to build complex data models.

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
