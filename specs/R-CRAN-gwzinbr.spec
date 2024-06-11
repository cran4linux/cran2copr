%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gwzinbr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geographically Weighted Zero Inflated Negative Binomial Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-sp 

%description
Fits a geographically weighted regression model using zero inflated
probability distributions. Has the zero inflated negative binomial
distribution (zinb) as default, but also accepts the zero inflated Poisson
(zip), negative binomial (negbin) and Poisson distributions. Can also fit
the global versions of each regression model. Da Silva, A. R. & De Sousa,
M. D. R. (2023). "Geographically weighted zero-inflated negative binomial
regression: A general case for count data", Spatial Statistics
<doi:10.1016/j.spasta.2023.100790>. Brunsdon, C., Fotheringham, A. S., &
Charlton, M. E. (1996). "Geographically weighted regression: a method for
exploring spatial nonstationarity", Geographical Analysis,
<doi:10.1111/j.1538-4632.1996.tb00936.x>. Yau, K. K. W., Wang, K., & Lee,
A. H. (2003). "Zero-inflated negative binomial mixed regression modeling
of over-dispersed count data with extra zeros", Biometrical Journal,
<doi:10.1002/bimj.200390024>.

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
