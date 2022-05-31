%global __brp_check_rpaths %{nil}
%global packname  pedometrics
%global packver   0.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Pedometric Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 

%description
An R implementation of methods employed in the field of pedometrics, soil
science discipline dedicated to studying the spatial, temporal, and
spatio-temporal variation of soil using statistical and computational
methods. The methods found here include the calibration of linear
regression models using covariate selection strategies, computation of
summary validation statistics for predictions, generation of summary
plots, evaluation of the local quality of a geostatistical model of
uncertainty, and so on. Other functions simply extend the functionalities
of or facilitate the usage of functions from other packages that are
commonly used for the analysis of soil data. Formerly available versions
of suggested packages no longer available from CRAN can be obtained from
the CRAN archive <https://cran.r-project.org/src/contrib/Archive/>.

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
