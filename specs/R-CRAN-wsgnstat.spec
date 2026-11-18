%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wsgnstat
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Wrapped Two-Piece Exponential Power Distribution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
Requires:         R-stats 

%description
The two-piece exponential power distribution on the line (Fernández and
Steel, 1998, <doi:10.1080/01621459.1998.10474117>) and its wrapped version
on the circle, treated as a uniform scale mixture with generalised gamma
mixing (Ehlers, 2015, <doi:10.1080/01966324.2014.969460>). Given the
mixing variable, the variable is uniform on an interval that contains the
location. The package name follows the authors' earlier usage, the wrapped
skew generalised normal distribution. Density, distribution and quantile
functions, random generation from the mixture, and the characteristic
function and trigonometric moments for every shape parameter, evaluated on
a rotated path of integration, with the convergent series as a check. The
wrapped density adds an Euler-Maclaurin tail to the image sum, so small
shapes are covered. Maximum likelihood fitting of the four-parameter
wrapped distribution under a lower bound on the shape, over both the
regular and the spike branch, with the location searched over the
observations when the shape is at most one; the grouped likelihood for
rounded data; profile likelihoods; and standard errors from the expected
information or a parametric bootstrap. A pure-C back-end does the numerics
and also backs the 'Python' package 'wsgnstat'.

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
