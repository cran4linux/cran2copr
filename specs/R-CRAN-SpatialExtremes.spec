%global __brp_check_rpaths %{nil}
%global packname  SpatialExtremes
%global packver   2.0-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling Spatial Extremes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-fields 

%description
Tools for the statistical modelling of spatial extremes using max-stable
processes, copula or Bayesian hierarchical models. More precisely, this
package allows (conditional) simulations from various parametric
max-stable models, analysis of the extremal spatial dependence, the
fitting of such processes using composite likelihoods or least square
(simple max-stable processes only), model checking and selection and
prediction. Other approaches (although not completely in agreement with
the extreme value theory) are available such as the use of (spatial)
copula and Bayesian hierarchical models assuming the so-called conditional
assumptions. The latter approaches is handled through an (efficient) Gibbs
sampler. Some key references: Davison et al. (2012)
<doi:10.1214/11-STS376>, Padoan et al. (2010)
<doi:10.1198/jasa.2009.tm08577>, Dombry et al. (2013)
<doi:10.1093/biomet/ass067>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
