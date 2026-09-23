%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  binest
%global packver   0.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Group Means and SDs from Binned Count Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 

%description
Education agencies often report school or district score distributions as
the number of students scoring in each of several score ranges, or bins,
separated by threshold scores, or cuts.  The functions in the binest
package translate those bin counts into estimates of the mean and standard
deviation (SD).  They do so using the heteroskedastic ordered probit
(HETOP) model, which assumes that scores follow a normal distribution
within each school or district, each of which has its own mean and SD.
The binest package includes the fast_hetop() function, which fits the
model much more quickly than previous implementations.  The model is
described by Reardon, Shear, Castellano and Ho (2017)
<doi:10.3102/1076998616666279>; a Bayesian variant is described by
Lockwood, Castellano and Shear (2018) <doi:10.3102/1076998618795124>.

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
