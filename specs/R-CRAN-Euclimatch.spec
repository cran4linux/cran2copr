%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Euclimatch
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Euclidean Climatch Algorithm

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 

%description
An interface for performing climate matching using the Euclidean
"Climatch" algorithm. Functions provide a vector of climatch scores (0-10)
for each location (i.e., grid cell) within the recipient region, the
percent of climatch scores >= a threshold value, and mean climatch score.
Tools for parallelization and visualizations are also provided. Note that
the floor function that rounds the climatch score down to the nearest
integer has been removed in this implementation and the “Climatch”
algorithm, also referred to as the “Climate” algorithm, is described in:
Crombie, J., Brown, L., Lizzio, J., & Hood, G. (2008). “Climatch user
manual”. The method for the percent score is described in: Howeth, J.G.,
Gantz, C.A., Angermeier, P.L., Frimpong, E.A., Hoff, M.H., Keller, R.P.,
Mandrak, N.E., Marchetti, M.P., Olden, J.D., Romagosa, C.M., and Lodge,
D.M. (2016). <doi:10.1111/ddi.12391>.

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
