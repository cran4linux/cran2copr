%global __brp_check_rpaths %{nil}
%global packname  serp
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Smooth Effects on Response Penalty for CLM

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ordinal >= 2016.12.12
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-stats 
Requires:         R-CRAN-ordinal >= 2016.12.12
Requires:         R-CRAN-crayon 
Requires:         R-stats 

%description
A regularization method for the cumulative link models.  The
smooth-effect-on-response penalty (SERP) provides flexible modelling of
the ordinal model by enabling the smooth transition from the general
cumulative link model to a coarser form of the same model. In other words,
as the tuning parameter goes from zero to infinity, the subject-specific
effects associated with each variable in the model tend to a unique global
effect. The parameter estimates of the general cumulative model are mostly
unidentifiable or at least only identifiable within a range of the entire
parameter space. Thus, by maximizing a penalized rather than the usual
non-penalized log-likelihood, this and other numerical problems common
with the general model are to a large extent eliminated. Fitting is via a
modified Newton's method. Several standard model performance and
descriptive methods are also available. For more details on the penalty
implemented here, see, Ugba (2021) <doi:10.21105/joss.03705> and Ugba et
al. (2021) <doi:10.3390/stats4030037>.

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
